# Gioele Amendola
# 26/06/2024

from pathlib import Path
from time import *

print("\nFile Manager:\n")

class FileManager:

    def __init__(self, filename: str, mode: str) -> None:
        self.filename: str = str(Path(__file__).parent.resolve())+"\\"+filename
        self.mode: str = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            print("Caught an exception")
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Traceback: {traceback}")
        else:
            self.file.close()

def filemanager(func) -> None:
    def wrapper(*args):
        print("Opening file")
        func(*args)
        print("File closed\n")
    return wrapper

@filemanager
def fileopen(filename: str, mode: str) -> None:
    with FileManager(filename, mode) as f:
        f.write("HAWK TUAH!")
        f.close()

fileopen("example.txt","w")

print("Time manager:\n")

class Timer:

    def __init__(self) -> None:
        self.count: int = 0
    
    def __enter__(self) -> None:
        self.count = time()
    
    def __exit__(self, exc_type, exc_val, traceback) -> float:
        if exc_type is not None:
            print("Caught an exception")
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Traceback: {traceback}")
        else:
            print(f"time elapsed: {time() - self.count:.5f}") 

def timer(func):
    def wrapper(sec):
        print("Initiating function")
        func(sec)
        print("End of function\n")
    return wrapper

@timer
def checkTime(sec: int):
    with Timer():
        sleep(sec)

checkTime(2)


