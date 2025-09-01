from langchain_community.tools import DuckDuckGoSearchRun
# tools are runnables in langchain

search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke('Top news in India today')
print(result)