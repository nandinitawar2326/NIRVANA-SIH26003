
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { createPatient } from "../services/api";

function PatientRegistration() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    age: "",
    gender: "",
    location: "",
    caregiver_name: "",
  });

  const [loading, setLoading] = useState(false);

  function handleChange(event) {
    const { name, value } = event.target;

    setFormData({
      ...formData,
      [name]: value,
    });
  }

  async function handleSubmit(event) {
    event.preventDefault();

    setLoading(true);

    try {
      const patientData = {
        name: formData.name,
        age: Number(formData.age),
        gender: formData.gender,
        location: formData.location,
        caregiver_name: formData.caregiver_name,
      };

      console.log("Sending patient:", patientData);

      const result = await createPatient(patientData);

      console.log("Backend response:", result);

      // Save returned patient information
      localStorage.setItem(
        "patient",
        JSON.stringify(result.patient)
      );

      alert("Patient registered successfully! ✅");

      // Go to Home
      navigate("/home");

    } catch (error) {
      console.error("Registration error:", error);

      alert(
        "Unable to register patient.\n\n" +
        error.message
      );

    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="form-page">

      <Link to="/" className="back-button">
        ← Welcome
      </Link>

      <div className="form-card">

        <div className="form-header">

          <div className="form-icon">
            🧠
          </div>

          <h1>
            Patient Registration
          </h1>

          <p>
            Enter the patient's information to create an account.
          </p>

        </div>

        <form onSubmit={handleSubmit}>

          {/* PATIENT NAME */}
          <div className="form-group">

            <label>
              Patient Name
            </label>

            <input
              type="text"
              name="name"
              placeholder="Enter full name"
              value={formData.name}
              onChange={handleChange}
              required
            />

          </div>


          {/* AGE */}
          <div className="form-group">

            <label>
              Age
            </label>

            <input
              type="number"
              name="age"
              placeholder="Enter age"
              min="1"
              max="120"
              value={formData.age}
              onChange={handleChange}
              required
            />

          </div>


          {/* GENDER */}
          <div className="form-group">

            <label>
              Gender
            </label>

            <select
              name="gender"
              value={formData.gender}
              onChange={handleChange}
              required
            >

              <option value="">
                Select gender
              </option>

              <option value="Male">
                Male
              </option>

              <option value="Female">
                Female
              </option>

              <option value="Other">
                Other
              </option>

            </select>

          </div>


          {/* LOCATION */}
          <div className="form-group">

            <label>
              Location
            </label>

            <input
              type="text"
              name="location"
              placeholder="Enter city or location"
              value={formData.location}
              onChange={handleChange}
              required
            />

          </div>


          {/* CAREGIVER */}
          <div className="form-group">

            <label>
              Caregiver Name
            </label>

            <input
              type="text"
              name="caregiver_name"
              placeholder="Enter caregiver name"
              value={formData.caregiver_name}
              onChange={handleChange}
              required
            />

          </div>


          {/* REGISTER BUTTON */}
          <button
            type="submit"
            className="primary-form-button"
            disabled={loading}
          >

            {loading
              ? "Registering..."
              : "🧠 Register Patient"}

          </button>

        </form>

      </div>

    </div>
  );
}

export default PatientRegistration;

