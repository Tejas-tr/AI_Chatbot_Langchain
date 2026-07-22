# to use OPEN AI model in LANGCHAIN
from langchain_openai import ChatOpenAI

# To create prompt in LANGCHAIN
# ChatPromptTemplate --> for normal prompting
# MessagesPlaceHolder --> create memory to store historical conversation
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# extract only required information from Model output
from langchain_core.output_parsers import StrOutputParser

# to define Human / user message and AI message in history
from langchain_core.messages import HumanMessage, AIMessage

# to connect .env for password
from dotenv import load_dotenv
load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ('system', 'you are a friendly tutor.'),
    MessagesPlaceholder('history'),
    ('human', '{question}'),
])

# define model
model = ChatOpenAI(model='gpt-5-nano')

chain = prompt | model

history = [HumanMessage('My name is Alex'), AIMessage('Hi Alex')]
print(chain.invoke({'history': history, 'question': 'what is my name'}).content)

