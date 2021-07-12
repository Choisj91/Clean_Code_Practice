# Won't work
# start()


def start():
    print('Start')
    next()


# Won't work
# start()


def next():
    print('Next')
    last()


def last():
    print('Last')

# Will work
# All the methods must me declared before the start method
start()