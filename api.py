## put and delete https verbs
## working with api -- json

from flask import Flask, request, jsonify

app = Flask(__name__)

# initial data in my todo list
# Use a list of dicts (square brackets). A set (curly braces) containing dicts raises
# TypeError: unhashable type: 'dict' because dicts are unhashable.
items = [
    {'id': 1, 'task': 'Buy groceries', 'description': 'Milk, Bread, Eggs' },
    {'id': 2, 'task': 'Read book', 'description': 'Finish reading Flask tutorial' },
    {'id': 3, 'task': 'Exercise', 'description': 'Go for a 30-minute run' }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Todo app </h1>"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## get item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

## add new item
@app.route('/items', methods=['POST'])
def add_item():
    if not request.json or 'task' not in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'task': request.json['task'],
        'description': request.json.get('description', "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

## put update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad Request'}), 400

    item['task'] = request.json.get('task', item['task'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)
## delete item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    items = [itm for itm in items if itm['id'] != item_id]
    return jsonify({'result': 'Item deleted'})

if __name__ == "__main__":
    app.run(debug=True)