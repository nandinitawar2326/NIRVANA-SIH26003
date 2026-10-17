import { Link } from "react-router-dom";

function Login() {
  return (
    <div className="auth-page">

      <div className="auth-logo">
        🧠
      </div>

      <h1>Welcome Back 👋</h1>

      <p>Please login to continue</p>

      <div className="auth-box">

        <label>Username</label>

        <input
          type="text"
          placeholder="Enter your username"
        />

        <label>Password</label>

        <input
          type="password"
          placeholder="Enter your password"
        />

        <Link to="/home" className="auth-button">
          Login
        </Link>

      </div>

      <p>
        Don't have an account?
        <Link to="/signup"> Sign Up</Link>
      </p>

    </div>
  );
}

export default Login;