from langchain_core.prompts import PromptTemplate

fstring_template = """
给我讲一个关于{name}的{what}故事
"""

jinja_template = "给我讲一个关于{name}的{what}故事"

prompt_fstring = PromptTemplate.from_template(fstring_template)
prompt_jinja = PromptTemplate.from_template(jinja_template)

response = prompt_fstring.format(name="孙悟空", what="火焰山")
print(response)

response = prompt_jinja.format(name="小狗", what="高兴")
print(response)