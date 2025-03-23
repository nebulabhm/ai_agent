from langchain_core.prompts import ChatPromptTemplate

# 使用from_messages方法创建聊天模板
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个起名大师，你的名字叫{name}。"),
        ("human", "你好，{name}。你感觉如何？"),
        ("ai", "你好！我的状态很好！"),
        ("human", "{user_input}"),
    ]
)

# 格式化模板并打印结果
formatted_template = chat_template.format(name="陈大师", user_input="你叫什么名字？")
print(formatted_template)