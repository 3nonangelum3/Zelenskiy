import random

import Game.Offers
import Localization.LocalizationAPI
from Localization.LocalizationAPI import localise, unlocalize, getLanguage

# var-list
params = {}
# will be used to decide how much cards to use
currentOfferMaxIndex = 10
maxOfferInder = 0
# aka score
daysAlive = 0
language: str = ""
# system vars
loadDeclined = False
loadSuccess = False
gameQuit = False
saveGame = False


# functions
def loadGame() -> bool | None:
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
                global loadDeclined
                if load == "True":
                    loadDeclined = False
                    return True
                elif load == "False":

                    loadDeclined = True
                    return False
                else:
                    load = ""
            except TypeError:
                load = ""


def nonValidCode():
    """
    Initialises a proses of non-valid code report to user
    """
    print(localise(language, "invalidCode"))
    global loadSuccess
    loadSuccess = False


def getDataFromCode(code: str) -> dict | None:
    """
    Decodes given code. If one part of the code is undecipherable returns null
    :param code: String that contains coded params
    :return: A dictionary filled with parameters found in code
    """
    encoded = {}
    if 10 < len(code) < 15:
        encodedCode = ""
        for i in code:
            encodedCode += chr(ord(i) - 15)
        langCode = encodedCode[0] + encodedCode[1]
        if langCode == 'en':
            encoded["language"] = "English"
        elif langCode == 'ru':
            encoded["language"] = "Русский язык"
        elif langCode == "uk":
            encoded["language"] = "Українська мова"
        else:
            nonValidCode()
            return None
        days = ""
        for i in range(10, len(encodedCode)):
            days += encodedCode[i]
        try:
            encoded["influence"] = int(encodedCode[2] + encodedCode[3])
            encoded["people"] = int(encodedCode[2] + encodedCode[3])
            encoded["money"] = int(encodedCode[4] + encodedCode[5])
            encoded["army"] = int(encodedCode[6] + encodedCode[7])
            encoded["currentOfferMaxIndex"] = int(encodedCode[8] + encodedCode[9])
            encoded["daysAlive"] = int(days)
        except TypeError:
            nonValidCode()
            return None
        return encoded
    else:
        nonValidCode()
        return None


def gameInit():
    """
    initialize all vaiables and lists before starting a game
    :return:
    """
    global language, loadSuccess, loadDeclined
    language = getLanguage()
    dataList = {}
    while not loadSuccess and not loadDeclined:
        if loadGame():
            code = input(f"{localise(language, 'getCode')}\n\n>>> ")
            if unlocalize(language, code) == "Stop":
                print("Loading saved game stopped")
            else:
                dataList = getDataFromCode(code)
    global params, currentOfferMaxIndex, maxOfferInder, daysAlive
    if loadSuccess:
        language = dataList["language"]
        params["influence"] = dataList["influence"]
        params["people"] = dataList["people"]
        params["money"] = dataList["money"]
        params["army"] = dataList["army"]
        maxOfferIndex = 0
        currentOfferMaxIndex = dataList["currentOfferMaxIndex"]
        daysAlive = dataList["daysAlive"]
    else:
        params["influence"] = 50
        params["people"] = 50
        params["money"] = 50
        params["army"] = 50
        maxOfferIndex = 0
        currentOfferMaxIndex = 0
        daysAlive = 0


def listActions():
    print(Localization.LocalizationAPI.localise(language, "commandsList"))


def codeCreator() -> str:
    code = ""
    if language == "English":
        code += "en"
    elif language == "Русский язык":
        code += "ru"
    elif language == "Українська мова":
        code += "uk"
    code += params["influence"]
    code += params["army"]
    code += params["money"]
    code += params["people"]
    code += str(currentOfferMaxIndex)
    code += str(daysAlive)
    result = ""
    for i in code:
        result += chr(ord(i) + 15)
    return result


def gameStart():
    print(localise(language, "gameUI"))
    startGame = ""
    while startGame == "":
        startGame = input(localise(language, "startGame") + "\n\n>>> ")
        startGame = unlocalize(language, startGame)
        if startGame == "False":
            global gameQuit
            gameQuit = False
        elif startGame == "True":
            print(localise(language, "gameStarts"))
        else:
            startGame = ""
    print("<---------------------------->")
    print(localise(language, "foreword"))
    global saveGame, gameQuit
    while True:
        currentOffer = Game.Offers.offers[random.randint(0, currentOfferMaxIndex)]
        print(currentOffer[Localization.LocalizationAPI.getLanguageIndex(language)])
        userInput = input(">>> ")
        while userInput != "accept" or userInput != "decline":
            if userInput == "list actions":
                listActions()
            elif userInput == "quit":
                gameQuit = False
            elif userInput == "save game":
                saveGame = True
            userInput = input(">>> ")
        if userInput == "accept":
            for i in params:
                params[i] += currentOffer[3][i]
                if params[i] <= 0:
                    gameQuit = True
                    saveGame = False
        elif userInput == "decline":
            for i in params:
                params[i] += currentOffer[4][i]
                if params[i] <= 0:
                    gameQuit = True
                    saveGame = False
        elif saveGame:
            print("Saving game\n"
                  "This is a token that you would need to continue playing your game later:\n"
                  f"{codeCreator()}")
            gameQuit = True
        elif gameQuit:
            break
    print("Thanks for playing!!!")
