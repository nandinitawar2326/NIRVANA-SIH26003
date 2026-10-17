
import { useState } from "react";
import { Link } from "react-router-dom";

function Safety() {
  const [sosSent, setSosSent] = useState(false);

  const [checklist, setChecklist] = useState({
    door: false,
    medicine: false,
    water: false,
    emergency: false,
  });

  function sendSOS() {
    setSosSent(true);

    alert("Emergency alert sent to your caregiver!");
  }

  function toggleChecklist(item) {
    setChecklist({
      ...checklist,
      [item]: !checklist[item],
    });
  }

  return (
    <div className="safety-page">

      {/* Back Button */}
      <Link to="/home" className="back-button">
        ← Home
      </Link>

      {/* Header */}
      <div className="safety-header">

        <div className="safety-icon">
          🛡️
        </div>

        <h1>Safety</h1>

        <p>
          Stay safe and connected with your loved ones.
        </p>

        <div className="safe-status">
          🟢 You are safe right now
        </div>

      </div>


      {/* Emergency SOS */}
      <section className="safety-card sos-card">

        <div className="safety-card-icon">
          🚨
        </div>

        <h2>Emergency SOS</h2>

        <p>
          Need immediate help? Press the button below
          to alert your caregiver.
        </p>

        <button
          className="sos-button"
          onClick={sendSOS}
        >
          🚨 EMERGENCY SOS
        </button>

        {sosSent && (
          <div className="sos-success">
            ✅ Emergency alert sent to your caregiver.
          </div>
        )}

      </section>


      {/* Safe Zone */}
      <section className="safety-card">

        <div className="safety-card-title">
          <span>📍</span>
          <h2>Safe Zone</h2>
        </div>

        <div className="safe-zone-box">

          <div className="safe-zone-icon">
            🏠
          </div>

          <div>
            <h3>Home</h3>

            <p>
              You are currently inside your registered
              safe zone.
            </p>

            <span className="safe-zone-status">
              🟢 Safe Zone Active
            </span>
          </div>

        </div>

        <p className="small-info">
          If the patient leaves the safe zone,
          the caregiver can be notified.
        </p>

      </section>


      {/* Emergency Alerts */}
      <section className="safety-card">

        <div className="safety-card-title">
          <span>🔔</span>
          <h2>Emergency Alerts</h2>
        </div>

        <div className="alert-preview">

          <div className="alert-preview-icon">
            🚨
          </div>

          <div>
            <h3>No Active Alerts</h3>

            <p>
              There are no emergency alerts right now.
            </p>
          </div>

        </div>

        <Link
          to="/alerts"
          className="view-alerts-button"
        >
          View All Alerts →
        </Link>

      </section>


      {/* Emergency Contacts */}
      <section className="safety-card">

        <div className="safety-card-title">
          <span>📞</span>
          <h2>Emergency Contacts</h2>
        </div>

        <div className="contact-item">

          <div className="contact-icon">
            👩
          </div>

          <div className="contact-info">
            <h3>Family Member</h3>
            <p>Primary Caregiver</p>
          </div>

          <button
            className="call-button"
            onClick={() =>
              alert("Calling your family member...")
            }
          >
            📞 Call
          </button>

        </div>


        <div className="contact-item">

          <div className="contact-icon">
            👨‍⚕️
          </div>

          <div className="contact-info">
            <h3>Doctor</h3>
            <p>Assigned Doctor</p>
          </div>

          <button
            className="call-button"
            onClick={() =>
              alert("Calling your doctor...")
            }
          >
            📞 Call
          </button>

        </div>

      </section>


      {/* Safety Checklist */}
      <section className="safety-card">

        <div className="safety-card-title">
          <span>🔐</span>
          <h2>Safety Checklist</h2>
        </div>

        <p className="checklist-description">
          Complete your daily safety checks.
        </p>


        <div
          className="checklist-item"
          onClick={() => toggleChecklist("door")}
        >
          <span className="checkbox">
            {checklist.door ? "☑️" : "⬜"}
          </span>

          <span>
            Main door checked
          </span>
        </div>


        <div
          className="checklist-item"
          onClick={() => toggleChecklist("medicine")}
        >
          <span className="checkbox">
            {checklist.medicine ? "☑️" : "⬜"}
          </span>

          <span>
            Medicines checked
          </span>
        </div>


        <div
          className="checklist-item"
          onClick={() => toggleChecklist("water")}
        >
          <span className="checkbox">
            {checklist.water ? "☑️" : "⬜"}
          </span>

          <span>
            Water bottle nearby
          </span>
        </div>


        <div
          className="checklist-item"
          onClick={() => toggleChecklist("emergency")}
        >
          <span className="checkbox">
            {checklist.emergency ? "☑️" : "⬜"}
          </span>

          <span>
            Emergency contact available
          </span>
        </div>

      </section>

    </div>
  );
}

export default Safety;

