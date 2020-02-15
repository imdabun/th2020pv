from flask import Flask
from flask_cors import CORS
from flask import jsonify
import redis
import json

redis_host = "localhost"
redis_port = 6379
redis_password = ""

app = Flask(__name__)
CORS(app)

def find_redis(r):
    currentKeys = r.keys()
    outputs = []
    for a in currentKeys:
        print(a,int(r.get(a)))
        outputs.append([a,int(r.get(a))])
    return outputs

def flush_redis(r):
    for key in r.keys():
        r.delete(key)

@app.route('/page/<page_id>',methods=['GET'])
def home(page_id):
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    if(page_id == "end"):
        outputs = find_redis(r)
        flush_redis(r)
        return jsonify(outputs)

    elif (page_id == "analy"):
        outputs = find_redis(r)
        return jsonify(outputs)

    else:
        print(page_id)
        if (r.exists(json.dumps(page_id)) == 0):
            r.set(json.dumps(page_id), 1)
        else:
            r.set(json.dumps(page_id), int(r.get(json.dumps(page_id))) + 1)
        return jsonify(r.get(json.dumps(page_id)))