import React, { useEffect, useState } from "react";
import axios from "axios";

const DoctorList = () => {
  const [doctors, setDoctors] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/users?role=doctor")
      .then((res) => setDoctors(res.data))
      .catch(() => alert("Failed to fetch doctors"));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold text-blue-700 mb-4">Available Doctors</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {doctors.map((doc) => (
          <div
            key={doc.id}
            className="bg-white p-4 rounded-lg shadow-md border border-gray-100"
          >
            <h3 className="text-lg font-semibold">{doc.username}</h3>
            <p className="text-gray-500">{doc.email}</p>
            <a
              href={`/book/${doc.id}`}
              className="text-blue-600 mt-2 inline-block underline"
            >
              Book Appointment
            </a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DoctorList;
