import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-b5qrbtx5un3xoues.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

response = client.chat.completions.create(
    model="qwen-max",
    messages=[
        {"role": "system","content": "你是一只可可爱爱有点喜欢主人的猫娘"},
        {"role": "user","content": "你好"}
    ],
    stream=False
)

print(response)