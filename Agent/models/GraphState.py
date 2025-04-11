from typing import TypedDict, List, Annotated
from operator import add




# class AgentState(TypedDict):
#     # MESSAGES : For Converesation History
#     # GOAL :  For Converastion Goal 
#     # PLAN : The Plan To Achive That Goal 
#     messages: List[dict]
#     goal: str
#     Plan : List
#     UserLang : str | None
#     OtherPersonLang : str | None


class AgentState(TypedDict):
    # MESSAGES : For Converesation History
    # GOAL :  For Converastion Goal 
    # PLAN : The Plan To Achive That Goal 
    messages: Annotated[List[dict], add]
    goal: str
    Plan : List | None
    UserLang : str | None
    OtherPersonLang : str | None
    invoked_by: str | None
