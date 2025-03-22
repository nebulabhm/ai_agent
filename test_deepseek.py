'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2025-03-22 20:49:10
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2025-03-22 21:05:50
FilePath: \ai_agent\test_deepseek.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from deepseek_ai import DeepSeekAI

# 创建Deepseek实例
# 请替换为你的API密钥
api_key = "sk-a639b14a94e04b0dbefd8d20b0cc243d"
ds = DeepSeekAI(api_key=api_key)
messages = [
    {"role": "user", "content": "介绍一下你自己"}
]

response = ds.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    max_tokens=1000,
    temperature=0.5
)

print(response.choices[0].message.content)
 