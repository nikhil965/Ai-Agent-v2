import sys
import traceback
from flask import Flask, request, jsonify, send_from_directory

from agent import Agent
from config import API_KEY

app = Flask(__name__, static_folder="static", static_url_path="")

agent = Agent()


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "api_key_exists": API_KEY is not None
    })


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)

        user_input = data.get("message", "").strip()

        if not user_input:
            return jsonify({
                "success": False,
                "error": "Empty message"
            }), 400

        response = agent.run(user_input)

        return jsonify({
            "success": True,
            "response": response
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500


def run_cli():
    print("=" * 60)
    print("AI Agent")
    print("=" * 60)

    cli_agent = Agent()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            break

        try:
            response = cli_agent.run(user_input)
            print(f"Bot: {response}")

        except Exception:
            traceback.print_exc()


if __name__ == "__main__":
    if "--cli" in sys.argv:
        run_cli()
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)