// frontend/src/pages/ChatPage.jsx

import React, { useState, useEffect } from "react";
import { signup, login } from "../services/auth";
import { sendMessage } from "../services/chat";

export default function ChatPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [token, setToken] = useState(null);
  const [loggedIn, setLoggedIn] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // On page load, check if token exists in localStorage
  useEffect(() => {
    const savedToken = localStorage.getItem("access_token");
    if (savedToken) {
      setToken(savedToken);
      setLoggedIn(true);
    }
  }, []);

  const handleSignup = async () => {
    try {
      setLoading(true);
      setError("");
      await signup(email, password);
      alert("Signup successful. Now log in!");
    } catch (err) {
      console.error(err);
      setError(err?.response?.data?.detail || "Signup failed.");
    } finally {
      setLoading(false);
    }
  };

  const handleLogin = async () => {
    try {
      setLoading(true);
      setError("");
      const res = await login(email, password);
      setToken(res.access_token);
      localStorage.setItem("access_token", res.access_token);
      setLoggedIn(true);
      setEmail("");
      setPassword("");
    } catch (err) {
      console.error(err);
      setError(err?.response?.data?.detail || "Login failed.");
    } finally {
      setLoading(false);
    }
  };

  const handleSendMessage = async () => {
    try {
      setLoading(true);
      setError("");
      const res = await sendMessage(message, token);
      setReply(res.reply);
    } catch (err) {
      console.error(err);
      setError(err?.response?.data?.detail || "Failed to send message.");
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    setToken(null);
    setLoggedIn(false);
    setReply("");
  };

  return (
    <div className="p-8 max-w-xl mx-auto">
      {!loggedIn ? (
        <div className="space-y-4">
          <h1 className="text-2xl font-bold">Login or Signup</h1>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="border px-3 py-2 w-full"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="border px-3 py-2 w-full"
          />
          <div className="flex gap-4">
            <button
              onClick={handleSignup}
              disabled={loading}
              className="bg-green-600 text-white px-4 py-2 rounded"
            >
              Sign Up
            </button>
            <button
              onClick={handleLogin}
              disabled={loading}
              className="bg-blue-600 text-white px-4 py-2 rounded"
            >
              Log In
            </button>
          </div>
          {error && (
            <p className="text-red-600 text-sm">
              {error}
            </p>
          )}
        </div>
      ) : (
        <div className="space-y-4">
          <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold">Chat</h1>
            <button
              onClick={handleLogout}
              className="text-sm text-red-500"
            >
              Logout
            </button>
          </div>
          <input
            type="text"
            placeholder="Type your message..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            className="border px-3 py-2 w-full"
          />
          <button
            onClick={handleSendMessage}
            disabled={loading}
            className="bg-purple-600 text-white px-4 py-2 rounded"
          >
            Send
          </button>
          {reply && (
            <div className="mt-4 bg-gray-100 p-4 rounded">
              <strong>Server replied:</strong> {reply}
            </div>
          )}
          {error && (
            <p className="text-red-600 text-sm">
              {error}
            </p>
          )}
        </div>
      )}
    </div>
  );
}