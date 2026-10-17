
import { useState } from "react";
import { Link } from "react-router-dom";

// Family members
const familyMembers = [
  {
    person: "👩",
    name: "Daughter",
  },
  {
    person: "👨",
    name: "Son",
  },
  {
    person: "👶",
    name: "Grandchild",
  },
  {
    person: "👵",
    name: "Grandmother",
  },
  {
    person: "👴",
    name: "Grandfather",
  },
  {
    person: "👩‍🦱",
    name: "Sister",
  },
  {
    person: "👨‍🦱",
    name: "Brother",
  },
  {
    person: "❤️",
    name: "Caregiver",
  },
];

// Shuffle array
function shuffleArray(array) {
  return [...array].sort(() => Math.random() - 0.5);
}

// Create random questions
function createQuestions() {
  const selectedMembers = shuffleArray(familyMembers).slice(0, 5);

  return selectedMembers.map((member) => {
    // Create 3 random options including correct answer
    const otherMembers = familyMembers.filter(
      (item) => item.name !== member.name
    );

    const randomOthers = shuffleArray(otherMembers).slice(0, 2);

    const options = shuffleArray([
      member.name,
      randomOthers[0].name,
      randomOthers[1].name,
    ]);

    return {
      person: member.person,
      name: member.name,
      options: options,
    };
  });
}

function FamilyGame() {
  const [questions, setQuestions] = useState(
    createQuestions()
  );

  const [currentQuestion, setCurrentQuestion] = useState(0);

  const [score, setScore] = useState(0);

  const [selected, setSelected] = useState(null);

  const [finished, setFinished] = useState(false);

  const question = questions[currentQuestion];

  function selectAnswer(answer) {
    if (selected !== null) {
      return;
    }

    setSelected(answer);

    if (answer === question.name) {
      setScore((previousScore) => previousScore + 1);
    }

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

  function restartGame() {
    // Generate completely new random questions
    setQuestions(createQuestions());

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

        <h1>👨‍👩‍👧 Who Is This?</h1>

        <div className="success-message">

          <h2>❤️ Wonderful!</h2>

          <p>
            You recognized your family members.
          </p>

          <div className="family-final-score">
            {score} / {questions.length}
          </div>

          {score === questions.length && (
            <p>🌟 Perfect! You recognized everyone!</p>
          )}

          {score >= 3 &&
            score < questions.length && (
              <p>👏 Very Good! Keep practicing!</p>
            )}

          {score < 3 && (
            <p>😊 Good Try! Let's try again.</p>
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

  return (
    <div className="game-page">

      <Link to="/games" className="back-button">
        ← Brain Games
      </Link>

      <h1>👨‍👩‍👧 Who Is This?</h1>

      <p className="game-instruction">
        Who is this person?
      </p>

      <p className="question-number">
        Person {currentQuestion + 1} of {questions.length}
      </p>

      {/* LARGE PERSON IMAGE */}
      <div className="family-person-large">

        <div className="family-person-emoji">
          {question.person}
        </div>

      </div>

      {/* ANSWER OPTIONS */}
      <div className="family-options">

        {question.options.map((option, index) => {

          let resultClass = "";

          if (selected === option) {
            if (option === question.name) {
              resultClass = "correct";
            } else {
              resultClass = "wrong";
            }
          }

          return (
            <button
              key={index}
              className={`family-option ${resultClass}`}
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

export default FamilyGame;

