from flask import Flask, request
import requests

app = Flask(__name__)
server3_url = "http://server3-registry:8080"   #version docker
myport = 8574

@app.route('/<adresse>/<message>', methods=['POST','GET'])
def get_info(adresse = None, message = None):
  if message =="ping" :
    requests.post(f"http://server4-broker:1111/{adresse}/{message}")        #version docker
  #elif message =="pong" :
  else :
    requests.get("http://"+str(adresse)) 
  print('Adresse (host:port) de destinataire : ' + str(adresse) + ' Message : ' + str(message))
  return 'Adresse (host:port) : ' + str(adresse) + ' Message : ' + str('message')


if __name__ == "__main__":
    requests.post(server3_url + '/register', json={'address': f'http://server5-gateway:{myport}', 'type': 'server5'})
    app.run(host="0.0.0.0",port=myport)        #version docker
    #app.run(port=myport)
