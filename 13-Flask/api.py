from flask import Flask, jsonify, request


app= Flask(__name__)

items = [
    {"id":1, "name":"Item 1", "description":"This is first task"},
    {"id":2, "name":"Item 2", "description":"This is second task"}
]


@app.route('/')
def home():
    return "Welcome To The Sample To DO List App"


#get and retrieve all items
@app.route("/items", methods=["GET"])
def get_tems():
    return jsonify(items)

#item by id
@app.route("/items/<int:item_id>", methods=["GET"])
def itemby_id(item_id):
    item = next((x for x in items if item_id==x["id"]), None)
    if item is None:
        return jsonify({"Error: no such item found"})
    return jsonify(item)


#create new - POST API
#so using POSTMAN, we do POST request and provide with name and description and it appends the items
@app.route('/items', methods=["POST"])
def add_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"No item"})
    new_item={
        "id": items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

#updating existing
#likewise, we provide with an id and it updates the name and description for the id via postman
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((x for x in items if x["id"]==item_id), None)
    if item is None:
        return jsonify ({"Errornot found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

#delete
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global item
    items = [x for x in items if x["id"]!=item_id]
    return jsonify({"result": "Item deleted"})



if __name__ == "__main__":
    app.run(debug=True)