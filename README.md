# Microservice for Devon's program

## Communication Contract

### Requesting data from the microservice

The microservice reads a numerical code from cmd.txt.

The numerical codes are hard-coded into the program, and currently only 4 codes corresponding to requested functionalities are implemented. The codes are the numbers 1-4. The numerical code's purpose is to give the microservice instructions related to which .txt file it should copy data from, and which .txt file the copied data should be written in.

#### Numerical codes and their functions:

1: copies data from action.txt to games.txt
2: copies data from action.txt to progress.txt
3: copies data from games.txt to action.txt
4: copies data from progress.txt to action.txt

#### Calling the microservice

This microservice is designed to be constantly running in the background, so it only needs to be called once. The microservice will scan the contents of cmd.txt every half second, any codes placed in cmd.txt will be processed automatically by the microservice at the start of the next scan. It is recommended that the microService.py be called as a subprocess at the start of the main program, as follows:

```
import subprocess
import time

command = ["python", "microService.py"]
process = subprocess.Popen(command)
```
### Recieving data from the microservice

The microservice's output destination varies depending on the numerical request code which it is passed. To recieve data from the microservice, access the .txt file correlating to the numerical code written in cmd.txt that activated the microservice.

### UML Diagram

![UML diagram for Microservice, assignment 8](<CS361 UML for assignment 8.jpeg>)