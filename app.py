from flask import Flask, jsonify
import threading
import pymysql.cursors
import json
import random
import time


def generate_new_event():
    event = {
        'ship_type': random.choice(['TANKER', 'BOAT', 'POLICE', 'ECONOMY']),
        'ship_carrying': random.randint(60, 1200),
        'capitan_name': random.choice(['NIKOLAY OVECHKIN', 'IVAN LUKOV', 'ANTON ANTONOV', 'ALEKS BITOV'])
    }
    return json.dumps(event, indent=4, ensure_ascii=False), time.time()


def send_event():
    try:
        connection = pymysql.connect(host='212.233.88.28',
                                     user='user_root',
                                     password='fao43eS01W23fS2,9',
                                     database='TexUrok',
                                     cursorclass=pymysql.cursors.DictCursor)
        event, time_unix = generate_new_event()
        print('event created')
        with connection:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `Morine_Events` (`date_unix`, `event_json`) VALUES (%s, %s)"
                cursor.execute(sql, (time_unix, event))
                connection.commit()
                print('event send')
    except Exception as e:
        print(e)


class Worker(threading.Thread):
    def __int__(self):
        super().__init__()

    def run(self):
        while True:
            try:
                send_event()
            except Exception as e:
                print(e)
            time.sleep(120)


app = Flask(__name__)


@app.route('/get_credentials', methods=['GET'])
def get_credentials():
    return jsonify({
        'user': 'v',
        'password': '60DYrSUw298m2A80',
    })


if __name__ == '__main__':
    t1 = Worker()
    t1.daemon = True
    t1.start()
    app.run(host='84.23.55.222', port=9090)
