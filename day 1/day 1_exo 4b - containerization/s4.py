from flask import Flask, request
import requests

app = Flask(__name__)
server3_url = "http://server3:8080"   #version docker
myport = 1111

@app.route('/<adresse>/<message>', methods=['POST','GET'])
def get_info(adresse = None, message = None):
  requests.get("http://"+str(adresse)) 
  print('Adresse (host:port) : ' + str(adresse) + ' Message : ' + str('message'))
  return 'Adresse (host:port) : ' + str(adresse) + ' Message : ' + str('message')


if __name__ == "__main__":
    requests.post(server3_url + '/register', json={'address': f'http://localhost:{myport}', 'type': 'server1'})
    app.run(host="0.0.0.0",port=myport)        #version docker
