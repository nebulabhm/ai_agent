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

# 使用LangChain推荐的新方案替换已弃用的PipelinePromptTemplate
# 准备输入数据
my_input = {
    "persion": "一个善良的人",
    "xingge": "乐观开朗的性格",
    "behavior_list": "友善待人、乐于助人",
    "prohibit_list": "说谎、欺骗他人"
}

# 依次处理每个提示模板
for name, prompt in pipeline_prompts:
    # 使用invoke方法处理每个模板，并将结果转换为字符串
    my_input[name] = prompt.invoke(my_input).to_string()

# 使用full_prompt处理最终的组合结果
final_result = full_prompt.invoke(my_input)

# 打印最终结果
print("\n最终生成的提示词：")
print(final_result.to_string())
