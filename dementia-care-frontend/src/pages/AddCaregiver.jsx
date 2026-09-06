
import { useState } from "react";
import { Link } from "react-router-dom";

function AddCaregiver() {
  const [formData, setFormData] = useState({
    name: "",
    phone: "",
    relationship: "",
    patient_id: "",
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

    console.log("Caregiver Data:", formData);

    alert("Family member added successfully!");
  }

  return (
    <div className="form-page">

      <Link to="/dashboard" className="back-button">
        ← Dashboard
      </Link>

      <div className="form-card">

        <div className="form-header">
          <div className="form-icon">👨‍👩‍👧</div>

          <h1>Add Family Member</h1>

          <p>
            Add one trusted family member who can monitor the patient's progress.
          </p>
        </div>

        <form onSubmit={handleSubmit}>

          <div className="form-group">
            <label>Name</label>

            <input
              type="text"
              name="name"
              placeholder="Enter family member name"
              value={formData.name}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Phone Number</label>

            <input
              type="tel"
              name="phone"
              placeholder="Enter phone number"
              value={formData.phone}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Relationship</label>

            <select
              name="relationship"
              value={formData.relationship}
              onChange={handleChange}
              required
            >
              <option value="">Select relationship</option>
              <option value="Son">Son</option>
              <option value="Daughter">Daughter</option>
              <option value="Wife">Wife</option>
              <option value="Husband">Husband</option>
              <option value="Brother">Brother</option>
              <option value="Sister">Sister</option>
              <option value="Grandchild">Grandchild</option>
              <option value="Other">Other</option>
            </select>
          </div>

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

          <button
            type="submit"
            className="primary-form-button"
          >
            Add Family Member
          </button>

        </form>

      </div>

    </div>
  );
}

export default AddCaregiver;

