const API_URL = "https://miseai-production.up.railway.app";

fetch(API_URL)
  .then(res => res.json())
  .then(data => {
    if (data.message) {
      document.getElementById("message").innerText = "Welcome to MiseAI";
    } else {
      document.getElementById("message").innerText = "Unexpected response from backend.";
    }
  })
  .catch(err => {
    document.getElementById("message").innerText = "Error connecting to backend.";
    console.error(err);
  });