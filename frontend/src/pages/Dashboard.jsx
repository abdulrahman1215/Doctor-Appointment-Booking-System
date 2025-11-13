import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [appointments, setAppointments] = useState([]);
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      window.location.href = "/login";
      return;
    }

    const payload = JSON.parse(atob(token.split(".")[1]));
    setUser(payload);

    axios
      .get("http://127.0.0.1:5000/api/appointments", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => setAppointments(res.data))
      .catch(() => alert("Failed to load appointments"));
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  const updateStatus = async (id, status) => {
    try {
      await axios.put(
        `http://127.0.0.1:5000/api/appointments/${id}`,
        { status },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      alert(`Appointment ${status}`);
      setAppointments((prev) =>
        prev.map((a) => (a.id === id ? { ...a, status } : a))
      );
    } catch (err) {
      alert(err.response?.data?.message || "Failed to update");
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-blue-600">
          {user?.role === "doctor"
            ? "Doctor Dashboard"
            : "Patient Dashboard"}
        </h1>
        <button
          onClick={handleLogout}
          className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600"
        >
          Logout
        </button>
      </div>

      <div className="bg-white rounded-xl shadow-md p-4">
        <h2 className="text-xl font-semibold mb-3 text-gray-700">
          My Appointments
        </h2>

        {appointments.length === 0 ? (
          <p className="text-gray-500">No appointments yet.</p>
        ) : (
          <ul>
            {appointments.map((a) => (
              <li
                key={a.id}
                className="border-b py-2 flex justify-between items-center text-gray-700"
              >
                <span>
                  <strong>Doctor:</strong> {a.doctor_id} |{" "}
                  <strong>Date:</strong> {a.date}
                </span>
                <span>
                  <span
                    className={`font-semibold ${
                      a.status === "pending"
                        ? "text-yellow-600"
                        : a.status === "approved"
                        ? "text-green-600"
                        : "text-red-600"
                    }`}
                  >
                    {a.status}
                  </span>

                  {user?.role === "doctor" && a.status === "pending" && (
                    <span className="ml-4 space-x-2">
                      <button
                        onClick={() => updateStatus(a.id, "approved")}
                        className="bg-green-500 text-white px-2 py-1 rounded hover:bg-green-600"
                      >
                        Approve
                      </button>
                      <button
                        onClick={() => updateStatus(a.id, "rejected")}
                        className="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
                      >
                        Reject
                      </button>
                    </span>
                  )}
                </span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
