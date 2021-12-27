import psutil
from flask import Flask, jsonify
import subprocess
import time

app = Flask(__name__)

@app.route('/test_cpu/<duration>/<load>')
def test(duration, load):
    try:
        subprocess.Popen(["python","-m","cpu_load_generator","-l", load, "-d", duration, "-c", "-1"])
        half_of_duration = int(int(duration) // 2)
        time.sleep(half_of_duration)
        cpu_stats = psutil.cpu_percent(percpu=True)

        return jsonify({
            'cpu_stats': cpu_stats,
        })
    except Exception as e:
        print(e)
        return 'Invalid request'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')