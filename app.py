import datetime

from flask import Flask, jsonify, Response, render_template
import json
import random
import time

app = Flask(__name__)


@app.route('/api/time', methods=['GET'])
def time_serv():
    def gen_time():
        while True:
            yield f'data: {str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}\n\n'
            time.sleep(1)

    return Response(gen_time(), mimetype='text/event-stream')


@app.route('/api/status', methods=['GET'])
def serv_status():
    def gen_status():
        while True:
            yield f'data: OK\n\n'
            time.sleep(1)

    return Response(gen_status(), mimetype='text/event-stream')


@app.route('/api/conveyer_1', methods=['GET'])
def conveyer_1():
    def gen_conveyer_1():
        while True:
            yield f'data: {random.randint(0, 1000)}\n\n'
            time.sleep(1)
    return Response(gen_conveyer_1(), mimetype='text/event-stream')


@app.route('/api/conveyer_2', methods=['GET'])
def conveyer_2():
    def gen_conveyer_2():
        while True:
            yield f'data: {random.randint(0, 1000)}\n\n'
            time.sleep(1)
    return Response(gen_conveyer_2(), mimetype='text/event-stream')


@app.route('/api/conveyer_3', methods=['GET'])
def conveyer_3():
    def gen_conveyer_3():
        while True:
            yield f'data: {random.randint(0, 1000)}\n\n'
            time.sleep(1)
    return Response(gen_conveyer_3(), mimetype='text/event-stream')

@app.route('/api/furnace', methods=['GET'])
def furnace():
    def gen_furnace():
        while True:
            yield f'data: {random.choice(['Processing', 'Awaiting'])}\n\n'
            time.sleep(5)
    return Response(gen_furnace(), mimetype='text/event-stream')


@app.route('/api/random', methods=['GET'])
def random_number():
    return jsonify({'random': random.random()})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9090, debug=True)
