import ccxt
from flask import Flask, jsonify


app = Flask(__name__)
binance = ccxt.binance()
orderbook = binance.fetch_order_book('BTC/USDT')


@app.route("/spending", methods=["GET"])
def spending():
    asks = orderbook.get("asks")
    bids = orderbook.get("bids")
    response = {
        "asks": [ {"price": price, "quantity": btc} for price, btc in asks ],
        "bids": [ {"price": price, "quantity": btc} for price, btc in bids ],
    }
    print(response)
    return jsonify({
        "result": True,
        "data": response
    })


if __name__ == '__main__':
    app.run()
