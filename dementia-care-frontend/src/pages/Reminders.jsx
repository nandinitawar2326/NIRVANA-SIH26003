
import { useState } from "react";
import { Link } from "react-router-dom";

function Reminders() {
  const [formData, setFormData] = useState({
    patient_id: "",
    title: "",
    reminder_type: "",
    scheduled_time: "",
    description: "",
    status: "Active",
  });

  function handleChange(event) {
    const { name, value } = event.target;

    setFormData({
      ...formData,
      [name]: value,
    });
  }

  function handleSubmit(event) {
    event.preventDefault();

    console.log("Reminder Data:", formData);

    alert("Reminder created successfully!");
  }

  return (
    <div className="form-page">

      <Link to="/dashboard" className="back-button">
        ← Dashboard
      </Link>

      <div className="form-card">

        <div className="form-header">
          <div className="form-icon">⏰</div>

          <h1>Create Reminder</h1>

          <p>
            Schedule medicine and daily activity reminders.
          </p>
        </div>

        <form onSubmit={handleSubmit}>

          <div className="form-group">
            <label>Patient ID</label>

            <input
              type="text"
              name="patient_id"
              placeholder="Enter patient ID"
              value={formData.patient_id}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Reminder Title</label>

            <input
              type="text"
              name="title"
              placeholder="Example: Morning Medicine"
              value={formData.title}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Reminder Type</label>

            <select
              name="reminder_type"
              value={formData.reminder_type}
              onChange={handleChange}
              required
            >
              <option value="">Select reminder type</option>
              <option value="Medicine">Medicine</option>
              <option value="Meal">Meal</option>
              <option value="Water">Water</option>
              <option value="Exercise">Exercise</option>
              <option value="Appointment">Appointment</option>
              <option value="Sleep">Sleep</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <div className="form-group">
            <label>Scheduled Time</label>

            <input
              type="time"
              name="scheduled_time"
              value={formData.scheduled_time}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Description</label>

            <textarea
              name="description"
              placeholder="Enter reminder description"
              value={formData.description}
              onChange={handleChange}
              rows="4"
              required
            />
          </div>

          <div className="form-group">
            <label>Status</label>

            <select
              name="status"
              value={formData.status}
              onChange={handleChange}
            >
              <option value="Active">Active</option>
              <option value="Pending">Pending</option>
              <option value="Completed">Completed</option>
              <option value="Cancelled">Cancelled</option>
            </select>
          </div>

          <button
            type="submit"
            className="primary-form-button"
          >
            Create Reminder
          </button>

        </form>

      </div>

    </div>
  );
}

export default Reminders;

