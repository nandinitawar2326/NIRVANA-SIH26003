
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Authentication
import Welcome from "./pages/Welcome";
import Login from "./pages/Login";

// Registration
import PatientRegistration from "./pages/PatientRegistration";
import AddCaregiver from "./pages/AddCaregiver";

// Main Pages
import Home from "./pages/Home";
import Medicine from "./pages/Medicine";
import Games from "./pages/Games";
import Garden from "./pages/Garden";
import Stories from "./pages/Stories";
import Family from "./pages/Family";
import Calm from "./pages/Calm";
import Contacts from "./pages/Contacts";
import Safety from "./pages/Safety";

// Caregiver / Backend Modules
import Reminders from "./pages/Reminders";
import MemoryAssistance from "./pages/MemoryAssistance";
import Alerts from "./pages/Alerts";

// Games
import MemoryGame from "./pages/MemoryGame";
import ObjectGame from "./pages/ObjectGame";
import PatternGame from "./pages/PatternGame";
import FamilyGame from "./pages/FamilyGame";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* =========================
            WELCOME & AUTHENTICATION
        ========================= */}

        <Route
          path="/"
          element={<Welcome />}
        />

        <Route
          path="/login"
          element={<Login />}
        />


        {/* =========================
            REGISTRATION
        ========================= */}

        <Route
          path="/patient-registration"
          element={<PatientRegistration />}
        />

        <Route
          path="/add-caregiver"
          element={<AddCaregiver />}
        />


        {/* =========================
            PATIENT HOME
        ========================= */}

        <Route
          path="/home"
          element={<Home />}
        />


        {/* =========================
            PATIENT FEATURES
        ========================= */}

        <Route
          path="/medicine"
          element={<Medicine />}
        />

        <Route
          path="/games"
          element={<Games />}
        />

        <Route
          path="/garden"
          element={<Garden />}
        />

        <Route
          path="/stories"
          element={<Stories />}
        />

        <Route
          path="/family"
          element={<Family />}
        />

        <Route
          path="/calm"
          element={<Calm />}
        />

        <Route
          path="/contacts"
          element={<Contacts />}
        />

        <Route
          path="/safety"
          element={<Safety />}
        />


        {/* =========================
            REMINDERS
        ========================= */}

        <Route
          path="/reminders"
          element={<Reminders />}
        />


        {/* =========================
            MEMORY ASSISTANCE
        ========================= */}

        <Route
          path="/memory-assistance"
          element={<MemoryAssistance />}
        />


        {/* =========================
            EMERGENCY ALERTS
        ========================= */}

        <Route
          path="/alerts"
          element={<Alerts />}
        />


        {/* =========================
            BRAIN GAMES
        ========================= */}

        <Route
          path="/games/memory"
          element={<MemoryGame />}
        />

        <Route
          path="/games/object"
          element={<ObjectGame />}
        />

        <Route
          path="/games/pattern"
          element={<PatternGame />}
        />

        <Route
          path="/games/family"
          element={<FamilyGame />}
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;

