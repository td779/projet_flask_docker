#server Pong
from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
port_server_ping = 5372

#port de server pong
myport = 4567


server3_url = "http://localhost:8080"


def send_to_ping():
    time.sleep(3)
    address = requests.get(server3_url + '/get_address', params={'type': 'server2'}).text    
    response = requests.get(address + "/ping")
    print("Server 1-Pong received pong from Server 2-Ping via 3 :", response.text)


@app.route('/pong')
def pong():
    Thread(target=send_to_ping).start()
    return "Hi, pong's here"

if __name__ == '__main__':
    requests.post(server3_url + '/register', json={'address': f'http://localhost:{myport}', 'type': 'server1'})
    app.run(port=myport)