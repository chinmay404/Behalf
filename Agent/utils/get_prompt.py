from Agent.utils.load_prompt import load_prompt_from_yaml
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate


def get_sys_prompt(user_language: str, other_person_language: str, invoked_by: str, goal: str):
    """Get system prompt from YAML file"""
    try:
        sys_prompt = load_prompt_from_yaml("ASSISTANT_SYSTEM_PROMPT")  
        prompt_template = PromptTemplate.from_template(sys_prompt)  
        final_prompt = prompt_template.format(
            user_language=user_language,
            other_person_language=other_person_language,
            invoked_by=invoked_by,
            goal=goal
        )
        return final_prompt
    except Exception as e:
        print(f"Error loading system prompt: {e}")
        return None

