Doctor-Appointment-Booking-System

🏥 Doctor Appointment Booking System
A full-stack web application for booking doctor appointments, built with Flask (backend) and React + Tailwind CSS (frontend).

🔎 Summary

This project provides:

User authentication (patients and doctors)

Role-based access (patient / doctor / admin)

Appointment booking, cancellation, and status updates

Doctor directory and search

Responsive React UI with Tailwind CSS

🧰 Tech Stack

Backend

Python, Flask

Flask-JWT-Extended (JWT auth)

Flask-SQLAlchemy (ORM)

Flask-Migrate (DB migrations)

SQLite (default, easy to change to PostgreSQL)

Frontend

React (Vite)

Tailwind CSS

Axios

React Router

Tools

Postman / curl for API testing

Git & GitHub

📁 Project Structure
doctor-appointment-booking-system/
├── app.py                 # Flask application entry point
├── config.py              # Configuration & env loading
├── model.py               # Database models (User, Appointment, ...)
├── database.db            # SQLite DB file (auto-created)
├── routes/                # API route blueprints
│   ├── auth_routes.py
│   ├── appointment_routes.py
│   └── doctor_routes.py
├── migrations/            # Flask-Migrate migrations
├── requirements.txt
├── frontend/              # React frontend (Vite + Tailwind)
│   ├── package.json
│   └── src/
└── README.md

⚙️ Prerequisites

Python 3.8+

Node.js 16+ and npm/yarn

(Optional) PostgreSQL if you prefer a production DB

🛠 Installation & Setup
1) Clone repository
git clone https://github.com/abdulrahman1215/Doctor-Appointment-Booking-System.git
cd Doctor-Appointment-Booking-System

2) Backend (Flask)
Create & activate virtualenv

Windows

python -m venv venv
venv\Scripts\activate


Mac / Linux

python -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Environment variables

Create a .env file in the backend root (or project root if backend is at repo root). Example .env:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_flask_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=sqlite:///database.db
# For PostgreSQL example:
# DATABASE_URL=postgresql://postgres:password@localhost:5432/doctor_db


If you use PostgreSQL, create the database first:

CREATE DATABASE doctor_db;

Initialize database & run migrations (Flask-Migrate)

Make sure FLASK_APP is set (from .env or export).
Linux / Mac

export FLASK_APP=app.py
flask db init        # only first time
flask db migrate -m "Initial migration"
flask db upgrade


Windows (cmd)

set FLASK_APP=app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Run the backend
python app.py


Default server: http://127.0.0.1:5000 (or as configured)

3) Frontend (React + Tailwind)
cd frontend
npm install
npm run dev


Frontend default (Vite): http://localhost:5173

Note: Make sure frontend api base URL points to your Flask backend (e.g., http://localhost:5000/api). Update frontend/src/api.js (or wherever configured).

📡 API Endpoints (summary)

Authentication

POST /api/auth/register — Register new user (role: patient/doctor/admin)

POST /api/auth/login — Login (returns JWT)

GET /api/auth/profile — Get current user (auth required)

Appointments

GET /api/appointments/doctors — List all doctors

POST /api/appointments/book — Book an appointment (auth required)

GET /api/appointments/my-appointments — User appointments (auth required)

DELETE /api/appointments/cancel/<id> — Cancel appointment (auth required)

PUT /api/appointments/update-status/<id> — Update status (doctors only)

Doctors

GET /api/doctors/ — All doctors

GET /api/doctors/search?q=<query> — Search doctors

🔐 Auth Flow (brief)

User registers → stored in DB with role.

User logs in → backend returns JWT.

Frontend stores token (e.g., localStorage).

Requests to protected routes include header:

Authorization: Bearer <JWT_TOKEN>

🔬 Example cURL Requests

Register

curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Ram","email":"ram@example.com","password":"pass123","role":"PATIENT"}'


Login

curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"ram@example.com","password":"pass123"}'


Protected: Get my appointments

curl -X GET http://localhost:5000/api/appointments/my-appointments \
  -H "Authorization: Bearer <YOUR_JWT>"

✅ Good-to-have / Future Enhancements

Switch from SQLite → PostgreSQL for production

Email notifications (appointment confirmation)

SMS / OTP verification

Pagination & filters for doctor search

Admin dashboard UI & stats

Docker + docker-compose for local multi-service startup

CI/CD pipeline (GitHub Actions)

🧪 Testing the API

Use Postman or Insomnia to test endpoints. Import a collection (if you have one) that contains register/login/book flows. Ensure you add Authorization header with the Bearer <token> for protected endpoints.

🤝 Contributing

Fork repo

Create feature branch: git checkout -b feature/your-feature

Commit changes & push: git push origin feature/your-feature

Open a Pull Request — describe changes & purpose

Please follow the existing code style and test new changes.

📝 License

This project is licensed under the MIT License — see LICENSE for details.

👤 Author

Abdul Rahman

GitHub: https://github.com/abdulrahman1215

Email: mdabdulrahmanaslam@gmail.com
