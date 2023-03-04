from time import time
from rich import print as rprint

class exec_time():

    def start():
        global init
        init = time()
    
    def stop():
        total_in_seconds = (time() - init)
        total_in_millisecond = total_in_seconds * 1000
        rprint('[bold yellow]exec_time: [white]{:.2f}ms'.format(total_in_millisecond))