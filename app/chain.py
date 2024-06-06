
# chain.py에 우리의 로직이 들어가 있다.
# LCLE의 기반한 코드
# from langchain.chat_models import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
# pip install -U langchain-openai
# pip install -U langchain-community

from langchain_openai import ChatOpenAI

# langchain_community로 설치 후 대응
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# with open("openai.txt") as f:
#     docs = f.read()

# window cp949 이슈대응
with open("openai.txt", encoding='utf-8') as f:
    docs = f.read()

# task에는 우리가 알고 있는 입력이 들어오게 된다.
template = """Based on the following instrutions, help me write a good prompt TEMPLATE for the following task:

{task}

Notably, this prompt TEMPLATE expects that additional information will be provided by the end user of the prompt you are writing. For the piece(s) of information that they are expected to provide, please write the prompt in a format where they can be formatted into as if a Python f-string.

When you have enough information to create a good prompt, return the prompt in the following format:\n\n```prompt\n\n...\n\n```

Instructions for a good prompt:

{instructions}
"""
prompt = ChatPromptTemplate.from_messages([("system", template)]).partial(
    instructions=docs
)

# chain만 생성해 주면 끝이다. return 등은 없다. 호출이 없다.
chain = (
    prompt | ChatOpenAI(model="gpt-4-1106-preview", temperature=0) | StrOutputParser()
)