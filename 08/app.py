from flask import Flask, jsonify, abort, make_response, request
from inventory import get_items as get_items_dict, insert_item


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/api/v1.0/items', methods=['GET'])
def get_items():
    return jsonify(get_items_dict())


@app.route('/api/v1.0/items/<string:room_id>', methods=['GET'])
def get_rooms_items(room_id):
    room_items = [item for item in get_items_dict() if item['Room'] == room_id]
    if len(room_items) == 0:
        abort(404)
    return jsonify(room_items)


@app.route('/api/v1.0/items', methods=['POST'])
def create_item():
    if not request.json \
            or not ('item' in request.json and 'room' in request.json and 'cost' in request.json):
        abort(400)
    new_item = [request.json['room'],
                request.json['item'],
                request.json['cost']]
    insert_item(new_item)
    return jsonify({'item': new_item}), 201


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
