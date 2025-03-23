from langchain_core.prompts.pipeline import PipelinePromptTemplate

# 打印文档字符串
print("PipelinePromptTemplate文档:")
print(PipelinePromptTemplate.__doc__)

# 打印参数信息
print("\n参数信息:")
import inspect
print(inspect.signature(PipelinePromptTemplate.__init__))