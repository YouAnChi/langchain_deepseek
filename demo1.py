from langchain_deepseek import ChatDeepSeek
import os
llm = ChatDeepSeek(
    model="deepseek-reasoner",
    # temperature=0,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
    api_key="sk-1ea9167338bc4daf945bf8a769ade25f1",
    base_url="https://api.deepseek.com/v1",
    # other params...
)

messages=[
        {"role": "user", "content": "langchain对于直接官方调用deepseek API有什么用？"}
]

# 使用流式输出显示回答
for chunk in llm.stream(messages):
    print(chunk.text(), end="")

