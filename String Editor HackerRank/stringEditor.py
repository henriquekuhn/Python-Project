import re

class stringEditor:
    def __init__(self, string):
        self.string = string

    def stringManipulation(self):
        string_list = self.string.split()
        string_list2 = re.split(r'[!,\s]+', self.string)
        print(string_list)
        print(string_list2)

if __name__ ==  "__main__":
    
    #typedString = "Teste de como é dividida a string, lista!comando"
    typedString = input("Type a text: ")
    text1 = stringEditor(typedString)

    text1.stringManipulation()