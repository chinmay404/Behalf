from crewai.tools import BaseTool
import dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool
from speech_and_audios.tts import text_to_speech_eleven_labs, simple_pyttsx3_tts
from speech_and_audios.tts import simple_pyttsx3_tts as tts
from speech_and_audios.speech_main import record_and_transcribe
from get_llm import get_google_llm
from info import get_info


def start_communication():
    try:
        user_input = input("Enter the user input : ")
        extracted_info = get_info(user_input)
        situation = extracted_info.get("situation")
        opposite_party = extracted_info.get("opposite_party")
        goal_of_communication = extracted_info.get("goal_of_communication")
        expected_output = extracted_info.get("expected_output")
        lang = "German"
        try:
            result = start_crew(
                situation, opposite_party, goal_of_communication, expected_output, user_input, lang)
            return result
        except Exception as e:
            print(f"Error in start_crew or in crew : {e}")
            return False
    except Exception as e:
        print(e)
        return False


def take_ttd_input():
    listened = str(record_and_transcribe())
    return listened


def start_crew(situation, opposite_party, goal_of_communication, expected_output, user_input, lang):
    google_llm = get_google_llm()

    @tool("Take_User_Opinion")
    def TakeUserOpinion(argument: str) -> str:
        """Use This to ask on something Which is Really needed or any decision want from User."""
        # path = text_to_speech_eleven_labs(argument)
        # simple_pyttsx3_tts(argument)
        # print
        res = input(f"USERS INPUT : \n{argument} : \n")
        return res

    @tool("Listen_to_opposit_party")
    def Listen_to_opposit_party(argument: str) -> str:
        """Use This to ask anything you want to other party in their language"""
        # path = text_to_speech_eleven_labs(argument)
        # simple_pyttsx3_tts(argument)
        res = input(f"FOR OPP PARTY : \n{argument}\nPARTY INPUT : ")
        # res = take_ttd_input()
        return res

    @tool("tell_user_something")
    def tell_user_something(argument: str) -> str:
        """Use This to tell user about anything you want in English"""
        # text_to_speech_eleven_labs(argument)
        # simple_pyttsx3_tts(argument)
        res = input(f"FOR USER : \n{argument}\nUSER INPUT : ")
        # res = take_ttd_input()
        return res

    cummunication_agent = Agent(
        role='Communicator',
        goal=f"""Your purpose is to communicate on behalf of the user in the {situation} situation with the opposite party, {opposite_party}. You will talk to {opposite_party} in {lang} to achieve the goal: {goal_of_communication}.""",
        backstory="""You ARe a great Communicater you know how to commincate with diffrent people with diffrent language and achive the given goal """,
        verbose=True,
        allow_delegation=True,
        llm=google_llm,
        tools=[TakeUserOpinion, Listen_to_opposit_party, tell_user_something]
    )

    manager = Agent(
        role="Manager",
        goal="""Efficiently manage the crew and ensure task completion of the 
        ** Goal *** :  Talk Behlaf of user to {} for the {} in {} language to achive the goal of {}""".format(opposite_party, situation, lang, goal_of_communication),
        backstory="You're an experienced comminicator who had knowldege of how to do comminucation and get things donw for usser in best and effcinet way using.",
        allow_delegation=True,
        llm=google_llm,
        verbose=True
    )

    negociator = Agent(
        role="Negotiator",
        goal="""Your task is to negotiate effectively to achieve {goal_of_communication} in {lang} with {oppo_party}. Always act in the best interest of the user, ensuring a positive and beneficial outcome for them.""",
        backstory="""You are skilled in communication and negotiation, with a strong focus on understanding the other party's position while advocating for the user's needs""",
        verbose=True,
        allow_delegation=True,
        llm=google_llm,
        tools=[Listen_to_opposit_party, TakeUserOpinion, tell_user_something]
    )
    
    summuriser = Agent(
        role="summuriser",
        goal="""Summurises things and imortant details happened in communication.""",
        backstory="""You are good summuriser""",
        verbose=True,
        # allow_delegation=True,
        llm=google_llm,
        # tools=[Listen_to_opposit_party, TakeUserOpinion, tell_user_something]
    )

    task1 = Task(
        description=f"""Communicate on behalf of the user with {opposite_party}, asking for {situation} in {lang}.
            Complete the communication seamlessly while translating responses back to English for the user. 
            If additional clarification or input is required, use the tool 'TakeUserOpinion' to request the user's guidance in English.
            also tell the user what they said in English 
            Additionally, inform the user of all responses in English and allow them to provide further questions or instructions for the other party,
            if needed, via the 'TakeUserOpinion' tool.
            Also Ask USer Before telling about any decision or any important thing to other party""",
        agent=cummunication_agent,
        expected_output="I have talked with them ",
    )

    task2 = Task(
        description=f"""ASk For User if there any negociation needed if no then skip this task. if yes do the negociation with {opposite_party} in {lang}. if No Then stop""",
        agent=negociator,
        expected_output="I have asked user for negociation",
    )

    task3 = Task(
        description=f"""tell The all important details happend in communication and Explain Situation back to user in English and also user for anything else needed to ask to other party or stop the conversation""",
        agent=cummunication_agent,
        expected_output="Here is what they said to me : ",
    )

    # task4 = Task(
    #     description=f"""Ask user for anything else needed to ask to other party or stop the conversation""",
    #     agent=cummunication_agent,
    #     expected_output="Here is what they said to me : ",
    # )

    crew = Crew(
        agents=[cummunication_agent, negociator],
        tasks=[task1, task2, task3],
        verbose=1,
        manager_agent=manager,
        cache=True,
        process=Process.sequential,
        max_rpm=50
    )

    result = crew.kickoff()
    return result


start_communication()
