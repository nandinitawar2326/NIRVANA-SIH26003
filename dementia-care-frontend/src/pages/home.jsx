import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="home-page">

      {/* Header */}
      <header className="home-header">
        <div>
          <h1>Good Morning 👋</h1>
          <p>Hello! 🌸 Let's have a happy and healthy day.</p>
        </div>

        <div className="profile-icon">
          👤
        </div>
      </header>


      {/* Next Activity */}
      <section className="next-activity">

        <h2>Next Activity</h2>

        <div className="medicine-card">

          <div className="medicine-icon">
            💊
          </div>

          <div className="medicine-info">
            <h3>Morning Medicine</h3>
            <p>Take your medicine</p>
            <span>⏰ 8:00 AM</span>
          </div>

          <Link to="/medicine" className="take-button">
            TAKE
          </Link>

        </div>

      </section>


      {/* Main Features */}
      <section className="features">

        <h2>What would you like to do?</h2>

        <div className="feature-grid">

          <Link to="/games" className="feature-card">
            <span>🧠</span>
            <strong>Brain Games</strong>
            <small>Exercise your memory</small>
          </Link>


          <Link to="/garden" className="feature-card">
            <span>🌱</span>
            <strong>My Garden</strong>
            <small>See your garden grow</small>
          </Link>


          <Link to="/stories" className="feature-card">
            <span>📖</span>
            <strong>Stories</strong>
            <small>Listen to familiar stories</small>
          </Link>


          <Link to="/family" className="feature-card">
            <span>👨‍👩‍👧</span>
            <strong>Family</strong>
            <small>See your loved ones</small>
          </Link>


          <Link to="/calm" className="feature-card">
            <span>🧘</span>
            <strong>Calm & Breathe</strong>
            <small>Take a peaceful moment</small>
          </Link>


          <Link to="/contacts" className="feature-card">
            <span>❤️</span>
            <strong>Talk to Someone</strong>
            <small>Connect with family</small>
          </Link>


          <Link to="/safety" className="feature-card">
            <span>🛡️</span>
            <strong>Safety</strong>
            <small>Check your safety</small>
          </Link>

        </div>

      </section>


      {/* Voice Assistant */}
      <section className="voice-section">

        <button className="voice-button">
          🎤
          <span>
            <strong>What should I do now?</strong>
            <small>Tap to ask your assistant</small>
          </span>
        </button>

      </section>

    </div>
  );
}

export default Home;