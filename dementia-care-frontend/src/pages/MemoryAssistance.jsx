
import { useState } from "react";
import { Link } from "react-router-dom";

function MemoryAssistance() {
  const [formData, setFormData] = useState({
    patient_id: "",
    title: "",
    content: "",
    memory_type: "",
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

    console.log("Memory Assistance Data:", formData);

    alert("Memory saved successfully!");
  }

  return (
    <div className="form-page">

      <Link to="/dashboard" className="back-button">
        ← Dashboard
      </Link>

      <div className="form-card">

        <div className="form-header">
          <div className="form-icon">🧠</div>

          <h1>Memory Assistance</h1>

          <p>
            Save important memories to help the patient remember familiar people and places.
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
            <label>Memory Title</label>

            <input
              type="text"
              name="title"
              placeholder="Example: My Daughter"
              value={formData.title}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Memory Content</label>

            <textarea
              name="content"
              placeholder="Enter memory information..."
              value={formData.content}
              onChange={handleChange}
              rows="6"
              required
            />
          </div>

          <div className="form-group">
            <label>Memory Type</label>

            <select
              name="memory_type"
              value={formData.memory_type}
              onChange={handleChange}
              required
            >
              <option value="">Select memory type</option>
              <option value="Family">Family</option>
              <option value="Person">Person</option>
              <option value="Place">Place</option>
              <option value="Event">Event</option>
              <option value="Routine">Routine</option>
              <option value="Personal Information">
                Personal Information
              </option>
              <option value="Other">Other</option>
            </select>
          </div>

          <button
            type="submit"
            className="primary-form-button"
          >
            Save Memory
          </button>

        </form>

      </div>

    </div>
  );
}

export default MemoryAssistance;

