from Localization.LocalizationAPI import localise, unlocalize, getLanguage

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
    while load == "":
        load = input(f"{localise(language, 'gameLoad')}\n\n>>> ")



def gameInit():
    """
    initialize all vaiables and lists before starting a game
    :return:
    """
    global language
    language = getLanguage()

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
