import os
import sys
import subprocess
import importlib

print('Working directory:', os.getcwd())
print('Python path:', sys.path)

# 检查langchain-core版本
try:
    import langchain_core
    print('langchain_core version:', langchain_core.__version__)
    print('langchain_core modules:', dir(langchain_core))
except ImportError as e:
    print('Error importing langchain_core:', e)

# 尝试安装或升级langchain-core
print('\n尝试重新安装langchain-core...')
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'langchain-core>=0.1.0'])

# 重新加载模块
if 'langchain_core' in sys.modules:
    print('\n重新加载langchain_core模块...')
    importlib.reload(langchain_core)

# 再次检查schema模块
print('\n检查schema模块...')
try:
    from langchain_core.schema import SystemMessage, HumanMessage, AIMessage
    print('成功导入schema类！')
    print('SystemMessage:', SystemMessage)
    print('HumanMessage:', HumanMessage)
    print('AIMessage:', AIMessage)
except ImportError as e:
    print('导入schema错误:', e)

# 如果仍然无法导入，尝试查看langchain_core包的结构
print('\n检查langchain_core包结构...')
try:
    import langchain_core
    langchain_core_path = langchain_core.__path__[0]
    print('langchain_core路径:', langchain_core_path)
    print('langchain_core目录内容:')
    for item in os.listdir(langchain_core_path):
        print(f'  - {item}')
except Exception as e:
    print('检查包结构时出错:', e)