#server Ping
from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
port_server_pong = 4567

#port de server ping
myport = 5372
url = f"http://localhost:{port_server_pong}"




def send_pong():
    time.sleep(0.5)
    response = requests.get(url + "/pong")
    print("Server 2-Ping received pong from Server 1-Pong:", response.text)


@app.route('/ping')
def ping():
    Thread(target=send_pong).start() 
    return "ping"

if __name__ == '__main__':
    #pong_thread = Thread(target=send_pong)
    #pong_thread.start()
    app.run(port=myport)