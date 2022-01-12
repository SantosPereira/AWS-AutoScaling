from flask import Flask, render_template, request, jsonify
from cpu_load_generator import load_single_core, load_all_cores, from_profile

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/carga", methods=["POST"])
def geraCarga():
    taxaConsumo = float(request.form['taxaConsumo'])
    duracao = int(request.form['duracao'])
    # load_single_core(core_num=0, duration_s=20, target_load=0.4)  # generate load on single core (0)
    load_all_cores(duration_s=duracao, target_load=taxaConsumo)  # generates load on all cores
    # from_profile(path_to_profile_json=r"c:\profiles\profile1.json")

    dados = {
        'status':201
    }
    return jsonify(dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0')