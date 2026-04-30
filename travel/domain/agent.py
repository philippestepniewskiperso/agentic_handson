from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel

model = BedrockConverseModel("eu.anthropic.claude-sonnet-4-5-20250929-v1:0")

agent = Agent(model=model)
