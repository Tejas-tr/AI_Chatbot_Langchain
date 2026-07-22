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
    ('system', 'you are a friendly tutor and will answer to point.'),
    MessagesPlaceholder('history'),
    ('human', '{question}'),
])

# define model 
# gpt-5-nano
model = ChatOpenAI(model='gpt-4o-mini')

# parse output
parse = StrOutputParser()

chain = prompt | model | parse

# create empty history
hist = []

print('Chat with bot, type quit or exit to stop conversation')
while True:
    question = input('you : ')
    if (question.strip().lower()) in ['quit','exit']:
        break
    response = chain.invoke({'history': hist, 'question': question})
    print(response)
    hist.append(HumanMessage(question))
    hist.append(AIMessage(response))
    print(f' history row has {len(hist)} messages')




