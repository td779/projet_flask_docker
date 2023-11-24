from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
port_server_ping = 5372

#port de server pong
myport = 4567
url = f"http://localhost:{port_server_ping}"

def send_ping():
    time.sleep(0.5)
    response = requests.get(url + "/ping")
    print("Server 1-Pong received pong from Server 2-Ping:", response.text)


@app.route('/pong')
def pong():
    Thread(target=send_ping).start() #ajouter par chatGPT
    return "pong"

if __name__ == '__main__':
    #ping_thread = Thread(target=send_ping)
    #ping_thread.start()  
    app.run(port=myport)