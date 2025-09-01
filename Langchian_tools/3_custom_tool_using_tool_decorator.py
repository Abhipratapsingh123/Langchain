from langchain_core.tools import tool


#step 1 create a function

def multiply(a,b):
    """Multiply two numbers"""
    return a*b

# add type hints

def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

#add tool decorator
@tool
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

# use

result = multiply.invoke({'a':3,'b':10})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)

# we send llm the schema of the function which is:

print(multiply.args_schema.model_json_schema())