import xmlrpc.client

#SERVER_IP = '192.168.0.19'
SERVER_IP = '192.168.0.73'

blinkt = xmlrpc.client.ServerProxy(f'http://{SERVER_IP}:8000')
#!/usr/bin/env python3
import time
from sys import exit

try:
    import psutil
except ImportError:
    exit('This script requires the psutil module\nInstall with: sudo apt install python3-psutil')

blinkt.set_clear_on_exit()

NUM_PIXELS = 8
def show_graph(v, r, g, b):
    v *= NUM_PIXELS
    for x in range(NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        blinkt.set_pixel(x, r, g, b)
        v -= 1

    blinkt.show()


blinkt.set_brightness(0.1)

while True:
    v = psutil.cpu_percent() / 100.0
    show_graph(v, 255, 255, 255)
    time.sleep(0.01)