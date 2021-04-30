import xmlrpc.client

#SERVER_IP = '192.168.0.19'
SERVER_IP = '192.168.0.73'

s = xmlrpc.client.ServerProxy(f'http://{SERVER_IP}:8000')
s.set_brightness(0.1)
s.clear()
s.set_pixel(0, 255, 255, 255)
s.show()

