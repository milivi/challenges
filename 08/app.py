from flask import Flask, jsonify, abort, make_response, request
from inventory import InventoryManager


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/api/v1.0/items', methods=['GET'])
def get_items():
    return jsonify(InventoryManager().get_items())


@app.route('/api/v1.0/items/<string:room_id>', methods=['GET'])
def get_rooms_items(room_id):
    room_items = [item for item in InventoryManager().get_items() if item['Room'] == room_id]
    if len(room_items) == 0:
        abort(404)
    return jsonify(room_items)


@app.route('/api/v1.0/items/<int:row_id>', methods=['GET'])
def get_item(row_id):
    this_item = [item for item in InventoryManager().get_items() if item['ID'] == row_id]
    if len(this_item) == 0:
        abort(404)
    return jsonify(this_item)


@app.route('/api/v1.0/items', methods=['POST'])
def create_item():
    if not request.json \
            or not ('item' in request.json and 'room' in request.json and 'cost' in request.json):
        abort(400)
    new_item = [request.json['room'],
                request.json['item'],
                request.json['cost']]
    if InventoryManager().insert_item(new_item):
        return jsonify({'item': new_item}), 201
    else:
        # Create did not work
        return jsonify({'item', new_item}), 409


@app.route('/api/v1.0/items/<int:row_id>', methods=['DELETE'])
def delete_item(row_id):
    if InventoryManager().delete_item(row_id):
        return jsonify({'response': 'Deleted'})
    else:
        return jsonify({'response': 'Not Deleted'})


@app.route('/api/v1.0/items/<int:row_id>', methods=['PUT'])
def update_item(row_id):
    if not request.json or not row_id \
            or not ('item' in request.json and 'room' in request.json and 'cost' in request.json):
        abort(400)
    updated_item = [row_id,
                    request.json['room'],
                    request.json['item'],
                    request.json['cost']]
    if InventoryManager().update_item(updated_item):
        return jsonify(updated_item)
    else:
        # Update did not work
        return jsonify(updated_item), 409


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
