from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

advertisements = []

@app.route('/advertisements', methods=['POST'])
def create_advertisement():
    data = request.get_json()
    new_ad = {
        'id': len(advertisements) + 1,
        'title': data['title'],
        'description': data['description'],
        'created_at': datetime.now().isoformat(),
        'owner': data['owner']
    }
    advertisements.append(new_ad)
    return jsonify(new_ad), 201

@app.route('/advertisements', methods=['GET'])
def get_advertisements():
    return jsonify(advertisements), 200

@app.route('/advertisements/<int:ad_id>', methods=['DELETE'])
def delete_advertisement(ad_id):
    global advertisements
    advertisements = [ad for ad in advertisements if ad['id'] != ad_id]
    return jsonify({'message': 'Advertisement deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем сервер в режиме отладки