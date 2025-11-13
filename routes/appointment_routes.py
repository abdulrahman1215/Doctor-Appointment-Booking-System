from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from model import db, User, Appointment

appointment_bp = Blueprint('appointment_bp', __name__)

# ------------------------------------------------
# 1️⃣ GET ALL DOCTORS
# ------------------------------------------------
@appointment_bp.route('/doctors', methods=['GET'])
@jwt_required()
def get_doctors():
    doctors = User.query.filter_by(role='doctor').all()
    result = []
    for d in doctors:
        result.append({
            'id': d.id,
            'name': d.name,
            'email': d.email
        })
    return jsonify({'doctors': result}), 200


# ------------------------------------------------
# 2️⃣ BOOK AN APPOINTMENT (Patient)
# ------------------------------------------------
@appointment_bp.route('/book', methods=['POST'])
@jwt_required()
def book_appointment():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    patient = User.query.get(current_user_id)
    if patient.role != 'patient':
        return jsonify({'error': 'Only patients can book appointments'}), 403

    doctor_id = data.get('doctor_id')
    date = data.get('date')
    time = data.get('time')

    if not doctor_id or not date or not time:
        return jsonify({'error': 'All fields are required'}), 400

    doctor = User.query.filter_by(id=doctor_id, role='doctor').first()
    if not doctor:
        return jsonify({'error': 'Doctor not found'}), 404

    new_appointment = Appointment(
        patient_id=current_user_id,
        doctor_id=doctor_id,
        date=date,
        time=time,
        status='pending'
    )
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment booked successfully!'}), 201


# ------------------------------------------------
# 3️⃣ VIEW APPOINTMENTS (Patient & Doctor)
# ------------------------------------------------
@appointment_bp.route('/my-appointments', methods=['GET'])
@jwt_required()
def get_my_appointments():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if user.role == 'patient':
        appointments = Appointment.query.filter_by(patient_id=current_user_id).all()
    elif user.role == 'doctor':
        appointments = Appointment.query.filter_by(doctor_id=current_user_id).all()
    else:
        return jsonify({'error': 'Invalid user role'}), 400

    result = []
    for a in appointments:
        result.append({
            'id': a.id,
            'doctor_name': a.doctor.name if a.doctor else None,
            'patient_name': a.patient.name if a.patient else None,
            'date': a.date,
            'time': a.time,
            'status': a.status
        })

    return jsonify({'appointments': result}), 200


# ------------------------------------------------
# 4️⃣ CANCEL APPOINTMENT (Patient)
# ------------------------------------------------
@appointment_bp.route('/cancel/<int:appointment_id>', methods=['DELETE'])
@jwt_required()
def cancel_appointment(appointment_id):
    current_user_id = get_jwt_identity()
    appointment = Appointment.query.get(appointment_id)

    if not appointment:
        return jsonify({'error': 'Appointment not found'}), 404

    if appointment.patient_id != current_user_id:
        return jsonify({'error': 'Unauthorized action'}), 403

    appointment.status = 'cancelled'
    db.session.commit()

    return jsonify({'message': 'Appointment cancelled successfully!'}), 200


# ------------------------------------------------
# 5️⃣ UPDATE APPOINTMENT STATUS (Doctor only)
# ------------------------------------------------
@appointment_bp.route('/update-status/<int:appointment_id>', methods=['PUT'])
@jwt_required()
def update_appointment_status(appointment_id):
    current_user_id = get_jwt_identity()
    doctor = User.query.get(current_user_id)

    if doctor.role != 'doctor':
        return jsonify({'error': 'Only doctors can update status'}), 403

    data = request.get_json()
    new_status = data.get('status')

    if new_status not in ['confirmed', 'rejected']:
        return jsonify({'error': 'Invalid status. Use confirmed/rejected.'}), 400

    appointment = Appointment.query.filter_by(id=appointment_id, doctor_id=current_user_id).first()

    if not appointment:
        return jsonify({'error': 'Appointment not found'}), 404

    appointment.status = new_status
    db.session.commit()

    return jsonify({'message': f'Appointment status updated to {new_status}'}), 200

@appointment_bp.route('/api/admin/stats', methods=['GET'])
@jwt_required()
def admin_stats():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if user.role != 'admin':
        return jsonify({'message': 'Access denied — admin only'}), 403

    total_users = User.query.count()
    total_doctors = User.query.filter_by(role='doctor').count()
    total_patients = User.query.filter_by(role='patient').count()
    total_appointments = Appointment.query.count()
    approved = Appointment.query.filter_by(status='approved').count()
    rejected = Appointment.query.filter_by(status='rejected').count()
    pending = Appointment.query.filter_by(status='pending').count()

    return jsonify({
        'total_users': total_users,
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'approved': approved,
        'rejected': rejected,
        'pending': pending
    })
