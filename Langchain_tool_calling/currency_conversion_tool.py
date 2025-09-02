from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain import hub
import requests
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Define tools
# This tool fetches the currency conversion rate.
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency conversion factor between a given base currency and a target currency"""
    url = f"https://v6.exchangerate-api.com/v6/bc048cde424b4dbb5ac707/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    return data.get("conversion_rate")

# This tool calculates the final value using the rate from the first tool.
@tool
def convert(base_currency_value: int, conversion_rate: float) -> float:
    """given a currency conversion rate this function calculates the target currency values from a given base currency value"""
    return base_currency_value * conversion_rate

# Create the list of tools
tools = [get_conversion_factor, convert]

# Bind the tools to the LLM
llm_with_tools = llm.bind_tools(tools)

# Fetch a standard prompt for tool-calling agents
prompt = hub.pull("hwchase17/openai-tools-agent")

# Create the tool-calling agent
agent = create_tool_calling_agent(llm_with_tools, tools, prompt)

# Create the AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Invoke the executor with the complex request

result = agent_executor.invoke({
    "input": "What is the conversion factor between USD and INR, and based on this conversion factor convert 567 USD to INR?"
})

print("Final Output:", result['output'])

result2 = agent_executor.invoke({
    "input": "What is the capital of India and what is the value of indian rupee a compared to US dollar tell me the value of 1 dollar in INR"
})
print("Final Output:", result2['output'])
