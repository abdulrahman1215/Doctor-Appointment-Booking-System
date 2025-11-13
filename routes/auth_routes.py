from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from model import db, User

auth_routes = Blueprint('auth_routes', __name__)

# ------------------------------------------------
# 1️⃣ REGISTER USER (Patient or Doctor)
# ------------------------------------------------
@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'patient')
    specialization = data.get('specialization', None)

    if not name or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    hashed_pw = generate_password_hash(password)

    new_user = User(
        name=name,
        email=email,
        password=hashed_pw,
        role=role,
        specialization=specialization
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': f'{role.capitalize()} registered successfully!'}), 201


# ------------------------------------------------
# 2️⃣ LOGIN USER (Generate JWT Token)
# ------------------------------------------------
@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid email or password'}), 401

    # Generate JWT token
    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        'message': 'Login successful!',
        'token': access_token,
        'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        }
    }), 200


# ------------------------------------------------
# 3️⃣ TEST PROTECTED ROUTE (Optional)
# ------------------------------------------------
@auth_routes.route('/profile', methods=['GET'])
def profile():
    return jsonify({'message': 'Profile route working (test)'}), 200
