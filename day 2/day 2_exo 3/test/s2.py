from flask import Flask
import requests
import threading
import time

app = Flask(__name__)
myport = 5372
server3_url = "http://localhost:8080"   

def send_ping():
    time.sleep(2)
    requests.post("http://localhost:8574/localhost:4567/ping")
    
    #alimenter la partie get_address du server 3
    requests.get(server3_url + '/get_address', params={'type': 'server2'})


#threading.Thread(target=send_ping).start()

@app.route('/')
def index():
    threading.Thread(target=send_ping).start()
    return "Server 2"

if __name__ == "__main__":
    print(requests.post(server3_url + '/register', json={'address': f'http://localhost:{myport}', 'type': 'server2'}))
    #app.run(host="0.0.0.0",port=myport)        #version docker
    app.run(port=myport)

