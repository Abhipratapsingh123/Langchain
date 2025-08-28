from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

# model creation
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# schema class for pydantic


class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="Give the sentiment of the feedback")


# creating pydantic parser
parser2 = PydanticOutputParser(pydantic_object=Feedback)

parser1 = StrOutputParser()

# Defining prompt
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback into positive or negative\n {feedback}\n{format_instruction}",
    input_variables=['text'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

# branch_chain = RunnableBranch(
#     (condition1,chain1),
#     (condition2,chain2),
#     default_chain
# )

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback, Donot give options just write the short response\n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback, Donot give options just write the short response\n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment=='positive', prompt2|model|parser1),
    (lambda x: x.sentiment=='negative', prompt3|model|parser1),
    RunnableLambda(lambda x: "couldnot find sentiment")
)

chain= classifier_chain|branch_chain

result = chain.invoke({'feedback':'This is a wonderful phone'})

print(result)

# visualising chain
chain.get_graph().print_ascii()