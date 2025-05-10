"""
https://wikidocs.net/233345
06. LCEL 인터페이스

LCEL 인터페이스
사용자 정의 체인을 가능한 쉽게 만들 수 있도록, Runnable 프로토콜을 구현했습니다.

Runnable 프로토콜은 대부분의 컴포넌트에 구현되어 있습니다.

이는 표준 인터페이스로, 사용자 정의 체인을 정의하고 표준 방식으로 호출하는 것을 쉽게 만듭니다. 표준 인터페이스에는 다음이 포함됩니다.

- stream: 응답의 청크를 스트리밍합니다.
- invoke: 입력에 대해 체인을 호출합니다.
- batch: 입력 목록에 대해 체인을 호출합니다.

비동기 메소드도 있습니다.

- astream: 비동기적으로 응답의 청크를 스트리밍합니다.
- ainvoke: 비동기적으로 입력에 대해 체인을 호출합니다.
- abatch: 비동기적으로 입력 목록에 대해 체인을 호출합니다.
- astream_log: 최종 응답뿐만 아니라 발생하는 중간 단계를 스트리밍합니다.
"""

# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보로드
load_dotenv()

from langchain_teddynote import logging

# 프로젝트 이름을 입력합니다.
logging.langsmith("CH01-Basic")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ChatOpenAI 모델을 인스턴스화합니다.
model = ChatOpenAI()
# 주어진 토픽에 대한 농담을 요청하는 프롬프트 템플릿을 생성합니다.
prompt = PromptTemplate.from_template("{topic} 에 대하여 3문장으로 설명해줘.")
# 프롬프트와 모델을 연결하여 대화 체인을 생성합니다.
chain = prompt | model | StrOutputParser()

# chain.stream 메서드를 사용하여 '멀티모달' 토픽에 대한 스트림을 생성하고 반복합니다.
# end="" 인자는 출력 후 줄바꿈을 하지 않도록 설정
# flush=True 인자는 출력 버퍼를 즉시 비우도록 합니다
for token in chain.stream({"topic": "멀티모달"}):
    # 스트림에서 받은 데이터의 내용을 출력합니다. 줄바꿈 없이 이어서 출력하고, 버퍼를 즉시 비웁니다.
    print(token, end="", flush=True)