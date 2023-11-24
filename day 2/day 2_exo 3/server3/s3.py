#server 3-central
from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
myport = 8080
servers = {}


@app.route('/register', methods=['POST'])
def register():
    address = request.json.get('address')
    server_type = request.json.get('type')
    servers[server_type] = address
    print(server_type)
    return "Registered", 200

@app.route('/get_address', methods=['GET'])
def get_address():
    server_type = request.args.get('type')
    return "bonjour" + servers.get(server_type, "Not found"), 200

if __name__ == '__main__':
    #app.run(host="0.0.0.0",port=myport)
    #app.run(port=myport)
    app.run(host="0.0.0.0",port=myport)        #version docker
    print(servers)
