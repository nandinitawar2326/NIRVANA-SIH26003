
import { useState } from "react";
import { Link } from "react-router-dom";

// Different patterns
const patterns = [
  {
    sequence: ["🔴", "🔵", "🔴", "🔵"],
    answer: "🔴",
    options: ["🔴", "🟢", "🟡"],
  },
  {
    sequence: ["🌸", "🌼", "🌸", "🌼"],
    answer: "🌸",
    options: ["🌸", "🌹", "🌻"],
  },
  {
    sequence: ["🍎", "🍌", "🍎", "🍌"],
    answer: "🍎",
    options: ["🍊", "🍎", "🍇"],
  },
  {
    sequence: ["⭐", "🌙", "⭐", "🌙"],
    answer: "⭐",
    options: ["☀️", "⭐", "🌈"],
  },
  {
    sequence: ["🐶", "🐱", "🐶", "🐱"],
    answer: "🐶",
    options: ["🐰", "🐶", "🐯"],
  },
  {
    sequence: ["🟢", "🟡", "🔵", "🟢", "🟡"],
    answer: "🔵",
    options: ["🔴", "🔵", "🟣"],
  },
  {
    sequence: ["🍎", "🍎", "🍌", "🍎", "🍎"],
    answer: "🍌",
    options: ["🍊", "🍌", "🍇"],
  },
  {
    sequence: ["☀️", "🌙", "⭐", "☀️", "🌙"],
    answer: "⭐",
    options: ["⭐", "🌈", "☁️"],
  },
  {
    sequence: ["🌳", "🌸", "🌳", "🌸"],
    answer: "🌳",
    options: ["🌳", "🌻", "🌲"],
  },
  {
    sequence: ["🐱", "🐶", "🐰", "🐱", "🐶"],
    answer: "🐰",
    options: ["🐯", "🐰", "🐹"],
  },
];

// Pick 5 random questions
function getRandomQuestions() {
  return [...patterns]
    .sort(() => Math.random() - 0.5)
    .slice(0, 5);
}

function PatternGame() {

  const [questions, setQuestions] = useState(
    getRandomQuestions()
  );

  const [currentQuestion, setCurrentQuestion] = useState(0);

  const [score, setScore] = useState(0);

  const [selected, setSelected] = useState(null);

  const [finished, setFinished] = useState(false);


  const question = questions[currentQuestion];


  // When user selects an answer
  function selectAnswer(answer) {

    // Prevent selecting multiple answers
    if (selected !== null) {
      return;
    }

    setSelected(answer);

    // Correct answer
    if (answer === question.answer) {
      setScore((previousScore) => previousScore + 1);
    }

    // Move to next question after 1 second
    setTimeout(() => {

      if (currentQuestion + 1 < questions.length) {

        setCurrentQuestion(
          (previousQuestion) => previousQuestion + 1
        );

        setSelected(null);

      } else {

        setFinished(true);

      }

    }, 1000);
  }


  // Start a completely new game
  function restartGame() {

    setQuestions(getRandomQuestions());

    setCurrentQuestion(0);

    setScore(0);

    setSelected(null);

    setFinished(false);
  }


  // Final screen
  if (finished) {

    return (
      <div className="game-page">

        <Link to="/games" className="back-button">
          ← Brain Games
        </Link>

        <h1>🔢 Complete the Pattern</h1>

        <div className="success-message">

          <h2>🎉 Excellent!</h2>

          <p>
            You completed the game!
          </p>

          <h2>
            {score} / {questions.length}
          </h2>

          {score === questions.length && (
            <p>🌟 Perfect Score!</p>
          )}

          {score >= 3 && score < questions.length && (
            <p>👏 Very Good!</p>
          )}

          {score < 3 && (
            <p>😊 Good Try! Keep practicing!</p>
          )}

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


  // Game screen
  return (
    <div className="game-page">

      <Link to="/games" className="back-button">
        ← Brain Games
      </Link>

      <h1>🔢 Complete the Pattern</h1>

      <p className="game-instruction">
        Look carefully. What should come next?
      </p>

      <p className="question-number">
        Question {currentQuestion + 1} of {questions.length}
      </p>


      {/* Pattern */}
      <div className="pattern-box">

        {question.sequence.map((item, index) => (
          <span key={index}>
            {item}{" "}
          </span>
        ))}

        <span>❓</span>

      </div>


      {/* Answer options */}
      <div className="pattern-options">

        {question.options.map((option, index) => {

          let resultClass = "";

          if (selected === option) {

            if (option === question.answer) {
              resultClass = "correct";
            } else {
              resultClass = "wrong";
            }

          }

          return (
            <button
              key={index}
              className={`pattern-option ${resultClass}`}
              onClick={() => selectAnswer(option)}
            >
              {option}
            </button>
          );

        })}

      </div>


      <p className="score">
        Score: {score}
      </p>

    </div>
  );
}

export default PatternGame;

