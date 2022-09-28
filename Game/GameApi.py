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
        load = unlocalize(language, load)
        if load:
            try:
                if load == "False":
                    return False
                elif load == "True":
                    return True
                else:
                    return None
            except TypeError:
                load = ""


def getDataCode(code: str):
    return {}


def gameInit():
    """
    initialize all vaiables and lists before starting a game
    :return:
    """
    global language
    language = getLanguage()
    dataLoaded = False
    dataList = {}
    loading = loadGame()
    if loading:
        code = input(f"{localise(language, 'getCode')}\n>>> ")
        if unlocalize(language, code) == "Stop":
            print("Loading saved game stopped")
        else:
            dataList = getDataCode(code)
            dataLoaded = True
    global params, currentOfferIndex, maxOfferInder, daysAlive
    if dataLoaded:
        params["influence"] = dataList["influence"]
        params["people"] = dataList["people"]
        params["money"] = dataList["money"]
        params["army"] = dataList["army"]
        maxOfferIndex = 0
        currentOfferIndex = dataList["currentOfferIndex"]
        daysAlive = dataList["daysAlive"]
    else:
        params["influence"] = 50
        params["people"] = 50
        params["money"] = 50
        params["army"] = 50
        maxOfferIndex = 0
        currentOfferIndex = 0
        daysAlive = 0


def gameStart():
    pass
