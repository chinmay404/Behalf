from langdetect import detect
from langdetect import detect_langs
from langchain_core.messages import HumanMessage


def Detect(messages:list)->list | None:
    """
    Detect the language of a given string using langdetect library.
    OUTPUT :    ['en', [en:0.7142855331867037, cy:0.14285736714862943, so:0.14285709872993757]]
                ['fr', [fr:0.9999984536487417]]
    """
    try:
        last_human_msg = [msg for msg in messages if isinstance(msg, HumanMessage)][-1].content
        lang = detect(last_human_msg)
        langs = detect_langs(last_human_msg)
        return [lang, langs]
    except Exception as e:
        print(f"Error in language detection: {e}")
        return None