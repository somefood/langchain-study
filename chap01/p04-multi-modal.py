"""
멀티모달 모델(이미지 인식)
- 멀티모달은 여러 가지 형태의 정보(모달)를 통합하여 처리하는 기술이나 접근 방식. 다양한 데이터 유형 포함
- 텍스트: 문서, 책, 웹 페이지 등의 글자로 된 정보
- 이미지: 사진, 그래픽, 그림 등 시각적 정보
- 오디오: 음성, 음악, 소리 효과 등의 청각적 정보
- 비디오: 동영상 클립, 실시간 스트리밍 등 시각적 및 청각적 정보의 결합
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

from langchain_teddynote.models import MultiModal
from langchain_teddynote.messages import stream_response
from langchain_teddynote import logging

logging.langsmith("CH01-Basic")


# 객체 생성
llm = ChatOpenAI(
    temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    max_tokens=2048,  # 최대 토큰수
    model="gpt-4o",  # 모델명
)

# 멀티모달 객체 생성
multimodal_llm = MultiModal(llm)

IMAGE_URL = "https://t3.ftcdn.net/jpg/03/77/33/96/360_F_377339633_Rtv9I77sSmSNcev8bEcnVxTHrXB4nRJ5.jpg"

# 이미지 파일로 부터 질의
answer = multimodal_llm.stream(IMAGE_URL)
# 스트리밍 방식으로 각 토큰을 출력합니다. (실시간 출력)
stream_response(answer)

# # 로컬 PC 에 저장되어 있는 이미지의 경로 입력
# IMAGE_PATH_FROM_FILE = "./images/sample-image.png"
#
# # 이미지 파일로 부터 질의(스트림 방식)
# answer = multimodal_llm.stream(IMAGE_PATH_FROM_FILE)
# # 스트리밍 방식으로 각 토큰을 출력합니다. (실시간 출력)
# stream_response(answer)