from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

from travel.domain.models import TravelPlan

model = BedrockConverseModel(
    "eu.anthropic.claude-sonnet-4-5-20250929-v1:0",
    provider=BedrockProvider(region_name="eu-west-1"),
)

agent = Agent(model=model,
              output_type = TravelPlan,
              system_prompt="Tu es un assistant de planification de voyage."
                            "Utilise toujours weathertool et location tool avant de produire le résultat final."
                            "Adapte tes suggestions à la météo prévue."

              )
