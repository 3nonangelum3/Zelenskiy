import Localization.LocalizationAPI

# var-list
params = {}
# will be used to decide how much cards to use
currentOfferIndex = 10
maxOfferInder = 0
# aka score
daysAlive = 0
language: str = ""


# functions
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

    global params, currentOfferIndex, maxOfferInder, daysAlive
    params["influence"] = 50
    params["people"] = 50
    params["money"] = 50
    params["army"] = 50
    maxOfferIndex = 0
    currentOfferIndex = 10
    daysAlive = 0


def gameStart():
    pass
