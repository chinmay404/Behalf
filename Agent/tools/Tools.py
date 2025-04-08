from langchain_core.tools import tool



@tool
def get_user_input(user_input: str) -> str:
    """Get user input."""
    return user_input


@tool
def get_other_person_input(other_person_input: str) -> str:
    """Get other person input."""
    return other_person_input