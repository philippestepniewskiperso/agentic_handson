from pydantic_ai import Agent

from travel.domain.model import model
from travel.domain.models import TravelPlan, TravelResponse
from travel.tools.location import location_tool
from travel.tools.time_awareness import current_date
from travel.tools.weather import weather_tool

travel_agent = Agent(model=model,
                     output_type = TravelPlan,
                     system_prompt="Tu es un assistant de planification de voyage."
                            "Adapte tes suggestions à la météo prévue et explique tes choix. ",
                     tools = [weather_tool,location_tool, current_date]
                     )

prettifier_agent = Agent(model=model,
                         output_type=TravelResponse,
                         system_prompt="Tu es un agent spécialisé dans la présentation de planing de voyage. "
                                       "Tu formattes les Travel Plan en beau markdown à montrer à l'utilisateur.",
                         )

def my_travel_workflow(user_prompt:str)->TravelResponse:
    """
    Outil permettant de construire un travel plan à partir de la demande utilisateur
    :param user_prompt: la demande de voyage de l'utilisateur
    :return: le programme bien formaté
    """
    print("Calling travel_workflow now")
    travel_plan : TravelPlan = travel_agent.run_sync(user_prompt).output
    pretty_travel_plan : TravelResponse = prettifier_agent.run_sync(travel_plan.model_dump_json()).output
    return pretty_travel_plan

main_agent = Agent(model=model,
                   output_type=str,
                   system_prompt="Tu es un agent conversationnel. Réponds aux demandes de l'utilisateur. "
                                 "Si ce n'est pas sujet de voyage, recentre la conversation de l'utilisateur.",
                   tools = [my_travel_workflow])




