#server Ping
from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
port_server_pong = 4567
#port de server ping
myport = 5372

server3_url = "http://localhost:8080"




def send_to_pong():
    time.sleep(3)
    address = requests.get(server3_url + '/get_address', params={'type': 'server1'}).text    
    response = requests.get(address + "/pong")
    print("Server 2-Ping received pong from Server 1-Pong via 3 :", response.text)


@app.route('/ping')
def ping():
    Thread(target=send_to_pong).start() 
    return "Hello, it's ping"

if __name__ == '__main__':
    requests.post(server3_url + '/register', json={'address': f'http://localhost:{myport}', 'type': 'server2'})
    app.run(port=myport)