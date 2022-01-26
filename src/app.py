from flask import Flask, request, jsonify, make_response
from cpu_load_generator import load_all_cores

app = Flask(__name__)

@app.route("/")
def main():
    return "Back-end dentro do Load Balancer"
    # return render_template('index.html')


@app.route("/carga", methods=["POST"])
def geraCarga():
    resposta = make_response(
        jsonify(
        dados = {
            'status':201
        }
        )
    )
    resposta.headers['Access-Control-Allow-Origin'] = '*'
    taxaConsumo = float(request.form['taxaConsumo'])
    duracao = int(request.form['duracao'])
    load_all_cores(duration_s=duracao, target_load=taxaConsumo)

    return resposta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)