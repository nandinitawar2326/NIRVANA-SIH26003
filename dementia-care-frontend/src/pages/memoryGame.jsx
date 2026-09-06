
import { useState } from "react";
import { Link } from "react-router-dom";

// Patient ID
const USER_ID = "U001";

// Game difficulty
const DIFFICULTY = "medium";

// Available pictures
const allPictures = [
  "🌸",
  "🍎",
  "🍌",
  "🍊",
  "🍇",
  "🌞",
  "🌙",
  "⭐",
  "🌈",
  "🌳",
  "🌻",
  "🍉",
  "🐶",
  "🐱",
  "🐰",
  "🦋",
  "🐘",
  "🐼",
  "🍰",
  "🍕",
];

// Create random cards
function createCards() {
  const shuffledPictures = [...allPictures].sort(
    () => Math.random() - 0.5
  );

  // 6 different pictures = 6 pairs = 12 cards
  const selectedPictures = shuffledPictures.slice(0, 6);

  const pairs = [
    ...selectedPictures,
    ...selectedPictures,
  ];

  return pairs
    .sort(() => Math.random() - 0.5)
    .map((value, index) => ({
      id: index,
      value: value,
    }));
}

function MemoryGame() {
  const [cards, setCards] = useState(createCards());

  const [flipped, setFlipped] = useState([]);

  const [matched, setMatched] = useState([]);

  // Number of pair attempts
  const [attempts, setAttempts] = useState(0);

  // Number of correctly matched pairs
  const [correctAnswers, setCorrectAnswers] = useState(0);

  // Time when the game started
  const [startTime, setStartTime] = useState(Date.now());

  // Final result
  const [gameResult, setGameResult] = useState(null);

  // Prevent clicking while checking two cards
  const [checking, setChecking] = useState(false);


  function handleCardClick(index) {

    // Don't allow clicking while checking
    if (checking) {
      return;
    }

    // Don't click the same card twice
    if (flipped.includes(index)) {
      return;
    }

    // Don't click already matched cards
    if (matched.includes(index)) {
      return;
    }

    // Maximum two cards at a time
    if (flipped.length === 2) {
      return;
    }


    const newFlipped = [
      ...flipped,
      index,
    ];

    setFlipped(newFlipped);


    // Wait until two cards are selected
    if (newFlipped.length === 2) {

      const firstCard = newFlipped[0];

      const secondCard = newFlipped[1];


      // One pair selection = one attempt
      const newAttempts = attempts + 1;

      setAttempts(newAttempts);


      // Check if the cards match
      if (
        cards[firstCard].value ===
        cards[secondCard].value
      ) {

        // Correct answer
        const newCorrectAnswers =
          correctAnswers + 1;

        setCorrectAnswers(newCorrectAnswers);


        const newMatched = [
          ...matched,
          firstCard,
          secondCard,
        ];

        setMatched(newMatched);

        setFlipped([]);


        // Check if game is complete
        if (newMatched.length === cards.length) {

          // Calculate actual time
          const endTime = Date.now();

          const timeTaken = Math.round(
            (endTime - startTime) / 1000
          );


          // Total pairs/questions
          const totalQuestions =
            cards.length / 2;


          // Accuracy
          const accuracy = Math.round(
            (newCorrectAnswers /
              totalQuestions) *
              100
          );


          // Score
          // Score starts with accuracy.
          // Extra attempts reduce the score.
          const score = Math.max(
            0,
            Math.round(
              (newCorrectAnswers /
                newAttempts) *
                100
            )
          );


          // Create ONLY the requested data
          const result = {
            user_id: USER_ID,

            game_type: "memory",

            score: score,

            accuracy: accuracy,

            difficulty: DIFFICULTY,

            time_taken: timeTaken,

            attempts: newAttempts,

            correct_answers: newCorrectAnswers,

            total_questions: totalQuestions,
          };


          setGameResult(result);
        }

      } else {

        // Wrong pair
        setChecking(true);


        // Show cards for 1 second
        setTimeout(() => {

          setFlipped([]);

          setChecking(false);

        }, 1000);
      }
    }
  }


  function restartGame() {

    // Create completely new random cards
    setCards(createCards());

    // Reset game
    setFlipped([]);

    setMatched([]);

    setAttempts(0);

    setCorrectAnswers(0);

    // Start a completely new timer
    setStartTime(Date.now());

    // Remove previous result
    setGameResult(null);

    setChecking(false);
  }


  // =========================
  // GAME FINISHED
  // =========================

  if (gameResult) {

    return (
      <div className="game-page">

        <Link
          to="/games"
          className="back-button"
        >
          ← Brain Games
        </Link>


        <h1>🧩 Memory Match</h1>


        <div className="success-message">

          <h2>🎉 Well Done!</h2>

          <p>
            You found all the matching pictures!
          </p>


          <h2>
            Score: {gameResult.score}
          </h2>


          <p>
            🎯 Accuracy:{" "}
            {gameResult.accuracy}%
          </p>


          <p>
            ⏱️ Time Taken:{" "}
            {gameResult.time_taken} seconds
          </p>


          <p>
            🎮 Attempts:{" "}
            {gameResult.attempts}
          </p>


          <p>
            ✅ Correct Answers:{" "}
            {gameResult.correct_answers}
          </p>


          <p>
            📋 Total Questions:{" "}
            {gameResult.total_questions}
          </p>


          <p>
            🎚️ Difficulty:{" "}
            {gameResult.difficulty}
          </p>

        </div>


        {/* JSON DATA */}
        <div className="backend-data">

          <h2>
            📤 Game Data
          </h2>

          <pre>
            {JSON.stringify(
              gameResult,
              null,
              2
            )}
          </pre>

        </div>


        <button
          className="restart-button"
          onClick={restartGame}
        >
          🔄 New Game
        </button>

      </div>
    );
  }


  // =========================
  // GAME SCREEN
  // =========================

  return (
    <div className="game-page">

      <Link
        to="/games"
        className="back-button"
      >
        ← Brain Games
      </Link>


      <h1>🧩 Memory Match</h1>


      <p className="game-instruction">
        Find the two matching pictures.
      </p>


      <h2>
        Attempts: {attempts}
      </h2>


      <div className="memory-grid">

        {cards.map((card, index) => {

          const isFlipped =
            flipped.includes(index) ||
            matched.includes(index);


          return (
            <button
              key={card.id}
              className={`memory-card ${
                isFlipped
                  ? "flipped"
                  : ""
              }`}
              onClick={() =>
                handleCardClick(index)
              }
              disabled={checking}
            >
              {isFlipped
                ? card.value
                : "❓"}
            </button>
          );
        })}

      </div>


      <div className="game-live-stats">

        <p>
          ✅ Correct Pairs:{" "}
          {correctAnswers}
        </p>

        <p>
          ❌ Wrong Attempts:{" "}
          {attempts - correctAnswers}
        </p>

      </div>

    </div>
  );
}

export default MemoryGame;
