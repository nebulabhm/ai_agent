from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 使用from_messages方法创建聊天模板
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个起名大师，你的名字叫{name}。"),
        ("human", "你好，{name}。你感觉如何？"),
        ("ai", "你好！我的状态很好！"),
        ("human", "{user_input}"),
        ("ai", " 我叫{name}，你好！"),
        ("human", "你的爸爸是谁？"),
    ]
)

sy = SystemMessage(
    content="你是一个起名大师",
    additional_kwargs={"大师名字": "陈大师"}
)

hu = HumanMessage(
    content="请问大师叫什么？",
    additional_kwargs={"大师名字": "陈大师"}
)

ai = AIMessage(
    content="我叫陈大师",
    additional_kwargs={"大师名字": "陈大师"} 
)

[sy, hu, ai]
# 格式化模板并打印结果
formatted_template = chat_template.format(name="陈大师", user_input="你叫什么名字？")
print(formatted_template)