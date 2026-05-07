import os

from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

model = BedrockConverseModel(
    "eu.anthropic.claude-sonnet-4-5-20250929-v1:0",
    provider=BedrockProvider(region_name=os.environ.get("AWS_DEFAULT_REGION")),
)
