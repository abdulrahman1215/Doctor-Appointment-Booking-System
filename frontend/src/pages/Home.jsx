import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-blue-50">
      <h1 className="text-4xl font-bold text-blue-700 mb-4">
        Doctor Appointment Booking System
      </h1>
      <div className="space-x-4">
        <Link
          to="/login"
          className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
        >
          Login
        </Link>
        <Link
          to="/register"
          className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700"
        >
          Register
        </Link>
      </div>
    </div>
  );
};

export default Home;
