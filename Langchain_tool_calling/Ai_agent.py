from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain import hub
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key_weather = os.getenv("API_KEY_WEATHER")
api_key_currency_converter = os.getenv("API_KEY_CURRENCY_CONVERTER")
api_holiday_key = os.getenv("API_HOLIDAY_KEY")


# --------------------- tools section-----------------------------------------------#

# tool 1
# initializing the seach tool
search_tool = DuckDuckGoSearchRun()


# tool 2
@tool
def weather_forecast(location:str='India',days:int=7)->dict:
    """Fetches the weather forecast for a given location in India (default: 7-day forecast)."""
    location_query = f"{location},IN"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key_weather}&q={location_query}&days={days}&aqi=yes&alerts=yes"
    response = requests.get(url)
    data = response.json()
    #error check
    if "error" in data:
        return {"error": data["error"]["message"]}
    
    forecast = {
        "location": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "current_temp_C": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "forecast_days": []
    }
    for day in data["forecast"]["forecastday"]:
        forecast["forecast_days"].append({
            "date": day["date"],
            "max_temp_C": day["day"]["maxtemp_c"],
            "min_temp_C": day["day"]["mintemp_c"],
            "condition": day["day"]["condition"]["text"],
            "daily_chance_of_rain": day["day"]["daily_chance_of_rain"]
        })

    return forecast
   

# # tool 3 and 4 

# This tool fetches the currency conversion rate.
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency conversion factor between a given base currency and a target currency"""
    url = f"https://v6.exchangerate-api.com/v6/{api_key_currency_converter}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    return data.get("conversion_rate")

# This tool calculates the final value using the rate from the first tool.
@tool
def convert(base_currency_value: int, conversion_rate: float) -> float:
    """given a currency conversion rate this function calculates the target currency values from a given base currency value"""
    return base_currency_value * conversion_rate


# 5th tool
@tool
def get_holiday(date: str, country: str = "IN") -> dict:
    """
    Fetches holiday information for a given date and country.
    - date must be in format YYYY-MM-DD (e.g., "2025-10-02").
    - country must be a 2-letter ISO code (e.g., "IN" for India).
    """
    year, month, day = date.split("-")
    url = f"https://holidays.abstractapi.com/v1/?api_key={api_holiday_key}&country={country}&year={year}&month={month}&day={day}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"HTTP {response.status_code}"}
    
    data = response.json()
    if not data:
        return {"message": f"No holiday on {date} in {country}"}
    
    return {
        "date": data[0].get("date"),
        "name": data[0].get("name"),
        "type": data[0].get("type"),
        "location": data[0].get("location"),
    }

 
tools = [search_tool,weather_forecast,get_conversion_factor,convert,get_holiday]

# --------------------- tools section-----------------------------------------------#



# ------------------ LLM + AGENT ------------------

# llm object

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Fetch a standard prompt for tool-calling agents
prompt = hub.pull("hwchase17/openai-tools-agent")



# Create the tool-calling agent
agent = create_tool_calling_agent(llm, tools,prompt)

# agent executor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# ------------------ LLM + AGENT ------------------


chat_history = [
    SystemMessage(content="You are a helpful assistant which properly analyse user's query and help them with their query also you have access to various tools.If anyone ask you who made you just say `I am an agent made by Abhi pratap singh`")
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    chat_history.append(HumanMessage(content=user_input))  # store user input
    
    # Pass chat history as context (last few messages only if you want to save tokens)
    result = agent_executor.invoke({"input": user_input,"chat_history": chat_history})
    
    # Extract agent response
    ai_response = result.get("output", str(result))
    chat_history.append(AIMessage(content=ai_response))  # store AI reply
    
    print("AI:", ai_response)   

print("\nChat history:")
for msg in chat_history:
    print(f"{msg.type.upper()}: {msg.content}")


