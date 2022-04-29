import multiprocessing as multi
import time
def process1(a):
    while True:
        a.put(0)
        time.sleep(1)
        a.put(1)
        time.sleep(1)
        a.put(2)
        time.sleep(1)
        a.put(3)
        time.sleep(1)
        a.put(4)
        time.sleep(1)
def process2(c, d):
    a = c.get()
    b = d.get()
    while True:
        if(c.empty() != True):
            a = c.get()
        if(d.empty() != True):
            b = d.get()
        while a == 0 and b == 0:
            print ("forward")
            if(c.empty() != True):
                a = c.get()
            if(d.empty() != True):
                b = d.get()
            if(b != 0 and a == 0):
                continue
            else:
                break
        while a == 1 and b == 0:
            print ("backward")
            if(c.empty() != True):
                a = c.get()
            if(d.empty() != True):
                b = d.get()
            if(b != 0 and a == 1):
                continue
            else:
                break
        while a == 2 and b == 0:
            print ("left")
            if(c.empty() != True):
                a = c.get()
            if(d.empty() != True):
                b = d.get()
            if(b != 0 and a == 2):
                continue
            else:
                break
        while a == 3 and b == 0:
            print ("right")
            if(c.empty() != True):
                a = c.get()
            if(d.empty() != True):
                b = d.get()
            if(b != 0 and a == 3):
                continue
            else:
                break
        while a == 4 or b == 1:
            print ("stop")
            if(c.empty() != True):
                a = c.get()
            if(d.empty() != True):
                b = d.get()
            if(a != 4 and b != 1):
                break
def process3(b):
    while True:
        b.put(0)
        time.sleep(2)
        b.put(1)
        time.sleep(2)
if __name__ == '__main__':
    a = multi.Queue()
    b = multi.Queue()
    a.put(0)
    b.put(0)
    process1 = multi.Process(target=process1, args=(a,))
    process2 = multi.Process(target=process2, args=(a, b,))
    process3 = multi.Process(target=process3, args=(b,))
    process1.start()
    process2.start()
    process3.start()