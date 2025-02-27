from langchain_deepseek import ChatDeepSeek
llm = ChatDeepSeek(
    model="deepseek-reasoner",
    # temperature=0,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
    api_key="sk-0ea9167338bc4daf945bf8a769ade25f",
    base_url="https://api.deepseek.com/v1",
    # other params...
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to 日语和中文."),
    ("human", "I love you."),
]

reasoning_content = ""
answer_content = ""
is_answering = False

print("\n" + "=" * 20 + "思考过程" + "=" * 20 + "\n")
for chunk in llm.stream(messages):
    if hasattr(chunk, 'additional_kwargs') and 'reasoning_content' in chunk.additional_kwargs:
        reasoning_content += chunk.additional_kwargs['reasoning_content']
        print(chunk.additional_kwargs['reasoning_content'], end='', flush=True)
    elif chunk.text():
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20 + "\n")
            is_answering = True
        answer_content += chunk.text()
        print(chunk.text(), end='', flush=True)

# 如果需要打印完整内容，可以取消下面的注释
# print("\n\n=== 完整推理过程 ===")
# print(reasoning_content)
# print("\n=== 完整翻译结果 ===")
# print(answer_content)
