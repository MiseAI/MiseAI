// frontend/src/pages/UploadInvoicePage.jsx

import React, { useState, useEffect } from "react";
import axios from "axios";

export default function UploadInvoicePage() {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [error, setError] = useState("");
  const [invoices, setInvoices] = useState([]);

  const token = localStorage.getItem("access_token");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    setUploadStatus("Uploading...");
    setError("");

    try {
      const formData = new FormData();
      formData.append("file", file);

      const res = await axios.post(
        `${import.meta.env.VITE_API_BASE_URL}/api/invoice/upload`,
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setUploadStatus("Upload successful!");
      fetchInvoices();
    } catch (err) {
      console.error(err);
      setError(err?.response?.data?.detail || "Upload failed.");
      setUploadStatus("");
    }
  };

  const fetchInvoices = async () => {
    try {
      const res = await axios.get(
        `${import.meta.env.VITE_API_BASE_URL}/api/invoice/list`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setInvoices(res.data.invoices);
    } catch (err) {
      console.error(err);
      setError("Failed to load invoices.");
    }
  };

  useEffect(() => {
    fetchInvoices();
  }, []);

  return (
    <div className="p-8 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Upload Invoice</h1>

      <input
        type="file"
        onChange={handleFileChange}
        className="mb-4"
      />

      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Upload
      </button>

      {uploadStatus && (
        <p className="mt-2 text-green-600">{uploadStatus}</p>
      )}
      {error && (
        <p className="mt-2 text-red-600">{error}</p>
      )}

      <h2 className="text-xl font-bold mt-8">Your Invoices</h2>
      <ul className="mt-4 space-y-2">
        {invoices.map((inv, idx) => (
          <li key={idx} className="border p-3 rounded">
            Vendor: {inv.vendor} — Amount: ${inv.amount} — Date: {inv.date}
          </li>
        ))}
      </ul>
    </div>
  );
}
