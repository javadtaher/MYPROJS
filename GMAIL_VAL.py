from os import system
import re

class gmailWriting_Validation():
    def __init__(self, gmail):
        self.__gmail = gmail
        self.GL_Evaliuation()

    def __str__(self):
        if self.GL_Evaliuation():
            return f"{self.__gmail} is valid"

        else:
            return f"{self.__gmail} isn't valid .........."

    @property
    def GMAIL(self):
        return self.__gmail
    
    @GMAIL.setter
    def GMAIL(self, Gmail):
        self.__gmail = Gmail

    def GL_Evaliuation(self):
        strmatch = re.match(r'^[A-Za-z0-9][A-Za-z0-9\.\_]*\@[a-z]+\.[a-z]+', self.__gmail)
        if strmatch:
            strpart = str(self.__gmail).partition("@")
            if strpart[0][-1] != r'.':
                return True
            else:
                return False
        else:
            return False

while True:
    checkID = input("enter your 'Gmail' to check or 'done' to exit : ")
    match checkID:
        case 'done':
            system('cls')
            break

        case _:
            print(gmailWriting_Validation(checkID))
            input("press any key ..........")
            system('cls')
