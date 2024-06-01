from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://sudipk166:Sudip12345@first.pqabnqo.mongodb.net/"

client = MongoClient(MONGO_URI)
db = client['DemoDB']
users_collection = db['Food']

@app.route('/')
def hello():
    return "Hello World"

@app.route('/description')
def description():
    return "This is Description"


# Read Operation

@app.route('/api/user', methods=['GET'])
def get_user():
        users = list(users_collection.find({}, {'_id': 0}))
        return jsonify(users), 500
 
# Create Opeartion

@app.route('/api/user', methods=['POST'])
def add_user():
        new_user = request.get_json()  
        response = users_collection.insert_one(new_user)
        new_user['_id'] = str(response.inserted_id)  
        return jsonify(new_user), 201

#Delete Operation
    
@app.route('/api/user/<string:name>', methods=['DELETE'])
def delete_user(name):
        result = users_collection.delete_one({'name': name})
        if result.deleted_count > 0:
            return jsonify({"message": f"User '{name}' deleted."}), 200
        else:
            return jsonify({"message": f"User '{name}' not found."}), 404
 


if __name__ == '__main__':
    app.run(debug=True)
