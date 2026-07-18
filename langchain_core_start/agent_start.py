import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from requests_toolbelt.downloadutils import stream

# 导入环境变量
load_dotenv()
base_url = os.getenv("DASHSCOPE_BASE_URL")
api_key = os.getenv("DASHSCOPE_API_KEY")

# 创建model
qwen = init_chat_model(
    model="qwen-max",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key
)
# 创建agent
agent = create_agent(model=qwen)


# 阻塞式访问
response = agent.invoke({
    "messages": [{"role": "user","content": "你是谁？"}]
})

# print(response)


# 流式调用
for token,metadata in agent.stream(
    {"messages": [{"role": "user","content": "你是谁？"}]},
    stream_mode="messages"
):
    if token.content:
        print(token.content,end="",flush=True)