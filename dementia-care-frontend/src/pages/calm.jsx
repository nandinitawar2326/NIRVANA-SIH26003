
import { useEffect, useRef, useState } from "react";
import { Link } from "react-router-dom";

function Calm() {
  const [duration, setDuration] = useState(1);
  const [timeLeft, setTimeLeft] = useState(60);
  const [isRunning, setIsRunning] = useState(false);
  const [phase, setPhase] = useState("Ready");
  const [sound, setSound] = useState("None");

  const elapsedRef = useRef(0);
  const timerRef = useRef(null);

  // Speak using browser voice
  function speak(text) {
    if (!("speechSynthesis" in window)) {
      return;
    }

    window.speechSynthesis.cancel();

    const message = new SpeechSynthesisUtterance(text);

    message.lang = "en-IN";
    message.rate = 0.85;
    message.pitch = 1;
    message.volume = 1;

    window.speechSynthesis.speak(message);
  }

  // Voice instruction for each breathing phase
  function speakPhase(currentPhase) {
    if (currentPhase === "Breathe In") {
      speak("Breathe in slowly");
    }

    if (currentPhase === "Hold") {
      speak("Hold gently");
    }

    if (currentPhase === "Breathe Out") {
      speak("Breathe out slowly");
    }
  }

  // Start selected session
  function startSession(selectedDuration) {
    // Stop any previous voice
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }

    // Clear old timer
    if (timerRef.current) {
      clearInterval(timerRef.current);
    }

    const totalSeconds = selectedDuration * 60;

    setDuration(selectedDuration);
    setTimeLeft(totalSeconds);
    setIsRunning(true);
    setPhase("Breathe In");

    elapsedRef.current = 0;

    // Start voice immediately
    setTimeout(() => {
      speak("Breathe in slowly");
    }, 100);

    // Start timer
    timerRef.current = setInterval(() => {
      elapsedRef.current += 1;

      const elapsed = elapsedRef.current;

      // Update remaining time
      setTimeLeft(totalSeconds - elapsed);

      // Check session completion
      if (elapsed >= totalSeconds) {
        clearInterval(timerRef.current);
        timerRef.current = null;

        setIsRunning(false);
        setPhase("Complete");

        if ("speechSynthesis" in window) {
          window.speechSynthesis.cancel();
        }

        speak("Wonderful. Your breathing session is complete.");

        return;
      }

      // 12 second breathing cycle
      const cycleTime = elapsed % 12;

      let newPhase;

      if (cycleTime < 4) {
        newPhase = "Breathe In";
      } else if (cycleTime < 6) {
        newPhase = "Hold";
      } else {
        newPhase = "Breathe Out";
      }

      // Only speak when phase changes
      setPhase((previousPhase) => {
        if (previousPhase !== newPhase) {
          speakPhase(newPhase);
        }

        return newPhase;
      });

    }, 1000);
  }

  // Pause
  function pauseSession() {
    setIsRunning(false);

    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }

    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }

    setPhase("Paused");
  }

  // Start again
  function resetSession() {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }

    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }

    elapsedRef.current = 0;

    setTimeLeft(duration * 60);
    setIsRunning(false);
    setPhase("Ready");
  }

  // Cleanup when leaving page
  useEffect(() => {
    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
      }

      if ("speechSynthesis" in window) {
        window.speechSynthesis.cancel();
      }
    };
  }, []);

  // Format timer
  function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;

    return `${String(minutes).padStart(2, "0")}:${String(
      remainingSeconds
    ).padStart(2, "0")}`;
  }

  return (
    <div className="calm-page">

      <Link to="/home" className="back-button">
        ← Home
      </Link>

      {/* HEADER */}
      <div className="calm-header">

        <div className="calm-main-icon">
          🌿
        </div>

        <h1>Calm & Breathe</h1>

        <p>
          Your AI voice assistant will guide you.
        </p>

      </div>

      {/* AI MESSAGE */}
      <div className="ai-breathe-message">

        <div className="ai-breathe-icon">
          🤖
        </div>

        <div>

          <strong>
            AI Breathing Assistant
          </strong>

          <p>
            Choose a session below. I will guide
            you with my voice.
          </p>

        </div>

      </div>

      {/* COMFORT MESSAGE */}
      <div className="comfort-message">

        <div>
          ❤️
        </div>

        <div>

          <strong>
            You are safe.
          </strong>

          <p>
            Take your time. There is no need to hurry.
          </p>

        </div>

      </div>

      {/* BREATHING CARD */}
      <section className="breathing-card">

        <h2>
          🌬️ Guided Breathing
        </h2>

        <p className="breathing-instruction">
          Choose 1, 3 or 5 minutes to begin.
        </p>

        {/* BREATHING CIRCLE */}
        <div
          className={`breathing-circle ${
            isRunning
              ? phase === "Breathe In"
                ? "breathing-in"
                : phase === "Breathe Out"
                ? "breathing-out"
                : "breathing-hold"
              : ""
          }`}
        >

          <div className="breathing-circle-content">

            <span className="breathing-icon">
              🌬️
            </span>

            <strong>
              {phase}
            </strong>

            {isRunning && (
              <small>

                {phase === "Breathe In" &&
                  "Slowly breathe in"}

                {phase === "Hold" &&
                  "Hold gently"}

                {phase === "Breathe Out" &&
                  "Slowly breathe out"}

              </small>
            )}

          </div>

        </div>

        {/* TIMER */}
        <div className="breathing-timer">
          {formatTime(timeLeft)}
        </div>

        {/* VOICE STATUS */}
        {isRunning && (
          <div className="voice-status">
            🔊 AI Assistant is speaking
          </div>
        )}

        {/* SESSION BUTTONS */}
        <div className="duration-section">

          <h3>
            Choose Session
          </h3>

          <div className="duration-buttons">

            <button
              className={
                duration === 1 && isRunning
                  ? "duration-active"
                  : ""
              }
              onClick={() => startSession(1)}
            >
              🌱 1 Minute
            </button>

            <button
              className={
                duration === 3 && isRunning
                  ? "duration-active"
                  : ""
              }
              onClick={() => startSession(3)}
            >
              🌿 3 Minutes
            </button>

            <button
              className={
                duration === 5 && isRunning
                  ? "duration-active"
                  : ""
              }
              onClick={() => startSession(5)}
            >
              🌳 5 Minutes
            </button>

          </div>

        </div>

        {/* PAUSE / RESET */}
        <div className="breathing-controls">

          {isRunning && (
            <button
              className="pause-breathe-button"
              onClick={pauseSession}
            >
              ⏸ Pause
            </button>
          )}

          {(phase === "Paused" || phase === "Complete") && (
            <button
              className="reset-breathe-button"
              onClick={resetSession}
            >
              🔄 Start Again
            </button>
          )}

        </div>

        {/* COMPLETE MESSAGE */}
        {phase === "Complete" && (
          <div className="session-complete">

            🌸 Wonderful! You completed your breathing session.

          </div>
        )}

      </section>

      {/* CALMING SOUNDS */}
      <section className="calm-card">

        <div className="calm-card-title">

          <span>
            🎵
          </span>

          <h2>
            Calming Sounds
          </h2>

        </div>

        <p>
          Choose a peaceful sound for your session.
        </p>

        <div className="sound-buttons">

          <button
            className={
              sound === "Rain"
                ? "sound-active"
                : ""
            }
            onClick={() => setSound("Rain")}
          >
            🌧️
            <span>
              Rain
            </span>
          </button>

          <button
            className={
              sound === "Ocean"
                ? "sound-active"
                : ""
            }
            onClick={() => setSound("Ocean")}
          >
            🌊
            <span>
              Ocean
            </span>
          </button>

          <button
            className={
              sound === "Birds"
                ? "sound-active"
                : ""
            }
            onClick={() => setSound("Birds")}
          >
            🐦
            <span>
              Birds
            </span>
          </button>

          <button
            className={
              sound === "None"
                ? "sound-active"
                : ""
            }
            onClick={() => setSound("None")}
          >
            🔇
            <span>
              None
            </span>
          </button>

        </div>

        {sound !== "None" && (
          <div className="selected-sound">
            🎵 {sound} selected
          </div>
        )}

      </section>

      {/* CALM ACTIVITIES */}
      <section className="calm-card">

        <div className="calm-card-title">

          <span>
            🧘
          </span>

          <h2>
            Calm Activities
          </h2>

        </div>

        <div className="calm-activities">

          <div className="calm-activity">

            <div>
              🌸
            </div>

            <h3>
              Look at Flowers
            </h3>

            <p>
              Take a quiet moment to enjoy nature.
            </p>

          </div>

          <div className="calm-activity">

            <div>
              ☁️
            </div>

            <h3>
              Watch the Clouds
            </h3>

            <p>
              Relax and observe the sky peacefully.
            </p>

          </div>

          <div className="calm-activity">

            <div>
              🙏
            </div>

            <h3>
              Quiet Moment
            </h3>

            <p>
              Sit comfortably and enjoy a peaceful moment.
            </p>

          </div>

        </div>

      </section>

      {/* BOTTOM MESSAGE */}
      <div className="calm-bottom-message">

        <div>
          💚
        </div>

        <h2>
          One breath at a time.
        </h2>

        <p>
          You are doing great. Keep going.
        </p>

      </div>

    </div>
  );
}

export default Calm;

