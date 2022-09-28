def getLanguage() -> str:
    """
    Asks user to input a language of an interface until valid language will be inputted
    :return: Language inputted by user
    """
    languageInnerVar = ""
    while languageInnerVar == "" or ["English", "Русский язык", "Українська мова"].index(languageInnerVar) is None:
        languageInnerVar = input("What language do you prefer?\n"
                         "Какой язык Вы предпочитаете?\n"
                         "Якій мові Ви надаєте перевагу?\n"
                         "English, Русский язык, Українська мова\n"
                         ">>> ")
    return languageInnerVar


def Localise(Language: int, varName: str):
