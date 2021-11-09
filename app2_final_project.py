from flask import Flask, json, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

plants = ["Monstera Deliciosa", "Begonia Imaculata", "Succulent", "Sansevieria Trifasciata", "Cactaceae"]
plants = {
    "items": plants
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inventory")
def inventory_items():
    return jsonify({"items": f"Please select a plant from the list and we'll notify you when to water it: {', '.join(plants['items'])}."})
    
@app.route("/plants", methods=["POST"])
def plants_page():
    response = plants["items"]
    if response is None:
        return render_template("items.html")
    else:
        return render_template("items.html", items=response)

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign-up.html")

if __name__ == "__main__":
    app.run(debug=True)
