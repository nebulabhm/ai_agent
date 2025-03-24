'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2025-03-24 22:43:57
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2025-03-24 22:47:52
FilePath: /ai_agent/share_propt.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from langchain.prompts import load_prompt

prompt = load_prompt("simple_prompt.yaml", encoding='utf-8')
print(prompt.format(name="小黑", what="吃什么"))

prompt = load_prompt("simple_prompt.json", encoding='utf-8')
print(prompt.format(name="小白", what="喝什么"))