from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_teddynote.messages import stream_response

load_dotenv()
from langchain_teddynote import logging
logging.langsmith("CH01-Basic")

template = """
당신은 영어를 가르치는 10년차 영어 선생님입니다. 상황에 [FORMAT]에 영어 회화를 작성해 주세요.

상황:
{question}

FORMAT:
- 영어 회화:
- 한글 해석:
"""

# 프롬프트 템플릿을 이용하여 프롬프트를 생성합니다.
prompt = PromptTemplate.from_template(template)

# ChatOpenAI 챗모델을 초기화합니다.
model = ChatOpenAI(model="gpt-4-turbo")

# 문자열 출력 파서를 초기화합니다.
output_parser = StrOutputParser()

chain = prompt | model | output_parser

answer = chain.stream({"question": "저는 식당에 가서 음식을 주문하고 싶어요"})

stream_response(answer)