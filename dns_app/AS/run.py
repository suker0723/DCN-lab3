
from flask import Flask,request,abort
import json

app = Flask(__name__)

@app.route('/dnsmsg')            
def dnsmsg():                                           
    data = json.load(request.files['dns_json'])             
    with open('tempfib.txt', 'w') as dns_file:
        json.dump(data, dns_file)
    return '201' 

@app.route('/dnsquery')
def dnsquery():
    data = json.load(request.files['dns_json'])  
    with open('tempfib.txt','r') as dns_file:
        old_data = json.load(dns_file)
        if data['TYPE'] == old_data['TYPE'] and data['NAME'] == old_data['NAME'] :
            response = {
                "TYPE" : old_data["TYPE"],
                "NAME" : old_data["NAME"],
                "VALUE": old_data["VALUE"],
                "TTL" : old_data["TTL"],
            }
            return response
        else :
            return abort(400)
        

app.run(host='0.0.0.0',
        port=53533,
        debug=True)