from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    name = data['name']
    date = data['date']
    city = data['city']
    grade = float(data['grade'])

    if grade < 10:
        result = "Result: Bad"
    elif grade < 17:
        result = "Result: Moderate"
    elif grade < 19:
        result = "Result: Very Good"
    else:
        result = "Result: Excellent"

    recommendation = f"{name} from {city} on {date} received a grade of {grade}/20. {result}."
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


