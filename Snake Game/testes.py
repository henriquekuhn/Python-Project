import os

file_path = "score.txt"

print("Current Working Directory:", os.getcwd())

DIRECTORY = os.getcwd()+"/Snake Game"
os.chdir(DIRECTORY)
print("Current Working Directory:", os.getcwd())



if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")