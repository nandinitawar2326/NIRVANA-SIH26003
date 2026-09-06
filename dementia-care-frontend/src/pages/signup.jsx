
import { Link } from "react-router-dom";

function Signup() {
  return (
    <div className="auth-page">

      <div className="auth-logo">
        🧠
      </div>

      <h1>Create Account ✨</h1>

      <p>Let's get you started</p>

      <div className="auth-box">

        <label>Username</label>

        <input
          type="text"
          placeholder="Create a username"
        />

        <label>Password</label>

        <input
          type="password"
          placeholder="Create a password"
        />

        <label>Confirm Password</label>

        <input
          type="password"
          placeholder="Confirm your password"
        />

        {/* Go to Patient Registration */}
        <Link
          to="/patient-registration"
          className="auth-button"
        >
          Continue to Registration →
        </Link>

      </div>

      <p>
        Already have an account?
        <Link to="/login"> Login</Link>
      </p>

    </div>
  );
}

export default Signup;

