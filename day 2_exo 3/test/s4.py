from flask import Flask, request
import requests

app = Flask(__name__)
server3_url = "http://localhost:8080"   #version docker
myport = 1111

@app.route('/<adresse>/<message>', methods=['POST','GET'])
def get_info(adresse = None, message = None):
  if message =="pong" :
    requests.post(f"http://localhost:8574/{adresse}/{message}")        #version docker
  else :
    requests.get("http://"+str(adresse)) 
    #requests.post("http://localhost:1111/adresse/message")        #version docker
  print('Adresse (host:port) de destinataire : ' + str(adresse) + ' Message : ' + str(message))
  return 'Adresse (host:port) : ' + str(adresse) + ' Message : ' + str('message')

if __name__ == "__main__":
    requests.post(server3_url + '/register', json={'address': f'http://localhost:{myport}', 'type': 'server4'})
    #app.run(host="0.0.0.0",port=myport)        #version docker
    app.run(port=myport)
