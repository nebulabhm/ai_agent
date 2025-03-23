from langchain_core.prompts import PromptTemplate
from typing import List, Any

def hello_world():
    print("Hello, World!")
    
PROMPT = PromptTemplate(
    input_variables=["function_name", "source_code"],
    template="Function name: {function_name}\nSource code:\n{source_code}"
)

import inspect

def get_source_code(function_name):
    source_code = inspect.getsource(function_name)
    return source_code
    
# 自定义模板
class CustomPromptTemplate(PromptTemplate):
    def format(self, **kwargs: Any) -> str:
        # 获得源代码
        source_code = get_source_code(kwargs["function_name"])
        
        # 生成提示词模版
        prompt = PROMPT.format(
            function_name=kwargs["function_name"].__name__, source_code=source_code
        )
        
        return prompt

# 使用自定义模板
a = CustomPromptTemplate(input_variables=["function_name"], template="模板内容")
pm = a.format(function_name=hello_world)

print(pm)
     
     
#      # 和LLM连接起来
#      from hw import DeepSeekLLM
     
# )
#         return self.template.format(**kwargs)