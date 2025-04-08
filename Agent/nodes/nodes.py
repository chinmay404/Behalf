
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from Agent.models.GraphState import AgentState
from langchain_core.messages import AnyMessage , AIMessage, HumanMessage
from Agent.utils.LanguageDetector import Detect



def DetectLanguage(state: AgentState):
    new_message = state["messages"]
    result = Detect(new_message)
    if result != "en":
        return "ProcessUserInput"
    else: 
        return "ProcessOtherPersonInput"



def ProcessUserInput(state: AgentState):
    print("ProcessUserInput")


def ProcessOtherPersonInput(state: AgentState):
    print("ProcessOtherPersonInput")


def assistant(state: AgentState):
    # Process the assistant's response
    assistant_message = AIMessage(content="Assistant's response")
    state["messages"].append(assistant_message)
    return {"messages": state["messages"]}


def OtherPersonassistant(state: AgentState):
    # Process the assistant's response
    assistant_message = AIMessage(content="OtherPersonassistant's response")
    state["messages"].append(assistant_message)
    return {"messages": state["messages"]}



def IsGoalCompleted(state: AgentState):
    # Process the assistant's response
    assistant_message = AIMessage(content="OtherPersonassistant's response")
    state["messages"].append(assistant_message)
    return {"messages": state["messages"]}

AllNodes = {"DetectLanguage" : DetectLanguage , 
            "ProcessUserInput" : ProcessUserInput,
            "ProcessOtherPersonInput" : ProcessOtherPersonInput,
            "assistant": assistant,
            "OtherPersonassistant": OtherPersonassistant,
            "IsGoalCompleted": IsGoalCompleted}