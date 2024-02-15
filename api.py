from flask import Flask, request, jsonify
from init import app,db
from model import User


@app.route('/',methods = ['GET'])
def sayHello():
    return "Hello!"

# 添加用户
@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'})

# 查询用户
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'})
    user_data = {
        'id': user.id,
        'name': user.name,
        'tel': user.tel
    }
    return jsonify({'user': user_data})

# 删除用户
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})


