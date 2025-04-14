from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from Agent.models.GraphState import AgentState
from langchain_core.messages import AnyMessage, AIMessage, HumanMessage
from Agent.nodes.nodes import AllNodes
from Agent.utils.display_graph import display_graph
from langgraph.prebuilt import tool_node, tools_condition, tool_validator, ToolNode
from Agent.tools.Tools import ToolList
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from Agent.speech_and_audios import speech_main
from Agent.models.Response_Request import ConfigRequest, ResponseConfigs


def get_graph():
    memory = MemorySaver()
    try:
        builder = StateGraph(AgentState)

        # Importiohnng Ndoes
        builder.add_node("assistant", AllNodes["assistant"])
        builder.add_node("DetectLanguage", AllNodes["DetectLanguage"])
        builder.add_node("tools", ToolNode(ToolList))
        builder.add_node("IsGoalCompleted", AllNodes["IsGoalCompleted"])

        # Adding edges
        builder.add_edge(START, "DetectLanguage")
        builder.add_edge("DetectLanguage", "assistant")
        builder.add_conditional_edges(
            "assistant",
            tools_condition,
            path_map={
                "tools": "tools",
                "assistant": "assistant"
            }
        )
        builder.add_edge("tools", "assistant")
        builder.add_conditional_edges("IsGoalCompleted", AllNodes["assistant"],  path_map={END, "assistant"})

        # Compilin Graph
        graph = builder.compile(checkpointer=memory)
        display_graph(graph)
        return graph
    except Exception as e:
        print(f"Error in graph creation: {e}")
        graph = None


# g = get_graph()
# messges = [HumanMessage(
#     content="i wnat to talk with this German person about getrting apples in very cheap price")]

# config = {"configurable": {"thread_id": "12"}}
# res = g.invoke({"messages": messges,
#                 "goal": "I want to talk with this German person about getting apples in very cheap price",
#                 "UserLang": "en",
#                 "OtherPersonLang": "de",
#                 "Plan": None,
#                 "invoked_by": "User"}, config=config)


def invoke_graph(user_id: str,
                 conversion_id: str,
                 filename: str,
                 graph) -> (str, bytes):
    text_res = speech_main.get_transcription(filename)
    if text_res is None:
        raise ValueError("Error in Transcription")
        return None, None
    else:
        try:
            g = graph
            messges = [HumanMessage(
                content=text_res)]
            config = {"configurable": {"thread_id": conversion_id}}
       g     res = g.invoke({"messages": messges,
                            "goal": text_res,
                            "UserLang": "en",
                            "OtherPersonLang": "de",
                            "Plan": None,
                            "invoked_by": user_id}, config=config)
            return res
        except Exception as e:
            print(f"Error in graph invocation: {e}")