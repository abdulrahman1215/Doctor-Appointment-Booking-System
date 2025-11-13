# Doctor-Appointment-Booking-System
🏥 Doctor Appointment Booking System

A full-stack web application for booking doctor appointments, built with Flask (backend) and React (frontend).

Features
User Authentication: Register and login as patients or doctors
Role-based Access: Different functionalities for patients and doctors
Appointment Management: Book, view, cancel, and update appointment status
Doctor Directory: Search and view available doctors
Admin Dashboard: Administrative features for managing the system
Responsive UI: Modern React frontend with Tailwind CSS
Tech Stack
Backend
Flask: Python web framework
Flask-JWT-Extended: JWT authentication
Flask-SQLAlchemy: Database ORM
Flask-Migrate: Database migrations
SQLite: Database (easily configurable for other databases)
Frontend
React: JavaScript library for UI
Vite: Build tool and dev server
React Router: Client-side routing
Axios: HTTP client for API calls
Tailwind CSS: Utility-first CSS framework





Project Structure


doctor-appointment-booking-system/
├── app.py                 # Flask application entry point
├── config.py              # Configuration settings
├── model.py               # Database models (User, Appointment)
├── database.db            # SQLite database file
├── routes/                # API route blueprints
│   ├── auth_routes.py     # Authentication endpoints
│   ├── appointment_routes.py  # Appointment management
│   └── doctor_routes.py   # Doctor-related endpoints
├── frontend/              # React frontend
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── api.js         # API configuration
│   │   └── App.jsx        # Main app component
│   ├── package.json
│   └── vite.config.js
└── README.md



Installation & Setup
Prerequisites
Python 3.8+
Node.js 16+
npm or yarn
Backend Setup
Clone the repository


git clone <https://github.com/abdulrahman1215/Doctor-Appointment-Booking-System>
cd doctor-appointment-booking-system
Create virtual environment


python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
Install Python dependencies


pip install flask flask-jwt-extended flask-sqlalchemy flask-migrate werkzeug
Set up the database


flask db init
flask db migrate
flask db upgrade
Run the backend


python app.py
The API will be available at http://localhost:5000

Frontend Setup
Navigate to frontend directory


cd frontend
Install dependencies


npm install
Run the development server


npm run dev
The frontend will be available at http://localhost:5173

API Endpoints
Authentication (/api/auth)
POST /api/auth/register - Register new user
POST /api/auth/login - User login
GET /api/auth/profile - Get user profile
Appointments (/api/appointments)
GET /api/appointments/doctors - Get all doctors
POST /api/appointments/book - Book appointment
GET /api/appointments/my-appointments - View user's appointments
DELETE /api/appointments/cancel/<id> - Cancel appointment
PUT /api/appointments/update-status/<id> - Update appointment status (doctors only)
Doctors (/api/doctors)
GET /api/doctors/ - Get all doctors
GET /api/doctors/search?q=<query> - Search doctors
Usage
Register: Create an account as a patient or doctor
Login: Authenticate to access the system
For Patients:
View available doctors
Book appointments
View and cancel your appointments
For Doctors:
View your appointments
Update appointment status (confirm/reject)
Admin: Access admin dashboard for system management
Configuration
Update config.py for:

Database URI (currently SQLite)
JWT secret keys
Other Flask configurations
Testing the API
Use tools like Postman or curl to test endpoints. Most appointment endpoints require JWT authentication.

Example login request:


curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password"}'
Contributing
Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request
License
This project is licensed under the MIT License.
