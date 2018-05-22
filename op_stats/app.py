from flask import Flask
import json
import sys
sys.path.append('/home/steven/so-exam3')
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/v1/stats/cpu')
def informacion_cpu():
    info_cpu = Stats.get_porcentaje_cpu()
    return json.dumps({'CPU_PORCENT': info_cpu})

@app.route('/v1/stats/memory')
def informacion_memoria():
    info_memoria = Stats.get_memoria_disponible()
    return json.dumps({'AVAILABLE_MEMORY': info_memoria})

@app.route('/v1/stats/disk')
def informacion_disco():
    info_disco = Stats.get_espacio_disco()
    return json.dumps({'FREE_DISK': info_disco})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
