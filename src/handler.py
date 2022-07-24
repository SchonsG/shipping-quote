from flask import Flask, request
from .models import Transporter

app = Flask(__name__)


@app.route("/shipping-quote", methods=["POST"])
def shipping_quote() -> list:
    data = request.get_json()

    weight = data["peso"]

    if weight <= 0:
        return {"body": []}

    result = []
    height = data["dimensao"]["altura"]
    width = data["dimensao"]["largura"]

    transporters = Transporter.check_delivery_availability(height, width)

    for transport in transporters:
        total = (weight * transport.constant) / 10

        result.append(
            {
                "nome": transport.name,
                "prazo_dias": transport.delivery_time,
                "valor_frete": total,
            }
        )

    return {"body": result}
