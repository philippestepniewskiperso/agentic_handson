# Hands-on Pydantic AI

## Setup

```bash
uv sync
```

Créer un fichier `.env` :

```
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_DEFAULT_REGION=eu-west-1
```

## Lancer l'app

```bash
chainlit run app.py
```

## Structure

```
travel/
├── domain/
│   ├── models.py          # Modèles Pydantic (TravelRequest, TravelAdvice)
│   └── agent.py           # Ton agent pydantic-ai
└── infrastructure/
    └── weather_client.py  # Client open-meteo
```

## Progression

### Étape 1 — Structured Output

Créer un `Agent` qui extrait depuis du texte un objet `TravelRequest` structuré.

Concepts : `Agent`, `result_type`, `BedrockConverseModel`

```python
from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel
from travel.domain.models import TravelRequest

agent = Agent(
    model=BedrockConverseModel("eu.anthropic.claude-sonnet-4-5-20250929-v1:0"),
    result_type=TravelRequest,
)
```

### Étape 2 — Tools

Ajouter un outil à l'agent pour récupérer la météo via `weather_client.fetch_weather`.

Concepts : `@agent.tool`, `RunContext`

```python
@agent.tool
async def get_weather(ctx: RunContext[None], city: str) -> list:
    return fetch_weather(city)
```

### Étape 3 — System Prompt & Multi-turn

Ajouter un `system_prompt` pour que l'agent pose des questions si des informations manquantes (ville, dates, activité).

Concepts : `system_prompt`, `message_history`

### Étape 4 — Multi-agent

Créer un agent orchestrateur qui délègue à deux sous-agents : un pour l'extraction, un pour les conseils.

Concepts : `agent.run()` depuis un tool, handoff entre agents
