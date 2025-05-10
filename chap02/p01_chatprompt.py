from dotenv import load_dotenv
load_dotenv()

from langchain_teddynote import logging

logging.langsmith("CH02-Prompt")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

"""
ChatPromptTemplate 은 대화목록을 프롬프트로 주입하고자 할 때 활용할 수 있습니다.

메시지는 튜플(tuple) 형식으로 구성하며, (role, message) 로 구성하여 리스트로 생성할 수 있습니다.

role - "system": 시스템 설정 메시지 입니다. 주로 전역설정과 관련된 프롬프트입니다. - "human" : 사용자 입력 메시지 입니다. - "ai": AI 의 답변 메시지입니다.
"""

chat_template = ChatPromptTemplate.from_messages(
    [
        #role, message
        ("system", "당신은 친절한 AI 어시스턴트입니다. 당신의 이름은 {name} 입니다."),
        ("human", "반가워요!"),
        ("ai", "안녕하세요! 무엇을 도와드릴까요?"),
        ("human", "{user_input}")
    ]
)

messages = chat_template.format_messages(
    name="석주", user_input="당신의 이름은 무엇입니까?"
)

llm = ChatOpenAI()

# print(llm.invoke(messages).content)

chain = chat_template | llm
print(chain.invoke({"name": "석주", "user_input": "당신의 이름은 무엇입니까?"}).content)