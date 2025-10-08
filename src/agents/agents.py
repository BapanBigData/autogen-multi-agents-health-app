from autogen_agentchat.agents import AssistantAgent
from src.utils.clients import model_client
from src.utils.prompts import (
    PROMPT_PLANNING_AGENT,
    PROMPT_HEALTH_CENTERS_AGENT,
    PROMPT_MEDICATION_AGENT,
    PROMPT_AIR_QUALITY_CHECKER_AGENT,
    PROMPT_FINAL_RESPONSE_AGENT,
)
from .tools import health_centers_search_tool, medication_info_tool, air_quality_tool


planning_agent = AssistantAgent(
    name="PlanningAgent",
    description="An agent for planning tasks, this agent should be the first to engage when given a new task.",
    model_client=model_client,
    system_message=PROMPT_PLANNING_AGENT,
)

health_centers_agent = AssistantAgent(
    name="HealthCentersAgent",
    description="An agent for searching health centers.",
    tools=[health_centers_search_tool],
    model_client=model_client,
    system_message=PROMPT_HEALTH_CENTERS_AGENT,
)

medication_agent = AssistantAgent(
    name="MedicationAgent",
    description="An agent to provide medication info.",
    tools=[medication_info_tool],
    model_client=model_client,
    system_message=PROMPT_MEDICATION_AGENT,
)

air_quality_checker_agent = AssistantAgent(
    name="AirQualityCheckerAgent",
    description="An agent to provide air quality of a given ZIP code.",
    tools=[air_quality_tool],
    model_client=model_client,
    system_message=PROMPT_AIR_QUALITY_CHECKER_AGENT,
)

final_response_agent = AssistantAgent(
    name="FinalResponseAgent",
    description="An agent that compiles all outputs into a single HTML response.",
    tools=[],
    model_client=model_client,
    system_message=PROMPT_FINAL_RESPONSE_AGENT,
)
