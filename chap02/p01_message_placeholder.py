from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

from langchain_teddynote import logging

logging.langsmith("CH02-Prompt")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

"""
ChatPromptTemplate 은 대화목록을 프롬프트로 주입하고자 할 때 활용할 수 있습니다.

메시지는 튜플(tuple) 형식으로 구성하며, (role, message) 로 구성하여 리스트로 생성할 수 있습니다.

role - "system": 시스템 설정 메시지 입니다. 주로 전역설정과 관련된 프롬프트입니다. - "human" : 사용자 입력 메시지 입니다. - "ai": AI 의 답변 메시지입니다.
"""

chat_prompt = ChatPromptTemplate.from_messages(
    [
        #role, message
        ("system", "당신은 요약 전문 AI 어시스턴트입니다. 당신의 임무는 주요 키워드로 대화를 요약하는 것입니다."),
        MessagesPlaceholder(variable_name="conversation"),
        ("human", "지금까지의 대화를 {word_count} 단어로 요약합니다."),
    ]
)

# formatted_chat_prompt = chat_prompt.format(
#     word_count=5,
#     conversation=[
#         ("human", "안녕하세요! 저는 오늘 새로 입사한 테디 입니다. 만나서 반갑습니다."),
#         ("ai", "반가워요! 앞으로 잘 부탁 드립니다."),
#     ],
# )

llm = ChatOpenAI()

# print(llm.invoke(messages).content)

chain = chat_prompt | llm | StrOutputParser()
result = chain.invoke({"word_count": 5, "conversation": [("human", "안녕하세요! 저는 오늘 새로 입사한 테디 입니다. 만나서 반갑습니다.",),
                                                         ("ai", "반가워요! 앞으로 잘 부탁 드립니다."), ], })

print(result)
