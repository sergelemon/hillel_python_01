from multiprocessing import Process, Pipe
from time import sleep
from os import getpid

def ponger(receiver, sender, response):
    while True:
        # receive a message
        msg = receiver.recv()
        # print it as f"Process{getpid()} got message: {msg}"
        print(f'Process{getpid()} got message: {msg}')
        # sleep before responding
        sleep(1)
        # send response message back
        receiver.send(response)

if __name__ == "__main__":
    # create 2 pipes
    gamer1, gamer2 = Pipe()
    # create 2 processes that will use ponger, give them different sides of pipes
    # they also need a specific message (either ping or pong)
    p1 = Process(target=ponger, args=(gamer2, gamer1, 'Pong'))
    p2 = Process(target=ponger, args=(gamer1, gamer2, 'Ping'))
    # start both processes
    p1.start()
    p2.start()
    # initiate ping-pong by sending first message to one of the pipes
    gamer1.send('Ping')

