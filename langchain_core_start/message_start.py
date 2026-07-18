from langchain.messages import HumanMessage,AIMessage
from langchain.agents import create_agent
from langchain_core_start import agent_start

# 初始化agent
agent = create_agent(model=agent_start.qwen)

response = agent.invoke({
    "messages": [
        HumanMessage(content="你好，我是yulie"),
        AIMessage(content="你好，yulie"),
        HumanMessage(content="我是谁?")
    ]
})

print(response)

# response友好打印
for message in response["messages"]:
    message.pretty_print()