import multiprocessing
import time

def sleep():

    print(f"Sono nella funzione")
    time.sleep(1)
    print(f"Sto uscendo dalla funzione")


if __name__ == "__main__":

    tic: float = time.time()

    sleep()
    sleep()

    toc: float = time.time()
    time_elapsed: float = toc - tic

    print(f"{time_elapsed=}")