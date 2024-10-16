from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Hello, World! I have been seen {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
