from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from Agent.models.GraphState import AgentState
from langchain_core.messages import AnyMessage , AIMessage, HumanMessage
from Agent.nodes.nodes import AllNodes
from Agent.utils.display_graph import display_graph


from langgraph.prebuilt import ToolNode

builder = StateGraph(AgentState)

builder.add_node("DetectLanguage" , AllNodes["DetectLanguage"])
builder.add_node("ProcessUserInput" , AllNodes["ProcessUserInput"])
builder.add_node("ProcessOtherPersonInput" , AllNodes["ProcessOtherPersonInput"])
builder.add_node("Userassistant" , AllNodes["assistant"])
builder.add_node("OtherPersonassistant" , AllNodes["OtherPersonassistant"])
builder.add_node("IsGoalCompleted" , AllNodes["IsGoalCompleted"])


builder.add_conditional_edges("DetectLanguage", AllNodes["DetectLanguage"], path_map=["ProcessUserInput", "ProcessOtherPersonInput"])
builder.add_edge("ProcessUserInput", "Userassistant")
builder.add_edge("ProcessOtherPersonInput", "OtherPersonassistant")
builder.add_edge("Userassistant", "IsGoalCompleted")
builder.add_edge("OtherPersonassistant", "IsGoalCompleted")
builder.add_edge("IsGoalCompleted", END)
builder.add_edge(START, "DetectLanguage")



graph = builder.compile()
display_graph(graph)