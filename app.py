import chainlit as cl
from pydantic_ai.messages import ModelMessage

from travel.domain.agent import agent


@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])


@cl.on_message
async def main(message: cl.Message):
    history: list[ModelMessage] = cl.user_session.get("history")

    response = await cl.Message(content="").send()
    async with agent.run_stream(message.content, message_history=history) as result:
        async for chunk in result.stream_text(delta=True):
            await response.stream_token(chunk)
    await response.update()

    cl.user_session.set("history", result.all_messages())
