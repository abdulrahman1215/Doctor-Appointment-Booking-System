from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import Config
from model import db
from routes.auth_routes import auth_routes
from routes.appointment_routes import appointment_bp
from routes.doctor_routes import doctor_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(appointment_bp, url_prefix='/api/appointments')
app.register_blueprint(doctor_bp, url_prefix='/api/doctors')

@app.route('/')
def home():
    return {"message": "Doctor Appointment API Running Successfully"}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not existing
    app.run(debug=True)
