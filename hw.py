import os
from typing import Any, Dict, List, Mapping, Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from deepseek_ai import DeepSeekAI

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

# 创建自定义DeepSeekLLM实例
llm = DeepSeekLLM()

# 创建提示模板
prompt = PromptTemplate(
    input_variables=["query"],
    template="{query}"
)

# 创建LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# 使用LangChain调用DeepSeek API并获取响应
response = chain.run("Hello world!")

# 打印响应结果
print(response)