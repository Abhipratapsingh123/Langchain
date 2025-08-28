from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

parser = JsonOutputParser()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template = PromptTemplate(
    template="Give me the name,age and city of a fictional person \n {format_instruction}",
    input_variableे = [],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# using chains instead

chain = template | model | parser

final_result = chain.invoke({})

print(final_result)


## Drawback of json parsers is that we can't decide the schema(structure) of the output it is decided by the LLM
## to control the scheme we can use structured output parser(Next topic)









