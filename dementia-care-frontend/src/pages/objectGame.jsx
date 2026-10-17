
import { useState } from "react";
import { Link } from "react-router-dom";

const USER_ID = "U001";
const DIFFICULTY = "medium";

const questions = [
  {
    target: "🍎",
    options: ["🍌", "🍎", "🍊", "🍇"],
  },
  {
    target: "🌸",
    options: ["🌳", "🌻", "🌸", "🌹"],
  },
  {
    target: "🐱",
    options: ["🐶", "🐱", "🐰", "🐯"],
  },
  {
    target: "☀️",
    options: ["🌙", "⭐", "☁️", "☀️"],
  },
  {
    target: "🍰",
    options: ["🍕", "🍔", "🍰", "🍩"],
  },
];

function ObjectGame() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selected, setSelected] = useState(null);
  const [finished, setFinished] = useState(false);

  const [attempts, setAttempts] = useState(0);
  const [correctAnswers, setCorrectAnswers] = useState(0);

  const [startTime, setStartTime] = useState(Date.now());
  const [gameResult, setGameResult] = useState(null);

  const question = questions[currentQuestion];

  function selectObject(object) {
    if (selected !== null) return;

    setSelected(object);

    const newAttempts = attempts + 1;
    setAttempts(newAttempts);

    let newCorrectAnswers = correctAnswers;

    if (object === question.target) {
      newCorrectAnswers = correctAnswers + 1;
      setCorrectAnswers(newCorrectAnswers);
    }

    setTimeout(() => {
      if (currentQuestion + 1 < questions.length) {
        setCurrentQuestion((previousQuestion) => previousQuestion + 1);
        setSelected(null);
      } else {
        const endTime = Date.now();

        const timeTaken = Math.round(
          (endTime - startTime) / 1000
        );

        const totalQuestions = questions.length;

        const accuracy = Math.round(
          (newCorrectAnswers / newAttempts) * 100
        );

        const score = Math.round(
          (newCorrectAnswers / totalQuestions) * 100
        );

        const result = {
          user_id: USER_ID,
          game_type: "object",
          score: score,
          accuracy: accuracy,
          difficulty: DIFFICULTY,
          time_taken: timeTaken,
          attempts: newAttempts,
          correct_answers: newCorrectAnswers,
          total_questions: totalQuestions,
        };

        setGameResult(result);
        setFinished(true);
      }
    }, 1000);
  }

  function restartGame() {
    setCurrentQuestion(0);
    setSelected(null);
    setFinished(false);

    setAttempts(0);
    setCorrectAnswers(0);

    setStartTime(Date.now());
    setGameResult(null);
  }

  if (finished && gameResult) {
    return (
      <div className="game-page">

        <Link to="/games" className="back-button">
          ← Brain Games
        </Link>

        <h1>🌸 Find the Same</h1>

        <div className="success-message">
          <h2>🎉 Well Done!</h2>

          <h2>Score: {gameResult.score}</h2>

          <p>🎯 Accuracy: {gameResult.accuracy}%</p>

          <p>
            ⏱️ Time Taken: {gameResult.time_taken} seconds
          </p>

          <p>
            🎮 Attempts: {gameResult.attempts}
          </p>

          <p>
            ✅ Correct Answers: {gameResult.correct_answers}
          </p>

          <p>
            📋 Total Questions: {gameResult.total_questions}
          </p>

          <p>
            🎚️ Difficulty: {gameResult.difficulty}
          </p>
        </div>

        <div className="backend-data">
          <h2>📤 Game Data</h2>

          <pre>
            {JSON.stringify(gameResult, null, 2)}
          </pre>
        </div>

        <button
          className="restart-button"
          onClick={restartGame}
        >
          🔄 Play Again
        </button>

      </div>
    );
  }

  return (
    <div className="game-page">

      <Link to="/games" className="back-button">
        ← Brain Games
      </Link>

      <h1>🌸 Find the Same</h1>

      <p className="game-instruction">
        Find the object that looks the same.
      </p>

      <p className="question-number">
        Question {currentQuestion + 1} of {questions.length}
      </p>

      <div className="target-object">
        <p>Find this:</p>
        <div>{question.target}</div>
      </div>

      <div className="object-options">
        {question.options.map((object, index) => (
          <button
            key={index}
            className={`object-option ${
              selected === object
                ? object === question.target
                  ? "correct"
                  : "wrong"
                : ""
            }`}
            onClick={() => selectObject(object)}
          >
            {object}
          </button>
        ))}
      </div>

      <div className="game-live-stats">
        <p>🎮 Attempts: {attempts}</p>
        <p>✅ Correct Answers: {correctAnswers}</p>
      </div>

    </div>
  );
}

export default ObjectGame;
