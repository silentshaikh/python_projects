import time

def countdown(t):
    while t:
        countMin, countSec = divmod(t,60)
        setTimerContent = f"{countMin} mins , {countSec} secs"
        print(setTimerContent,end="\r")
        time.sleep(1)
        t -= 1
    print("Timer Completed !")


countdown(120)