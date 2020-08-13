import os
import redis
from flask import Flask, request

# variables
ENV = os.environ
REDIS_HOST = ENV['REDIS_HOST'] if 'REDIS_HOST' in ENV else 'localhost'
REDIS_PORT = ENV['REDIS_PORT'] if 'REDIS_PORT' in ENV else '6379'
REDIS_DB = ENV['REDIS_DB'] if 'REDIS_DB' in ENV else '0'


app = Flask(__name__)
# redis connection
#pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


@app.route("/")
def hello():
    return "ok"


@app.route("/redis")
def redis_pool():
    args = request.args
    vkey = args.get('key') if args.get('key') else 'a'
    value = args.get('val') if args.get('val') else 'sin valor'
    exp = args.get('exp') if args.get('exp') else '10'
    
    r.set(vkey, value)
    value = r.get(vkey).decode('utf8')

    return "saved {}={}".format(vkey, value)


# run local
if __name__ == "__main__":
    app.run(port=8080)