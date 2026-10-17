
const API_BASE_URL = "http://10.249.188.236:8000";

// Create Patient
export async function createPatient(patientData) {
  const response = await fetch(
    `${API_BASE_URL}/patients/`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },

      body: JSON.stringify(patientData),
    }
  );

  if (!response.ok) {
    const errorText = await response.text();

    throw new Error(
      `Patient creation failed: ${response.status} ${errorText}`
    );
  }

  return await response.json();
}


// Get all patients
export async function getPatients() {
  const response = await fetch(
    `${API_BASE_URL}/patients/`
  );

  if (!response.ok) {
    throw new Error(
      `Failed to get patients: ${response.status}`
    );
  }

  return await response.json();
}


// Get one patient
export async function getPatient(patientId) {
  const response = await fetch(
    `${API_BASE_URL}/patients/${patientId}`
  );

  if (!response.ok) {
    throw new Error(
      `Failed to get patient: ${response.status}`
    );
  }

  return await response.json();
}

