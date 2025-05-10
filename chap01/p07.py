"""
https://wikidocs.net/233346
Runnable
"""

# .env 파일을 읽어서 환경변수로 설정
from dotenv import load_dotenv

# 토큰 정보로드
load_dotenv()
# LangSmith 추적을 설정합니다. https://smith.langchain.com
# !pip install -qU langchain-teddynote
from langchain_teddynote import logging

# 프로젝트 이름을 입력합니다.
logging.langsmith("CH01-Basic")

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


# prompt 와 llm 을 생성합니다.
prompt = PromptTemplate.from_template("{num} 의 10배는?")
llm = ChatOpenAI(temperature=0)

# chain 을 생성합니다.
chain = prompt | llm

# print(chain.invoke({"num": 5}))

from langchain_core.runnables import RunnablePassthrough

# runnable
runnable_chain = {"num": RunnablePassthrough()} | prompt | ChatOpenAI()

print(runnable_chain.invoke(10))