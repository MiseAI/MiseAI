const BASE = "https://miseai-backend-production.up.railway.app/auth";

async function register(event) {
  event.preventDefault();
  const { username, email, password } = event.target.elements;
  const res = await fetch(`${BASE}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: username.value,
      email: email.value,
      password: password.value,
    }),
  });
  const data = await res.json();
  if (res.ok) {
    alert(data.message);
    window.location.href = "/login.html";
  } else {
    alert(data.detail || JSON.stringify(data));
  }
}

async function login(event) {
  event.preventDefault();
  const { email, password } = event.target.elements;
  const res = await fetch(`${BASE}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      email: email.value,
      password: password.value,
    }),
  });
  const data = await res.json();
  if (res.ok) {
    localStorage.setItem("access_token", data.access_token);
    window.location.href = "/dashboard.html";
  } else {
    alert(data.detail || JSON.stringify(data));
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const regForm = document.getElementById("register-form");
  if (regForm) regForm.addEventListener("submit", register);

  const logForm = document.getElementById("login-form");
  if (logForm) logForm.addEventListener("submit", login);
});
