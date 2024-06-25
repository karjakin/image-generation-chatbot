from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
import json
import re

llm = OpenAI(api_key="sk-111111111111111111111111111111111111111111111111", base_url='http://127.0.0.1:5000/v1')
model = llm


prompt_template= PromptTemplate.from_template(
"GPT4 Correct User:" 
" {user_response}"
"<|end_of_turn|>")

prompt= prompt_template
chain = prompt | model

def ai_response(user_response):
    respuesta = chain.invoke({"user_response": user_response})
    return respuesta



user_response="hello, what is yout name?"
narracion = ai_response(user_response)
print(narracion)
