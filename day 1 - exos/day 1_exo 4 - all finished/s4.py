from flask import Flask, request
import requests

app = Flask(__name__)
myport = 1111

@app.route('/<port>/<message>')
def get_info(port = None, message = None):
  requests.get("http://"+str(port)) 
  print('Port : ' + str(port) + ' Message : ' + str('message'))
  return 'Port : ' + str(port) + ' Message : ' + str('message')


if __name__ == "__main__":
    #app.run(port=1111)
    app.run(host="0.0.0.0",port=myport)        #version docker
