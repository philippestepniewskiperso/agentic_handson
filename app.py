import chainlit as cl
from pydantic_ai.messages import ModelMessage
from dotenv import load_dotenv
from travel.domain.agent import agent

load_dotenv()

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])


@cl.on_message
async def main(message: cl.Message):
    history: list[ModelMessage] = cl.user_session.get("history")

    response = await cl.Message(content="").send()
    async with agent.run_stream(message.content, message_history=history) as result:
        if agent.output_type is None or agent.output_type is str:
            async for chunk in result.stream_text(delta=True):
                await response.stream_token(chunk)
        else:
            data = await result.get_output()
            await response.stream_token(str(data))
    await response.update()

    cl.user_session.set("history", result.all_messages())
