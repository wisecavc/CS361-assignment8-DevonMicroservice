import time

def main():
    res = None
    while True:
        with open("cmd.txt", "r") as file:
            res = file.read()
        time.sleep(0.5)
        # save request, save games
        if res == "1":
            with open("action.txt", "r") as file:
                lines = file.readlines()
                with open("games.txt", "w") as games:
                    for line in lines:
                        games.write(line)
            print("Action 1 complete")
            with open("cmd.txt", "w") as file:
                res = file.write("-1")
        # save request, save progress
        elif res == "2":
            with open("action.txt", "r") as file:
                lines = file.readlines()
                with open("progress.txt", "w") as progress:
                    for line in lines:
                        progress.write(line)
            print("Action 2 complete")
            with open("cmd.txt", "w") as file:
                res = file.write("-1")
        # load request, load games
        elif res == "3":
            with open("games.txt", "r") as file:
                lines = file.readlines()
                with open("action.txt", "w") as action:
                    for line in lines:
                        action.write(line)
            print("Action 3 complete")
            with open("cmd.txt", "w") as file:
                res = file.write("-2")
        # load request, load progress
        elif res == "4":
            with open("progress.txt", "r") as file:
                lines = file.readlines()
                with open("action.txt", "w") as action:
                    for line in lines:
                        action.write(line)
            print("Action 4 complete")
            with open("cmd.txt", "w") as file:
                res = file.write("-3")

if __name__ == "__main__":
    main()