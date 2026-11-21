
from flask import Flask, jsonify, request
from uuid import uuid4
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

# Stores simulated payments during application runtime
payments = {}
processed_keys = {}


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "PayShield Payment API is running",
        "status": "healthy"
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/payment", methods=["POST"])
def make_payment():

    data = request.get_json(silent=True)

    # Validate JSON request
    if not isinstance(data, dict):
        return jsonify({"error": "A valid JSON request is required"}), 400

    # Check amount
    if "amount" not in data:
        return jsonify({"error": "Amount is required"}), 400

    try:
        amount = Decimal(str(data["amount"]))
    except (InvalidOperation, ValueError, TypeError):
        return jsonify({"error": "Amount must be a valid number"}), 400

    if not amount.is_finite() or amount <= 0:
        return jsonify({"error": "Amount must be greater than zero"}), 400

    # Duplicate request protection
    idempotency_key = request.headers.get("Idempotency-Key")

    if idempotency_key and idempotency_key in processed_keys:
        return jsonify(processed_keys[idempotency_key]), 200

    # Create a unique transaction ID
    transaction_id = str(uuid4())

    payment = {
        "transaction_id": transaction_id,
        "amount": str(amount),
        "status": "SUCCESS",
        "message": "Simulated payment processed successfully"
    }

    payments[transaction_id] = payment

    if idempotency_key:
        processed_keys[idempotency_key] = payment

    return jsonify(payment), 201


@app.route("/payment/<transaction_id>", methods=["GET"])
def get_payment(transaction_id):
    payment = payments.get(transaction_id)

    if not payment:
        return jsonify({"error": "Transaction not found"}), 404

    return jsonify(payment), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
