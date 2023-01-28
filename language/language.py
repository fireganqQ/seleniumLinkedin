# by https://github.com/fireganqQ #

from json import loads, dump

class language:
    '''
        language class
    '''
    def configLanguageRead():
        '''
            Reading config file and converting to json format
        '''
        return loads(open("./language/config.file", "r").read())

    def get(name):
        '''
            Getting the text by reading the language file
        '''
        file = loads(open(f'./language/{language.configLanguageRead().get("language")}.lang', "r", encoding="utf-8").read())
        return file.get(name)
    
    def set(code):
        '''
            change language options
        '''
        a = open('./language/config.file', "r")
        a_ = loads(a.read())
        a.close()

        a_['language'] = code

        with open('./language/config.file', "w") as w:
            dump(a_, w)