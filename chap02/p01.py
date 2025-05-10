from dotenv import load_dotenv
load_dotenv()

from langchain_teddynote import logging

logging.langsmith("CH02-Prompt")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

from langchain_core.prompts import PromptTemplate

# template 정의. {country}는 변수로, 이후에 값이 들어갈 자리를 의미
template = "{country}의 수도는 어디인가요?"

# from_template 메소드를 이용하여 PromptTemplate 객체 생성
prompt = PromptTemplate.from_template(template)
prompt.format(country="대한민국")

chain = prompt | llm

print(chain.invoke("대한민국").content)

template = "{country1}과 {country2}의 수도는 각각 어디인가요?"

prompt = PromptTemplate(
    template=template,
    input_variables=["country1"],
    partial_variables={
        "country2": "미국"  # dictionary 형태로 partial_variables를 전달
    },
)

prompt.format(country1="대한민국")
prompt_partial = prompt.partial(country2="캐나다")
prompt_partial.format(country1="대한민국")

chain = prompt_partial | llm

print(chain.invoke("대한민국").content)
