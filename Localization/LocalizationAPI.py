import Localization.LocalizationData


def getLanguage() -> str:
    """
    Asks user to input a language of an interface until valid language will be inputted
    :return: Language inputted by user
    """
    language = ""
    while language == "":
        language = input("What language do you prefer?\n"
                         "Какой язык Вы предпочитаете?\n"
                         "Якій мові Ви надаєте перевагу?\n"
                         "English, Русский язык, Українська мова\n"
                         ">>> ")
        try:
            ["English", "Русский язык", "Українська мова"].index(language)
        except ValueError:
            language = ""
    return language


def getIndex(language: str):
    pass


def Localise(language: str, varName: str):
    if language in Localization