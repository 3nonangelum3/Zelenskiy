#var-list
influence = 0
people = 0
money = 0
army = 0
params = {}
def gameInit():
    language = getLanguage()
    global influence
    global people
    global money
    global army
    influence = 50
    people = 50
    money = 50
    army = 50
    if language == "English":
        params["influence"] = influence
        params[]
    pass


def getLanguage() -> str:
    """
    Asks user to input a language of an interface until valid language will be inputted
    """

    language = input("What language do you prefer?\n"
                     "Какой язык Вы предпочитаете?\n"
                     "Якій мові Ви надаєте перевагу?\n"
                     ">>> ")
    while language == "" or ["English", "Русский язык", "Українська мова"].index(language) is None:
        language = input("What language do you prefer?\n"
                         "Какой язык Вы предпочитаете?\n"
                         "Якій мові Ви надаєте перевагу?\n"
                         ">>> ")
    return language


def gameStart():
