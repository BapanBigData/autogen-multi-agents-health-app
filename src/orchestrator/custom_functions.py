from autogen_agentchat.messages import BaseAgentEvent, BaseChatMessage
from typing import Sequence
from src.agents.agents import planning_agent


def selector_func(messages: Sequence[BaseAgentEvent | BaseChatMessage]) -> str | None:
    if messages[-1].source != planning_agent.name:
        return planning_agent.name

    return None
