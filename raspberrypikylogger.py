import xmlrpc.client

# SERVER_IP = '192.168.0.19'
SERVER_IP = '192.168.0.73'

s = xmlrpc.client.ServerProxy(f'http://{SERVER_IP}:8000')

from pynput.keyboard import Listener
from pynput import keyboard
import time


def count_the_keys(key):
    blue = 7
    red = 1
    round = 0
    while True:

        if round == 0:
            s.set_brightness(1)
            s.clear()
            s.set_pixel(0, 255, 0, 0)
            s.set_pixel(7, 0, 0, 255)
            s.show()
            time.sleep(1)
        elif key == keyboard.Key.esc:
            return False
        elif key == keyboard.Key.tab and round == 0:
            s.set_brightness(1)
            s.set_pixel(0, 0, 0, 0)
            s.set_pixel(red, 255, 0, 0)
            s.show()
            red += 1
            time.sleep(1)
        elif key == keyboard.Key.tab and round != 1:
            s.set_brightness(1)
            s.set_pixel(red - 1, 0, 0, 0)
            s.set_pixel(red + 1, 255, 0, 0)
            s.show()
            red += 1
            time.sleep(1)
        elif key == keyboard.Key.space and round == 0:
            s.set_brightness(1)
            s.set_pixel(7, 0, 0, 0)
            s.set_pixel(blue - 1, 0, 0, 255)
            s.show()
            blue -= 2
            round -= 1
            time.sleep(1)
        elif key == keyboard.Key.space and round != 0:
            s.set_brightness(1)
            s.set_pixel(blue - 1, 0, 0, 0)
            s.set_pixel(blue - 1, 0, 0, 255)
            s.show()
            blue -= 2
            time.sleep(1)


with Listener(on_press=count_the_keys) as listener:
    listener.join()
