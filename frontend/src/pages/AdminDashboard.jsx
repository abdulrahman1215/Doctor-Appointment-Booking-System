import React, { useEffect, useState } from "react";
import axios from "axios";

const AdminDashboard = () => {
  const [stats, setStats] = useState(null);
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      window.location.href = "/login";
      return;
    }

    axios
      .get("http://127.0.0.1:5000/api/admin/stats", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => setStats(res.data))
      .catch(() => alert("Access denied or failed to load data"));
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  if (!stats)
    return (
      <div className="flex justify-center items-center min-h-screen text-xl text-gray-600">
        Loading...
      </div>
    );

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-blue-600">Admin Dashboard</h1>
        <button
          onClick={handleLogout}
          className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600"
        >
          Logout
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-md text-center">
          <h2 className="text-gray-500 mb-2">Total Users</h2>
          <p className="text-3xl font-bold text-blue-600">
            {stats.total_users}
          </p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-md text-center">
          <h2 className="text-gray-500 mb-2">Doctors</h2>
          <p className="text-3xl font-bold text-green-600">
            {stats.total_doctors}
          </p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-md text-center">
          <h2 className="text-gray-500 mb-2">Patients</h2>
          <p className="text-3xl font-bold text-indigo-600">
            {stats.total_patients}
          </p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-md text-center col-span-3">
          <h2 className="text-gray-500 mb-2">Appointments</h2>
          <div className="flex justify-around mt-4">
            <div>
              <p className="text-xl font-semibold text-blue-600">
                {stats.total_appointments}
              </p>
              <p className="text-gray-500">Total</p>
            </div>
            <div>
              <p className="text-xl font-semibold text-green-600">
                {stats.approved}
              </p>
              <p className="text-gray-500">Approved</p>
            </div>
            <div>
              <p className="text-xl font-semibold text-yellow-600">
                {stats.pending}
              </p>
              <p className="text-gray-500">Pending</p>
            </div>
            <div>
              <p className="text-xl font-semibold text-red-600">
                {stats.rejected}
              </p>
              <p className="text-gray-500">Rejected</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
