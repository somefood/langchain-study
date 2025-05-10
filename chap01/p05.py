"""
https://wikidocs.net/233344
LangChain Expression Language(LCEL)

PromptTemplate

사용자의 입력 변수를 사용하여 완전한 프롬프트 문자열을 만드는 데 사용되는 템플릿입니다
사용법
- template: 템플릿 문자열입니다. 이 문자열 내에서 중괄호 {}는 변수를 나타냅니다.
- input_variables: 중괄호 안에 들어갈 변수의 이름을 리스트로 정의합니다.
"""

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
from langchain_teddynote import logging
logging.langsmith("CH01-Basic")

from langchain_teddynote.messages import stream_response # 스트리밍 출력
from langchain_core.prompts import PromptTemplate

# template = "{country}의 수도는 어디인가요?"
#
# prompt_template = PromptTemplate.from_template(template)
#
# prompt = prompt_template.format(country="대한민국")
#
# model = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     max_tokens=2048,
#     temperature=0.1
# )

"""
LCEL(LangChain Expression Language)
- chain = prompt | model | output_parser
- | 기호는 unix 파이프 연산자와 유사하며, 서로 다른 구성 요소를 연결하고 한 구성 요소의 출력을 다음 구성 요소의 입력으로 전달합니다.
"""

prompt = PromptTemplate.from_template("{topic} 에 대해 쉽게 설명해주세요.")

model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

input = {"topic": "인공지능 모델의 학습 원리"}

response = chain.invoke(input)
print(response)
