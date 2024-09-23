import os

DIRECTORY_IN = os.getcwd() + "/Automating Mail Recipients/Input"
DIRECTORY_OUT = os.getcwd() + "/Automating Mail Recipients/Output"
os.chdir(DIRECTORY_IN)

class recipient_mail:

    def __init__(self):
        self.name_list = []
        self.common_letter = []

    # Use the class variable directly, without 'self.'
    def get_recipients(self):
        with open("names.txt") as file:
            for line in file:
                self.name_list.append(line.strip())
        print(self.name_list)


    def get_common_letter(self):
        with open("common_letter.txt") as file:
            self.common_letter = file.read()
            print(self.common_letter)


    def update_mail(self):
        os.chdir(DIRECTORY_OUT)
        
        for name in self.name_list:
            self.new_letter = self.common_letter.replace("Someone", name)
            print(f"{self.new_letter}")
            with open(f"letter_for_{name}.txt", "w") as file:
                file.write(self.new_letter)
                
            
                

write_mail = recipient_mail()
write_mail.get_recipients()
write_mail.get_common_letter()
write_mail.update_mail()
