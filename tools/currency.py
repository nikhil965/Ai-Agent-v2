import requests

RATE_URL = "https://api.exchangerate-api.com/v4/latest/{base}"


def execute(arguments: dict) -> str:
    amount = arguments.get("amount")
    from_currency = arguments.get("from", "").upper()
    to_currency = arguments.get("to", "").upper()

    if amount is None or not from_currency or not to_currency:
        return "Currency conversion error: amount, from, to required"

    try:
        response = requests.get(RATE_URL.format(base=from_currency), timeout=10)
        response.raise_for_status()
        data = response.json()

        rate = data["rates"].get(to_currency)
        if rate is None:
            return f"Currency '{to_currency}' not found"

        converted = float(amount) * rate
        return f"{amount} {from_currency} = {converted:.2f} {to_currency}"

    except Exception as e:
        return f"Currency conversion error: {e}"


if __name__ == "__main__":
    print(execute({"amount": 100, "from": "USD", "to": "INR"}))