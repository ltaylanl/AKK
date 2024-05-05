from flask import Flask, jsonify, request

app = Flask(__name__)

# Örnek karakterler(veritabanımsı)
characters = [
    {"id": 1, "name": "Character 1", "level": 10},
    {"id": 2, "name": "Character 2", "level": 15}
]

# Karakterleri listeleme
@app.route('/characters', methods=['GET'])
def get_characters():
    return jsonify(characters)

# Karakteri alma
@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = next((char for char in characters if char['id'] == character_id), None)
    if character:
        return jsonify(character)
    else:
        return jsonify({"message": "Character not found"}), 404

# Yeni karakter oluşturma
@app.route('/characters', methods=['POST'])
def create_character():
    data = request.json
    new_character = {
        "id": len(characters) + 1,
        "name": data['name'],
        "level": data['level']
    }
    characters.append(new_character)
    return jsonify(new_character), 201

# Karakteri güncelleme
@app.route('/characters/<int:character_id>', methods=['PUT'])
def update_character(character_id):
    data = request.json
    character = next((char for char in characters if char['id'] == character_id), None)
    if character:
        character['name'] = data['name']
        character['level'] = data['level']
        return jsonify(character)
    else:
        return jsonify({"message": "Character not found"}), 404

# Karakteri silme
@app.route('/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    global characters
    characters = [char for char in characters if char['id'] != character_id]
    return jsonify({"message": "Character deleted"})

if __name__ == '__main__':
    app.run(debug=True)
