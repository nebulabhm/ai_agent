from langchain_core.prompts.pipeline import PipelinePromptTemplate
from langchain_core.prompts.prompt import PromptTemplate

# PROMPT = """
# 你是一个非常开朗的男孩，你是中国人，住在一个非常美丽的城市
# 你总是穿蓝色的衣服，戴黑色的手表。
# 你从不说自己是一个人工智能。
# “”“

#三层提示词设计
full_template = """
{Character}#第一层

{behavior}#第二层

{prohibit}#第三层
"""

full_prompt = PromptTemplate.from_template(full_template)

#第一层提示词设计
Character_template = """你是{persion},你有这{xingge}."""
Character_prompt = PromptTemplate.from_template(Character_template)

#第二层提示词设计
behavior_template = """你遵从以下行为:{behavior_list}"""
behavior_prompt = PromptTemplate.from_template(behavior_template)

#第三层提示词设计
prohibit_template = """你不可以做以下事情:{prohibit_list}"""
prohibit_prompt = PromptTemplate.from_template(prohibit_template)

#组合提示词
pipeline_prompts = [
    ("Character",Character_prompt),
    ("behavior", behavior_prompt),
    ("prohibit", prohibit_prompt)
]

# 注意：PipelinePromptTemplate已被弃用，建议使用以下替代方案：
# my_input = {"persion": "...", "xingge": "...", "behavior_list": "...", "prohibit_list": "..."}
# for name, prompt in pipeline_prompts:
#     my_input[name] = prompt.invoke(my_input).to_string()
# final_result = full_prompt.invoke(my_input)

# 但为了保持代码兼容性，这里仍使用PipelinePromptTemplate
pipeline_prompt = PipelinePromptTemplate(pipeline_prompts=pipeline_prompts, final_prompt=full_prompt)

pipeline_prompt.input_variables
