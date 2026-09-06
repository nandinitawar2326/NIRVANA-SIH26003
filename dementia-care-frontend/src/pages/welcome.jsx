
import { Link } from "react-router-dom";

function Welcome() {
  return (
    <div className="welcome-page">

      <div className="logo">
        🧠
      </div>

      <h1>Dementia Care Companion</h1>

      <p className="welcome-text">
        A caring companion for everyday life ❤️
      </p>

      <div className="welcome-buttons">

        <Link
          to="/login"
          className="welcome-button"
        >
          🔐 Login
        </Link>

        <Link
          to="/patient-registration"
          className="welcome-button"
        >
          📝 Patient Registration
        </Link>

      </div>

    </div>
  );
}

export default Welcome;

