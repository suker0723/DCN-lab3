
from flask import Flask,request,abort
import json
import requests
app = Flask(__name__)


@app.route('/fibonacci',methods=['GET'])
def user():
    hostname = request.args.get('hostname')
    if hostname is None:
        return abort(400)
    fs_port = request.args.get('fs_port')
    if fs_port is None:
        return abort(400)
    seq_number = request.args.get('number')
    if seq_number is None:
        return abort(400)
    as_ip = request.args.get('as_ip')
    if as_ip is None:
        return abort(400)
    as_port = request.args.get('as_port')
    if as_port is None:
        return abort(400)

    url_dns = "http://" +"localhost" + ":" + as_port + "/dnsquery"
    myobj = {
        "NAME" : hostname,
        "TYPE" : "A",
    }
    res = requests.post(url_dns,data = myobj)
    url_res = "http://" + res['VALUE'] + "/" + res['NAME'] + "?" + "number=" + seq_number 
    ans = requests.post(url_res)
    return ans

app.run(host='0.0.0.0',
        port=8080,
        debug=True)