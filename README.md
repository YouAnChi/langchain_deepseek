# LangChain DeepSeek 示例项目

这是一个使用 LangChain 框架调用 DeepSeek API 的示例项目。本项目展示了如何通过 LangChain 的接口简化与 DeepSeek 大语言模型的交互过程。

## 功能特点

- 支持 DeepSeek Reasoner 模型
- 实现流式输出（Stream）功能
- 简化的 API 调用方式
- 支持自定义参数配置

## 环境要求

- Python 3.9 或更高版本
- 虚拟环境（推荐使用）

## 安装步骤

1. 克隆项目并创建虚拟环境：
```bash
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
# 或
myenv\Scripts\activate  # Windows
```

2. 安装依赖包：
```bash
pip install langchain-deepseek
```

## 配置说明

使用前需要配置 DeepSeek API 密钥。在代码中设置以下参数：

```python
api_key = "your-api-key-here"  # 替换为你的 DeepSeek API 密钥
base_url = "https://api.deepseek.com/v1"  # DeepSeek API 的基础 URL
```

## 使用示例

项目中的 `demo1.py` 展示了基本用法：

```python
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model="deepseek-reasoner",
    api_key="your-api-key-here",
    base_url="https://api.deepseek.com/v1",
)

messages=[
    {"role": "user", "content": "你的问题"}
]

# 使用流式输出显示回答
for chunk in llm.stream(messages):
    print(chunk.text(), end="")
```

## 参数配置

`ChatDeepSeek` 类支持多个可选参数：

- `model`: 选择使用的模型（默认为 "deepseek-reasoner"）
- `temperature`: 控制输出的随机性（0-1之间）
- `max_tokens`: 限制生成的最大 token 数
- `timeout`: API 调用超时时间
- `max_retries`: 失败重试次数

## 注意事项

- 请确保 API 密钥的安全性，不要将其直接硬编码在代码中
- 建议使用环境变量来存储 API 密钥
- 注意控制 API 调用频率，避免超出使用限制

## 更多信息

- [DeepSeek API 文档](https://platform.deepseek.com/docs)
- [LangChain 文档](https://python.langchain.com/)