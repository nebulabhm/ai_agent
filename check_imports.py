import os
import sys

print('Working directory:', os.getcwd())
print('Python path:', sys.path)

try:
    from langchain_core.schema import SystemMessage, HumanMessage, AIMessage
    print('Successfully imported schema classes')
except ImportError as e:
    print('Import error:', e)

try:
    import langchain_core
    print('langchain_core modules:', dir(langchain_core))
except ImportError as e:
    print('Error importing langchain_core:', e)