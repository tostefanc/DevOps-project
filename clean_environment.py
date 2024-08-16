import requests

try:
    requests.get('http://127.0.0.1:5001/stop_server')
except Exception as e:
    print("Exception occurred when stopping web_app: ", e)

try:
    requests.get('http://127.0.0.1:5600/stop_server')
except Exception as e:
    print("Exception occurred when stopping rest_app: ", e)
