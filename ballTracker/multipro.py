import multiprocessing as multi
import time

def test1():
    while True:
        time.sleep(1)
        print ("hi")
def test2():
    time.sleep(.25)
    while True:
        time.sleep(1)
        print ("check")
def test3():
    time.sleep(.5)
    while True:
        time.sleep(1)
        print ("bye")
def main():
    hi = multi.Process(target=test1, args=())
    bye = multi.Process(target=test3, args=())
    check = multi.Process(target=test2, args=())
    hi.start()
    check.start()
    bye.start()
if __name__ == '__main__':
    main()