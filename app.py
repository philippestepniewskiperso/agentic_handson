import asyncio

import chainlit as cl
from dotenv import load_dotenv

from travel.domain.agent import main_agent

load_dotenv()


@cl.on_message
async def main(message: cl.Message):
    result = await asyncio.to_thread(main_agent.run_sync, message.content)
    await cl.Message(content=result.output).send()
