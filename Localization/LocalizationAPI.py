from Localization import LocalizationData
from Localization import LocalizationLanguages


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


def getLanguageIndex(language: str) -> int | None:
    """
    Searches for language in a language list and returns it`s index.
    :param language: language of the interface
    :return: Index of the given language in the language list
    """
    try:
        return LocalizationLanguages.languages.index(language)
    except ValueError:
        return None


def localise(language: str, varName: str) -> str | None:
    """
    Searches for the value of given variable name in the list on given language
    :param language: language of the interface
    :param varName: variable name which value is needed
    :return: given variable`s value in given language
    """
    if language in LocalizationLanguages.languages:
        if varName in LocalizationData.varList:
            return LocalizationData.varList[varName][getLanguageIndex(language) or 0] or 0
        else:
            return None
    else:
        return None


def unlocalize(language: str, value: str) -> str | None:
    if language in LocalizationLanguages.languages:
        searchDict = LocalizationData.valueList[getLanguageIndex(language)] or None
        if value in list(searchDict.keys()):
            return str(searchDict[value])
        else:
            return None
    else:
        return None
