from autogen_agentchat.teams import SelectorGroupChat, RoundRobinGroupChat
from autogen_agentchat.agents import SocietyOfMindAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from src.agents.agents import (
    planning_agent,
    health_centers_agent,
    medication_agent,
    air_quality_checker_agent,
    final_response_agent,
)
from src.utils.clients import model_client
from src.utils.prompts import SELECTOR_PROMPT
from .custom_functions import selector_func

text_mention_termination = TextMentionTermination("TERMINATE")
max_messages_termination = MaxMessageTermination(max_messages=20)
termination = text_mention_termination | max_messages_termination

inner_team = SelectorGroupChat(
    participants=[
        planning_agent,
        health_centers_agent,
        medication_agent,
        air_quality_checker_agent,
    ],
    model_client=model_client,
    termination_condition=termination,
    selector_prompt=SELECTOR_PROMPT,
    allow_repeated_speaker=True,
    selector_func=selector_func,
)


society_of_mind_agent = SocietyOfMindAgent(
    "society_of_mind", team=inner_team, model_client=model_client
)

team = RoundRobinGroupChat([society_of_mind_agent, final_response_agent], max_turns=2)
