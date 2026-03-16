import redis
from flask import Flask
import time

app = Flask(__name__)

started = False
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/health/startup')
def startup():
    global started
    if not started:
        started = True
    return 'OK', 200

@app.route('/health/liveness')
def liveness():
    return 'I am alive', 200

@app.route('/health/readiness')
def readiness():
    if r is None:
        return 'Redis doesnt work', 503
    else:
        return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    while True:
        r.publish('news_channel', 'Hello world')
        time.sleep(5)