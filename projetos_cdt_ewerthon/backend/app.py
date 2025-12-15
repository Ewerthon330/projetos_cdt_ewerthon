from flask import Flask, request, jsonify
from flask_cors import CORS
from pricing_logic import simular_preco_final

app = Flask(__name__)
CORS(app)

@app.route("/simular_reserva", methods=["POST"])
def simular_reserva():
    try:
        dados = request.get_json()

        resultado = simular_preco_final(dados)

        return jsonify(resultado), 200

    except Exception as e:
        print("Erro em /simular_reserva:", e, flush=True)
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
