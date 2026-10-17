
import { Link } from "react-router-dom";

function Games() {
  return (
    <div className="games-page">

      {/* Back to Home */}
      <Link to="/home" className="back-button">
        ← Home
      </Link>

      {/* Page Heading */}
      <h1>🧠 Brain Games</h1>

      <p className="games-subtitle">
        Let's have some fun and exercise your memory!
      </p>

      {/* Games */}
      <div className="games-grid">

        {/* Memory Match */}
        <Link to="/games/memory" className="game-card">
          <div className="game-icon">🧩</div>

          <h2>Memory Match</h2>

          <p>
            Find the two matching pictures.
          </p>

          <span>
            Play Game →
          </span>
        </Link>


        {/* Find the Same */}
        <Link to="/games/object" className="game-card">
          <div className="game-icon">🌸</div>

          <h2>Find the Same</h2>

          <p>
            Find the object that looks the same.
          </p>

          <span>
            Play Game →
          </span>
        </Link>


        {/* Complete the Pattern */}
        <Link to="/games/pattern" className="game-card">
          <div className="game-icon">🔢</div>

          <h2>Complete the Pattern</h2>

          <p>
            Look carefully and choose what comes next.
          </p>

          <span>
            Play Game →
          </span>
        </Link>


        {/* Who Is This */}
        <Link to="/games/family" className="game-card">
          <div className="game-icon">👨‍👩‍👧</div>

          <h2>Who Is This?</h2>

          <p>
            Recognize someone you know.
          </p>

          <span>
            Play Game →
          </span>
        </Link>

      </div>

    </div>
  );
}

export default Games;


