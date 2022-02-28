
from flask import Flask,request,abort
import json

app = Flask(__name__)

@app.route('/register', methods = ['PUT'])
def register():
    js_obj = request.json()
    hostname = js_obj['hostname']
    ip = js_obj['ip']
    as_ip = js_obj['as_ip']
    as_port = js_obj['as_port']
    url = "http://" + as_ip + ":" + as_port + "/dnsmsg"
    dns_msg = {
            "TYPE" : "A",
            "NAME" : hostname,
            "VALUE": ip,
            "TTL" : 10,
        }
    dns_json = json.dumps(dns_msg)
    r = request.post(url,dns_json)
    return r 

@app.route('/fibonacci', methods = ['GET'])
def fib():
    number = request.args.get('number')
    if not isinstance(number,int):
        return abort(400)
    else: 
        return fib_recursion(number)

def fib_recursion(number):
    if (number == 0) or (number == 1):
        return number
    
    return fib_recursion(number-1) + fib_recursion(number-2)


app.run(host='0.0.0.0',
        port=9090,
        debug=True)