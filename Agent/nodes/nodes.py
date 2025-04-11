
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from Agent.models.GraphState import AgentState
from langchain_core.messages import AnyMessage, AIMessage, HumanMessage
from Agent.utils.LanguageDetector import Detect
from langgraph.prebuilt import tool_node, tools_condition, tool_validator, ToolNode
from Agent.utils.get_llm import LLM
from Agent.tools.Tools import ToolList
from Agent.utils.get_prompt import get_sys_prompt


llm = LLM.get_Gemini()
llm_with_tools = llm.bind_tools(ToolList)


# class AgentState(TypedDict):
#     # MESSAGES : For Converesation History
#     # GOAL :  For Converastion Goal
#     # PLAN : The Plan To Achive That Goal
#     messages: List[dict]
#     goal: str
#     Plan : List
#     UserLang : str | None
#     OtherPersonLang : str | None


def DetectLanguage(state: AgentState):
    new_message = state["messages"]
    # detected_lang = Detect(new_message)
    detected_lang = "de"
    user_lang = "en"  # TODO: add Here Read Language Form User DB
    return {"UserLang": user_lang, "OtherPersonLang": detected_lang[0], "invoked_by": "User" if detected_lang[0] == "en" else "OtherPerson"}


# def assistant(state: AgentState):
#     print("State: ", state)
#     # print(state["messages"])
#     # print(state["UserLang"],state["OtherPersonLang"],state["invoked_by"], state["goal"])
#     llm_invoked = llm_with_tools.invoke([get_sys_prompt(user_language=state["UserLang"],
#                                                         other_person_language=state["OtherPersonLang"],
#                                                         invoked_by=state["invoked_by"],
#                                                         goal=state["goal"])] + state["messages"])
#     return {"messages": state["messages"] + [llm_invoked]}


def assistant(state: AgentState) -> AgentState:
    # Invoke LLM with tools
    llm_invoked = llm_with_tools.invoke([get_sys_prompt(
        user_language=state["UserLang"],
        other_person_language=state["OtherPersonLang"],
        invoked_by=state["invoked_by"],
        goal=state["goal"]
    )] + state["messages"])

    # Return updated state with new message
    return {
        "messages": [*state["messages"], llm_invoked],
        "goal": state["goal"],
        "Plan": state["Plan"],
        "UserLang": state["UserLang"],
        "OtherPersonLang": state["OtherPersonLang"]
    }


def IsGoalCompleted(state: AgentState):
    return True


AllNodes = {"DetectLanguage": DetectLanguage,
            "assistant": assistant,
            "IsGoalCompleted": IsGoalCompleted}
