from os import system

class Id_Validation:
    def __init__(self, id):
        self.__id = id
        self.__eval = True

    def __str__(self):
        try:
            if self.Id_Evaliuation():
                return f"{int(self.__id)} is valid"

            else:
                return f"{int(self.__id)} isn't valid .........."
        except ValueError:
            return f"{self.__id} not respond .........."

    @property
    def ID(self):
        return self.__id
    
    @ID.setter
    def ID(self, code):
        self.__id = code

    @property
    def EVAL(self):
        return self.__eval
    
    @EVAL.setter
    def EVAL(self, evaluation):
        self.__eval = evaluation

    def Id_Evaliuation(self):
        newID = 0
        if 8 <= len(str(self.__id)) <= 10 :
            newID = '0'*(10-len(str(self.__id)))+str(self.__id)
            check = 0
            lastNum = 0
            check = int(newID[0])*10+int(newID[1])*9+int(newID[2])*8+int(newID[3])*7+int(newID[4])*6+int(newID[5])*5+int(newID[6])*4+int(newID[7])*3+int(newID[8])*2
            
            if check % 11 >= 2:
                lastNum = 11-(check % 11)

            
            else:
                lastNum = check % 11

            if lastNum != int(newID[9]):
                self.__eval = False

        else:
            self.EVAL = False

        if self.__eval:
                return True
        else:
                return False

while True:
    checkID = input("enter your Id_Code number to check or 'done' to exit : ")
    match checkID:
        case 'done':
            system('cls')
            break

        case _:
            print(Id_Validation(checkID))
            input("press any key ..........")
            system('cls')