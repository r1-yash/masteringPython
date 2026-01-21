from flask import Flask, jsonify, request


app= Flask(__name__)

items = [
    {"id":1, "name":"Item 1", "descrition":"This is first task"},
    {"id":2, "name":"Item 2", "descrition":"This is second task"}
]


@app.route('/')
def home():
    return "Welcome To The Sample To DO List App"


#get and retrieve all items
@app.route("/items", methods=["GET"])
def get_tems():
    return jsonify(items)

#item by id
@app.route("/item/<int:item_id>", methods=["GET"])
def itemby_id(item_id):
    item = next(x for x in items if item_id==x["id"])
    if item is None:
        return jsonify({"Error: no such item found"})
    return jsonify(item)


#create new 
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
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((x for x in items if x[id]==item_id), None)
    if item is None:
        return jsonify ({"Errornot found"})
    



if __name__ == "__main__":
    app.run(debug=True)