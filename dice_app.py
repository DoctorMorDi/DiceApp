# dice_app.py
from flask import Flask, request, jsonify
import random
import os
from waitress import serve

app = Flask(__name__)

dice_max = {
    'D6': 6,
    'D8': 8,
    'D10': 10,
    'D12': 12,
    'D20': 20,
    'D100': 100
}

@app.route("/roll", methods=["GET"])
def roll_dice():
    dice_type = request.args.get('diceType', '').upper()
    max_value = dice_max.get(dice_type)
    if max_value:
        result = random.randint(1, max_value)
        return jsonify({"diceType": dice_type, "result": result})
    else:
        return jsonify({"error": "Invalid dice type!"}), 400

if __name__ == "__main__":
    if os.environ.get('VERCEL') != None:
        serve(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        app.run(debug=True)
