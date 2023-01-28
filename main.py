# by https://github.com/fireganqQ #

import time
from colorama import Fore
from utils import (misc, handler)
from language import language

# title #
misc.headBar()

# language change menu #
def languageSettings():
    while 1:
        a = input(Fore.GREEN+ language.get("lang_set"))
        if "1" in list(a):
            language.set("tr")
            misc.clear()
            break

        elif "2" in list(a):
            language.set("en")
            misc.clear()
            break
        else:
            misc.clear()


# main function #
def main():
    # language selection #
    if language.configLanguageRead().get("language") == "default":
        languageSettings()


    while 1:
        b = input(Fore.GREEN+language.get('continue')+Fore.RESET)

        # Sign out #
        if "q" in list(b.lower()):
            break

        # Change language #
        elif "2" in list(b):
            languageSettings()

        elif "3" in list(b):
            a = input(Fore.GREEN+ language.get("url_entry")+Fore.RESET) # profile link entry

            b = handler()
            pageText = b.getPage(a)
            if pageText==True:
                misc.infoMagenta(language.get('name'), b.__name__()[0])
                misc.infoMagenta(language.get('lastname'), b.__name__()[1])
                misc.infoMagenta(language.get('about'), b.__about__())
                b.quit()
            else:
                b.quit()
                misc.error(pageText)


if __name__ == '__main__':
    main()