from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


load_dotenv()


def get_groq_llm():
    try:
        api_key = os.getenv("groq_api_key")
        if api_key:
            llm = ChatGroq(
                model="llama-3.3-70b-versatile",
                temperature=0.5,
                max_retries=4,
            )
            return llm
        else:
            print("failed To Read Groq API key.")
            return None
    except Exception as e:
        print(f"Error At get_groq_llm: {e}")
        return None


def get_deepseek():
    try:
        model = ChatOpenAI(
            model="deepseek-chat",
            api_key="sk-8237a6bdb61a48638e082942217a609a",
            base_url="https://api.deepseek.com",
            temperature=1.0
        )
    except Exception as e:
        print("Error in DeepSeek Coder ")
        return None
