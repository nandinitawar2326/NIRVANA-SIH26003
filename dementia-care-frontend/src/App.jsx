import { BrowserRouter, Routes, Route } from "react-router-dom";

// Authentication
import Welcome from "./pages/welcome.jsx";
import Login from "./pages/login.jsx";

// Registration
import PatientRegistration from "./pages/PatientRegistration.jsx";
import AddCaregiver from "./pages/AddCaregiver.jsx";

// Main Pages
import Home from "./pages/home.jsx";
import Medicine from "./pages/medicine.jsx";
import Games from "./pages/games.jsx";
import Garden from "./pages/garden.jsx";
import Stories from "./pages/stories.jsx";
import Family from "./pages/family.jsx";
import Calm from "./pages/calm.jsx";
import Contacts from "./pages/contacts.jsx";
import Safety from "./pages/safety.jsx";

// Caregiver / Backend Modules
import Reminders from "./pages/Reminders.jsx";
import MemoryAssistance from "./pages/MemoryAssistance.jsx";
import Alerts from "./pages/Alerts.jsx";

// Games
import MemoryGame from "./pages/memoryGame.jsx";
import ObjectGame from "./pages/objectGame.jsx";
import PatternGame from "./pages/patternGame.jsx";
import FamilyGame from "./pages/familyGame.jsx";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Welcome & Authentication */}
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />

        {/* Registration */}
        <Route
          path="/patient-registration"
          element={<PatientRegistration />}
        />
        <Route path="/add-caregiver" element={<AddCaregiver />} />

        {/* Patient Home */}
        <Route path="/home" element={<Home />} />

        {/* Patient Features */}
        <Route path="/medicine" element={<Medicine />} />
        <Route path="/games" element={<Games />} />
        <Route path="/garden" element={<Garden />} />
        <Route path="/stories" element={<Stories />} />
        <Route path="/family" element={<Family />} />
        <Route path="/calm" element={<Calm />} />
        <Route path="/contacts" element={<Contacts />} />
        <Route path="/safety" element={<Safety />} />

        {/* Reminders */}
        <Route path="/reminders" element={<Reminders />} />

        {/* Memory Assistance */}
        <Route
          path="/memory-assistance"
          element={<MemoryAssistance />}
        />

        {/* Emergency Alerts */}
        <Route path="/alerts" element={<Alerts />} />

        {/* Brain Games */}
        <Route path="/games/memory" element={<MemoryGame />} />
        <Route path="/games/object" element={<ObjectGame />} />
        <Route path="/games/pattern" element={<PatternGame />} />
        <Route path="/games/family" element={<FamilyGame />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
