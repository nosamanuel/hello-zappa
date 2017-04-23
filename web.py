from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.json:
        print(request.json)

    return jsonify([])
