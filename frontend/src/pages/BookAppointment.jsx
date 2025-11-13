import React, { useState } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

const BookAppointment = () => {
  const { doctorId } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ date: "" });
  const token = localStorage.getItem("token");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(
        "http://127.0.0.1:5000/api/appointments",
        { doctor_id: doctorId, date: formData.date },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      alert("Appointment booked!");
      navigate("/dashboard");
    } catch (err) {
      alert(err.response?.data?.message || "Booking failed");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-50">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded-xl shadow-md w-full max-w-sm"
      >
        <h2 className="text-2xl font-bold text-center mb-4 text-blue-600">
          Book Appointment
        </h2>

        <input
          type="date"
          name="date"
          value={formData.date}
          onChange={(e) => setFormData({ date: e.target.value })}
          className="w-full p-2 mb-3 border rounded-md"
          required
        />

        <button
          type="submit"
          className="w-full bg-blue-600 text-white p-2 rounded-md hover:bg-blue-700"
        >
          Confirm Booking
        </button>
      </form>
    </div>
  );
};

export default BookAppointment;
