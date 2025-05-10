from dotenv import load_dotenv
load_dotenv()

from langchain_teddynote import logging

logging.langsmith("CH01-Basic")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.1, # 창의성 (0.0 ~ 2.0)
    model="gpt-4o"
)

question = "대한민국의 수도는 어디인가요?"

response = llm.invoke(question)
print(f"[답변]: {response}")

print(response.content)

print(response.response_metadata)

"""
LogProb - 주어진 텍스트에 대한 모델의 토큰 확률의 로그 값
"""
llm_with_logprob = ChatOpenAI(
    temperature=0.1, # 창의성 (0.0 ~ 2.0)
    max_tokens=2048,
    model="gpt-3.5-turbo"
).bind(logprobs=True)

response = llm_with_logprob.invoke(question)

print(response.response_metadata)

"""
스트리밍 출력
- 질의에 대한 답변을 실시간으로 받을 때 유용
"""

answer = llm.stream("대한민국의 아름다운 관광지 10곳과 주소를 알려주세요!")
for token in answer:
    print(token.content, end="", flush=True)