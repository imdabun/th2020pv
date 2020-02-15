import redis
import json

redis_host = "localhost"
redis_port = 6379
redis_password = ""

data = {
    'p_id': 'j_Poll',
    'q_id': 'What is my name?',
    'c_id' : 'Never'
}
#def update_hello():

def find_redis(poll_id,question_id):
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    currentKeys = r.keys()
    currStr = "{\"p_id\": \"" + poll_id + "\", \"q_id\": \"" + question_id + "\", \"c_id\": "
    for a in currentKeys:
        if(not (len(a) > len(currStr)) or not (currStr == a[0:len(currStr)])):
            currentKeys.remove(a)
    outputs = []
    for a in currentKeys:
        b = a
        b = b.replace(currStr + "\"",'')
        b = b.replace("\"}","")
        outputs.append((b,int(r.get(a))))
    print(outputs)
    print(json.dumps(outputs))

def flush_redis(r):
    for key in r.keys():
        r.delete(key)

def hello_redis(dataStr):
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        if(r.exists(json.dumps(dataStr)) == 0):
            r.set(json.dumps(dataStr),0)
        else:
            r.set(json.dumps(dataStr), int(r.get(json.dumps(dataStr))) + 1)
    except Exception as e:
        print(e)

def updateHelloRedis():
    hello_redis(data)
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    for i in range(0,10):
        hello_redis(data)
        print(r.get(json.dumps(data)))
    data['c_id'] = 'Always'
    hello_redis(data)
    print(r.get(json.dumps(data)))
    #flush_redis(r)
    find_redis(data['p_id'],data['q_id'])

if __name__ == '__main__':
    updateHelloRedis()