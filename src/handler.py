from flask import Flask, request

from .models import Transporter

app = Flask(__name__)


@app.route("/shipping-quote", methods=["POST"])
def shipping_quote():
    request_data = request.get_json()

    width = request_data["dimensao"]["largura"]
    height = request_data["dimensao"]["altura"]
    weight = request_data["peso"]

    if weight <= 0:
        return {"data": []}

    transporters = Transporter.check_delivery_availability(height, width)

    result = []

    for transport in transporters:
        total = (weight * transport.constant) / 10

        result.append(
            {
                "nome": transport.name,
                "prazo_dias": transport.delivery_time,
                "valor_frete": total,
            }
        )

    return {"data": result}
