from typing import TypedDict, List

class AgentState(TypedDict):
    # MESSAGES : For Converesation History
    # GOAL :  For Converastion Goal 
    # PLAN : The Plan To Achive That Goal 
    messages: List[dict]
    goal: str
    Plan : List
    UserLang : str | None
    OtherPersonLang : str | None
