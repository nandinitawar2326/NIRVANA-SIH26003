
import { useState } from "react";

function AddPatient() {
  const [formData, setFormData] = useState({
    patient_id: "",
    name: "",
    age: "",
    gender: "",
    phone: "",
    address: "",
    dementia_stage: "",
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

    console.log("Patient Data:", formData);

    alert("Patient registered successfully!");
  }

  return (
    <div className="patient-registration-page">

      <div className="registration-card">

        <div className="registration-header">
          <div className="registration-icon">🧠</div>

          <h1>Patient Registration</h1>

          <p>
            Enter the patient's information
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
            <label>Patient Name</label>

            <input
              type="text"
              name="name"
              placeholder="Enter full name"
              value={formData.name}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-row">

            <div className="form-group">
              <label>Age</label>

              <input
                type="number"
                name="age"
                placeholder="Enter age"
                value={formData.age}
                onChange={handleChange}
                min="1"
                max="120"
                required
              />
            </div>

            <div className="form-group">
              <label>Gender</label>

              <select
                name="gender"
                value={formData.gender}
                onChange={handleChange}
                required
              >
                <option value="">Select gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
              </select>
            </div>

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
            <label>Address</label>

            <textarea
              name="address"
              placeholder="Enter patient's address"
              value={formData.address}
              onChange={handleChange}
              rows="3"
              required
            />
          </div>

          <div className="form-group">
            <label>Dementia Stage</label>

            <select
              name="dementia_stage"
              value={formData.dementia_stage}
              onChange={handleChange}
              required
            >
              <option value="">Select dementia stage</option>
              <option value="Mild">Mild</option>
              <option value="Moderate">Moderate</option>
              <option value="Severe">Severe</option>
            </select>
          </div>

          <button
            type="submit"
            className="register-patient-button"
          >
            Register Patient
          </button>

        </form>

      </div>

    </div>
  );
}

export default AddPatient;

