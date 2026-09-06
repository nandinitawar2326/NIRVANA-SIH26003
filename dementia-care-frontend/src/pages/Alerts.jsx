
import { useState } from "react";
import { Link } from "react-router-dom";

function Alerts() {
  const [alerts, setAlerts] = useState([
    {
      id: 1,
      patient_id: "U001",
      alert_type: "Fall Detection",
      message: "Possible fall detected.",
      location: "Patient's current location",
      status: "Active",
    },
  ]);

  function resolveAlert(id) {
    setAlerts(
      alerts.map((alert) =>
        alert.id === id
          ? { ...alert, status: "Resolved" }
          : alert
      )
    );
  }

  return (
    <div className="alerts-page">

      <Link to="/dashboard" className="back-button">
        ← Dashboard
      </Link>

      <div className="alerts-header">
        <div className="form-icon">🚨</div>

        <h1>Emergency Alerts</h1>

        <p>
          Monitor safety alerts for your patients.
        </p>
      </div>

      <div className="alerts-list">

        {alerts.length === 0 ? (
          <div className="no-alerts">
            <div>✅</div>
            <h2>No Emergency Alerts</h2>
            <p>Everything looks safe.</p>
          </div>
        ) : (
          alerts.map((alert) => (
            <div
              className={`alert-card ${
                alert.status === "Active"
                  ? "alert-active"
                  : "alert-resolved"
              }`}
              key={alert.id}
            >

              <div className="alert-top">

                <div>
                  <h2>🚨 {alert.alert_type}</h2>

                  <p>
                    Patient ID: <strong>{alert.patient_id}</strong>
                  </p>
                </div>

                <span className="alert-status">
                  {alert.status}
                </span>

              </div>

              <div className="alert-information">

                <p>
                  <strong>Message:</strong>
                  <br />
                  {alert.message}
                </p>

                <p>
                  <strong>📍 Location:</strong>
                  <br />
                  {alert.location}
                </p>

              </div>

              {alert.status === "Active" && (
                <button
                  className="resolve-button"
                  onClick={() => resolveAlert(alert.id)}
                >
                  ✓ Mark as Resolved
                </button>
              )}

            </div>
          ))
        )}

      </div>

    </div>
  );
}

export default Alerts;

