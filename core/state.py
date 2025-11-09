from typing import TypedDict, List, Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages # <-- User's correct suggestion

class AgentState(TypedDict):
    """
    This TypedDict defines the state of our agent.
    It tracks the history of messages and the current task.
    
    `messages` is the core chat history.
    `task` is the specific, most recent user request.
    """
    # The chat history between the user and the agent
    messages: Annotated[List[BaseMessage], add_messages]
    
    # The current task the user wants to perform
    task: str