from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from langchain_core_start import agent_start

# 2.创建智能体
agent = create_agent(model=agent_start.qwen)

# 3.组织多模态消息
multimodal_message = HumanMessage(
    content=[
        {"type": "image",
         "url": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg"},
        {"type": "text", "text": "这些图描绘了什么内容？"}
    ])

# 4.调用Agent，发送多模态消息
for token, metadata in agent.stream({
    "messages": [multimodal_message]
}, stream_mode="messages"):
    if token.content:
        print(token.content, end="", flush=True)