from langdetect import detect
from langdetect import detect_langs


def Detect(Text:str)->list | None:
    """
    Detect the language of a given string using langdetect library.
    OUTPUT :    ['en', [en:0.7142855331867037, cy:0.14285736714862943, so:0.14285709872993757]]
                ['fr', [fr:0.9999984536487417]]
    """
    try:
        lang = detect(Text)
        langs = detect_langs(Text)
        return [lang, langs]
    except Exception as e:
        print(f"Error in language detection: {e}")
        return None