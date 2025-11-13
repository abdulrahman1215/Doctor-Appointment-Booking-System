from flask import Blueprint, request, jsonify
from model import User

doctor_bp = Blueprint('doctor_bp', __name__)

# ------------------------------------------------
# 1️⃣ GET ALL DOCTORS
# ------------------------------------------------
@doctor_bp.route('/', methods=['GET'])
def get_all_doctors():
    doctors = User.query.filter_by(role='doctor').all()
    doctor_list = [
        {
            'id': doc.id,
            'name': doc.name,
            'email': doc.email,
            'specialization': doc.specialization
        } for doc in doctors
    ]
    return jsonify({'doctors': doctor_list}), 200


# ------------------------------------------------
# 2️⃣ SEARCH DOCTORS BY NAME OR SPECIALIZATION
# ------------------------------------------------
@doctor_bp.route('/search', methods=['GET'])
def search_doctors():
    query = request.args.get('q', '')
    doctors = User.query.filter(
        User.role == 'doctor',
        (User.name.ilike(f'%{query}%')) | (User.specialization.ilike(f'%{query}%'))
    ).all()

    doctor_list = [
        {
            'id': doc.id,
            'name': doc.name,
            'email': doc.email,
            'specialization': doc.specialization
        } for doc in doctors
    ]
    return jsonify({'results': doctor_list}), 200
