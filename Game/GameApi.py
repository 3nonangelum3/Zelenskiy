import Localization.LocalizationAPI

#var-list
params = {}
maxOfferIndex = 10
daysAlive = 0
language:str = ""
languageIndex = {"English": 1,
                 "Русский язык": 2,
                 "Українська мова": 3}

#functions
def loadGame() -> bool:
    """
    Asks user if they want to load previous game
    :return: True if Yes and False if No
    """
    load = ""
    while load == "" or [].index(load) is None:
        load = input("Do you want to load your previous game?\n"
                 "Хотите загрузить свою предыдущую игру?\n"
                 "Бажаєте завантажити свою попередню гру?\n"
                 ">>> ")

def gameInit():
    """
    initialize all vaiables and lists before starting a game
    :return:
    """
    global language
    language = Localization.LocalizationAPI.getLanguage()

    global params, maxOfferIndex, daysAlive, language
    params["influence"] = 50
    params["people"] = 50
    params["money"] = 50
    params["army"] = 50
    maxOfferIndex = 10
    daysAlive = 0




def gameStart():
