'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2025-03-22 21:50:57
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2025-03-23 09:36:59
FilePath: /ai_agent/hw.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
from typing import Any, Dict, List, Mapping, Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from deepseek_ai import DeepSeekAI
from langchain.schema import BaseOutputParser

# 设置API密钥
api_key = "sk-a639b14a94e04b0dbefd8d20b0cc243d"

# 创建自定义DeepSeek LLM类
class DeepSeekLLM(LLM):
    model_name: str = "deepseek-chat"
    max_tokens: int = 1000
    temperature: float = 0.5
    api_key: Optional[str] = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 使用实例变量而不是Pydantic字段存储client
        self._client = DeepSeekAI(api_key=self.api_key or api_key)
    
    @property
    def _llm_type(self) -> str:
        """
        The type identifier for the DeepSeek language model.
        
        Returns:
            str: A string literal "deepseek" representing the LLM type.
        """
        return "deepseek"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:

        messages = [{"role": "user", "content": prompt}]
        # 移除stop参数，DeepSeek API不支持该参数
        response = self._client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature
            # 移除stop参数
        )
        return response.choices[0].message.content

class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str) -> List[str]:
        """Parse the output of an LLM call."""
        return text.strip().split(", ")
    
# 创建自定义DeepSeekLLM实例
llm = DeepSeekLLM()

# 创建提示模板
prompt_template = PromptTemplate(
    input_variables=["query"],
    template="{query}"
)

# 创建RunnableSequence
chain = prompt_template | llm

# 创建起名大师的提示模板
name_prompt = PromptTemplate.from_template("你是一个{name}，请模仿示例起3个{country}名字，示例：男孩经常被叫做{boy}，女孩经常被叫做{girl}。请返回以逗号分割的列表形式。仅返回逗号分隔的列表，不要返回其他任何内容。")

# 创建起名大师的RunnableSequence
name_chain = name_prompt | llm

# 使用第一个RunnableSequence调用DeepSeek API并获取响应
response = chain.invoke({"query": "介绍一下你自己"})
print("自我介绍：")
print(response)

# 使用format方法格式化提示模板，然后将格式化后的字符串传递给LLM
formatted_prompt = name_prompt.format(name = "算命大师",country="中国特色的", boy="狗蛋", girl="翠花")
print("使用format方法的提示：")
print(formatted_prompt)
response = chain.invoke(formatted_prompt)
print("起名大师的回答：")
print(response)

# 使用CommaSeparatedListOutputParser解析起名大师的回答
parser = CommaSeparatedListOutputParser()
name_list = parser.parse(response)
print("格式化后的名字列表：")
print(name_list)




