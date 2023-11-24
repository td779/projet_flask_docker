from flask import Flask
import requests
import threading
import time

app = Flask(__name__)
myport = 4567
server3_url = "http://server3:8080"  #version docker
#server3_url = "http://localhost:8080"

def send_pong():
    time.sleep(2)
    #requests.get("http://localhost:1111/localhost:5372/pong")
    requests.get("http://server4:1111/server2:5372/pong")        #version docker
    
    #alimenter la partie get_address du server 3
    requests.get(server3_url + '/get_address', params={'type': 'server1'})

#threading.Thread(target=send_pong).start()

@app.route('/')
def index():
    threading.Thread(target=send_pong).start()
    return "Server 1"


if __name__ == "__main__":
    #print(requests.post(server3_url + '/register', json={'address': f'http://localhost:{myport}', 'type': 'server1'}))
    print(requests.get(server3_url + '/register', json={'address': f'http://server1:{myport}', 'type': 'server1'}))
    #app.run(port=myport)
    app.run(host="0.0.0.0",port=myport)        #version docker
