from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# first we have to make a schema with the help of responsescehema

schema = [
    ResponseSchema(name='fact-1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact-2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact-3',description='Fact 3 about the topic')
]

# create parser

parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
template=(
        "Give 3 facts about the {topic}.\n"
        "Respond ONLY in JSON format with no extra text.\n"
        "{format_instruction}"
    ),
input_variables=['topic'],
partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)


# con is that we cannot validate the output of the LLM, so next topic(Pydantic)
