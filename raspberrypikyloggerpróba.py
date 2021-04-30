import xmlrpc.client

# SERVER_IP = '192.168.0.19'
SERVER_IP = '192.168.0.73'

s = xmlrpc.client.ServerProxy(f'http://{SERVER_IP}:8000')

from pynput.keyboard import Listener
from pynput import keyboard

def count_the_keys(key):
    s.set_brightness(0.5)
    red = 1
    if key == keyboard.Key.tab:
        s.set_pixel((red-1), 0, 0, 0)
        s.set_pixel((red+1), 255, 0, 0)
        s.show()
        red = red + 1
    else:
        s.set_pixel(7, 0, 0, 255)
        s.show




    with Listener(on_press=count_the_keys) as listener:
        listener.join()
