# 导入Langchain的初始化模型的函数
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from sqlalchemy import true

# 导入环境变量
load_dotenv()
base_url = os.getenv("DASHSCOPE_BASE_URL")
api_key = os.getenv("DASHSCOPE_API_KEY")

# 调用init_chat_model函数初始化模型，参数model用来指定模型名称，Langchain会根据模型名字自动设定base_url，并从环境变量中获取api_key
model = init_chat_model(
    model="qwen-max",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key
)

print(type(model))

# 阻塞式访问
# response = model.invoke("你是谁？")

# 流式访问

stream = model.stream("你是谁？")
print(type(stream))

for chunk in stream:
    print(chunk,end="",flush=True)
