from flask import Flask, request, jsonify
from cpu_load_generator import load_all_cores

app = Flask(__name__)

@app.route("/")
def main():
    return "Back-end dentro do Load Balancer"
    # return render_template('index.html')


@app.route("/carga", methods=["POST"])
def geraCarga():
    taxaConsumo = float(request.form['taxaConsumo'])
    duracao = int(request.form['duracao'])
    load_all_cores(duration_s=duracao, target_load=taxaConsumo)

    dados = {
        'status':201
    }
    return jsonify(dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)