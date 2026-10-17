
import { Link } from "react-router-dom";

function Family() {
  return (
    <div className="family-page">

      {/* Back Button */}
      <Link to="/home" className="back-button">
        ← Home
      </Link>

      {/* Header */}
      <div className="family-header">

        <div className="family-main-icon">
          👨‍👩‍👧
        </div>

        <h1>My Family</h1>

        <p>
          Stay connected with the people who care about you.
        </p>

      </div>


      {/* Primary Caregiver */}
      <section className="family-card caregiver-card">

        <div className="family-card-title">
          <span>💚</span>
          <h2>Primary Caregiver</h2>
        </div>

        <div className="caregiver-info">

          <div className="caregiver-avatar">
            👩
          </div>

          <div className="caregiver-details">

            <h3>Family Member</h3>

            <p>
              Primary Caregiver
            </p>

            <p>
              📞 +91 XXXXX XXXXX
            </p>

          </div>

          <button
            className="family-call-button"
            onClick={() =>
              alert("Calling your primary caregiver...")
            }
          >
            📞 Call
          </button>

        </div>

      </section>


      {/* Today's Progress */}
      <section className="family-card">

        <div className="family-card-title">
          <span>📊</span>
          <h2>Today's Progress</h2>
        </div>

        <div className="progress-grid">

          <div className="progress-box">
            <span>🧠</span>
            <strong>3</strong>
            <small>Games Completed</small>
          </div>

          <div className="progress-box">
            <span>💊</span>
            <strong>4/4</strong>
            <small>Medicines</small>
          </div>

          <div className="progress-box">
            <span>📖</span>
            <strong>2</strong>
            <small>Activities</small>
          </div>

          <div className="progress-box">
            <span>⏰</span>
            <strong>5</strong>
            <small>Reminders</small>
          </div>

        </div>

      </section>


      {/* Cognitive Status */}
      <section className="family-card">

        <div className="family-card-title">
          <span>🧠</span>
          <h2>Cognitive Status</h2>
        </div>

        <div className="cognitive-status">

          <div className="cognitive-icon">
            🟢
          </div>

          <div>
            <h3>Stable</h3>

            <p>
              Today's cognitive performance is stable.
            </p>
          </div>

        </div>

        <Link
          to="/progress"
          className="family-action-button"
        >
          📊 View Detailed Progress →
        </Link>

      </section>


      {/* Important Updates */}
      <section className="family-card">

        <div className="family-card-title">
          <span>🔔</span>
          <h2>Important Updates</h2>
        </div>

        <div className="family-update">
          <span>💊</span>

          <div>
            <strong>Medicine completed</strong>
            <p>Morning medicine was taken.</p>
          </div>
        </div>


        <div className="family-update">
          <span>🧠</span>

          <div>
            <strong>Brain game completed</strong>
            <p>Memory Match was completed.</p>
          </div>
        </div>


        <div className="family-update">
          <span>🟢</span>

          <div>
            <strong>No safety alerts</strong>
            <p>Everything looks safe right now.</p>
          </div>
        </div>

      </section>


      {/* Family Memories */}
      <section className="family-card">

        <div className="family-card-title">
          <span>💕</span>
          <h2>Family Memories</h2>
        </div>

        <p className="family-description">
          Look at familiar people and important memories.
        </p>

        <div className="memory-preview">

          <div className="memory-photo">
            👨‍👩‍👧
          </div>

          <div className="memory-photo">
            🏡
          </div>

          <div className="memory-photo">
            🎉
          </div>

        </div>

        <Link
          to="/memory-assistance"
          className="family-action-button"
        >
          🧠 View My Memories →
        </Link>

      </section>


      {/* Talk to Family */}
      <section className="family-card talk-card">

        <div className="talk-icon">
          ❤️
        </div>

        <h2>Talk to Your Family</h2>

        <p>
          Your family is always there for you.
        </p>

        <Link
          to="/contacts"
          className="family-talk-button"
        >
          📞 Talk to Someone
        </Link>

      </section>

    </div>
  );
}

export default Family;

