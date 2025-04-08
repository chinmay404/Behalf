from crewai import LLM
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()


def get_google_llm():
    google_llm = LLM(
        model='gemini/gemini-1.5-flash',
        api_key=os.getenv("GOOGLE_API_KEY")
    )
    return google_llm


def get_local_llm(model_name="ollama/deepseek-r1:7b"):
    local_llm = LLM(
        model=model_name,
        base_url="http://localhost:11434",
        temperature=1.0
    )
    return local_llm


def get_groq_llm():
    groq_llm = ChatGroq(
        model="deepseek-r1-distill-llama-70b",
        api_key=os.getenv("groq_api_key")
    )
    return groq_llm
