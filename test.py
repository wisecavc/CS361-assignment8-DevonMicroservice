import subprocess
import time

command = ["python", "microService.py"]
process = subprocess.Popen(command)

def file_test(cmd):
    '''Tests pairs of files to determine if their contents match.'''
    time.sleep(1.0)
    if cmd == 1:
        output_file = "games.txt"
        input_file = "action.txt"
    elif cmd == 2:
        output_file = "progress.txt"
        input_file = "action.txt"
    elif cmd == 3:
        output_file = "action.txt"
        input_file = "games.txt"
    elif cmd == 4:
        output_file = "action.txt"
        input_file = "progress.txt"
    print("\nChecking if " + output_file + " contains the same contents as " + input_file)
    with open (output_file, "r") as output_test:
        with open (input_file, "r") as input_test:
            op = output_test.read()
            ip = input_test.read()
            if op == ip:
                print("Contents of " + output_file + " and " + input_file + " match. Test successful.")
            else:
                print("Contents of " + output_file + " and " + input_file + " do not match. Test failed.")
            return

while True:
    print("""
        commands:
          1: action.txt -> games.txt
          2: action.txt -> progress.txt
          3: games.txt -> action.txt
          4: progress.txt -> action.txt
          """)
    prompt = input("Which command would you like to demo: ")
    # action -> games
    if prompt == '1':
        input1 = input("insert text to move from action.txt to games.txt: ")
        with open("action.txt", "w") as file:
            file.write(input1)
            print("Action 1 initiating...")
            with open("cmd.txt", "w") as file:
                file.write("1")
                code = 1
    # action -> progress
    elif prompt == '2':
        input2 = input("insert text to move from action.txt to progress.txt: ")
        with open("action.txt", "w") as file:
            file.write(input2)
            print("Action 2 initiating...")
            with open("cmd.txt", "w") as file:
                file.write("2")
                code = 2
    # games -> action
    elif prompt == '3':
        input3 = input("insert text to move from games.txt to action.txt: ")
        with open("games.txt", "w") as file:
            file.write(input3)
            print("Action 3 initiating...")
            with open("cmd.txt", "w") as file:
                file.write("3")
                code = 3
    # progress -> action
    elif prompt == '4':
        input4 = input("insert text to move from progress.txt to action.txt: ")
        with open("progress.txt", "w") as file:
            file.write(input4)
            print("Action 4 initiating...")
            with open("cmd.txt", "w") as file:
                file.write("4")
                code = 4
    else:
        print("Command not recognized. Input was not a number between 1 and 4.")
    file_test(code)
    