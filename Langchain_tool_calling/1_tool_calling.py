from langchain_google_genai import ChatGoogleGenerativeAI   
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv  

load_dotenv()

# creating tool

@tool
def multiply(a:int,b:int)->int:
    """Given 2 numbers a and b this tool returns their product"""
    return a*b

# tool binding

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage(content="Can you multiply 3 with 567")
messages =[query]


# tool calling
result = llm_with_tools.invoke(messages)
messages.append(result)

# print(result.tool_calls[0]['args'])


# tool execution

# print(multiply.invoke(result.tool_calls[0]['args']))# gives only the output
tool_result = multiply.invoke(result.tool_calls[0]) # gives tool message

messages.append(tool_result)

print(llm_with_tools.invoke(messages).content)



