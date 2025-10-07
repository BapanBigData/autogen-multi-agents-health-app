from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from src.agents.agents import (
    planning_agent,
    health_centers_agent,
    medication_agent,
    air_quality_checker_agent,
)
from src.utils.clients import model_client
from src.utils.prompts import SELECTOR_PROMPT


class RoleAwareExactTextTermination(TextMentionTermination):
    def __init__(self, text: str = "TERMINATE", role_name: str = "PlanningAgent"):
        super().__init__(text)
        self.role_name = role_name
        self.text = text

    async def __call__(self, state):
        # Sometimes state is just a list of messages
        # Sometimes it's a tuple (messages, extra_info)
        messages = None
        if isinstance(state, tuple) and state:
            # assume first element is the message list
            messages = state[0]
        else:
            messages = state

        if not messages:
            return False, None

        last_msg = messages[-1]
        content = getattr(last_msg, "content", "") or ""
        source = getattr(last_msg, "source", None)

        if source == self.role_name and content.strip() == self.text:
            self._terminated = True
            return True, f"{self.role_name} ended the chat with '{self.text}'"

        return False, None




text_mention_termination = TextMentionTermination("TERMINATE")
max_messages_termination = MaxMessageTermination(max_messages=20)
termination = text_mention_termination | max_messages_termination

team = SelectorGroupChat(
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
)
