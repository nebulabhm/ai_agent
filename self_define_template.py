from langchain_core.prompts import PromptTemplate
from typing import List, Any

def hello_world():
    print("Hello, World!")
    return "Hello, World!"
    
PROMPT = """\
你是一个代码生成器，你需要根据以下要求生成代码：

函数名称：{function_name}

源代码：{source_code}

代码解释：
"""

import inspect

def get_source_code(function_name):
    source_code = inspect.getsource(function_name)
    return source_code
    
# 自定义模板
class CustomPromptTemplate(PromptTemplate):
    def format(self, **kwargs: Any) -> str:
        # 获得源代码
        source_code = get_source_code(kwargs["function_name"])
        
        # 获取代码解释，如果没有提供则使用默认值
        code_explanation = kwargs.get("code_explanation", "这是一个函数的代码实现")
        
        # 生成提示词模版
        prompt = PROMPT.format(
            function_name=kwargs["function_name"].__name__, 
            source_code=source_code,
            code_explanation=code_explanation
        )
        
        return prompt

# 使用自定义模板
a = CustomPromptTemplate(input_variables=["function_name"], template="模板内容")
pm = a.format(function_name=hello_world)

print(pm)
     
     
# 和LLM连接起来
from hw import DeepSeekLLM

# 创建DeepSeekLLM实例
llm = DeepSeekLLM()

# 创建chain对象，将自定义模板与LLM连接起来
chain = llm

# 使用chain调用LLM并获取响应
response = chain.invoke(pm)
print(response)