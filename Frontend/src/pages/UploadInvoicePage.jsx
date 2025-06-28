import React, { useState, useEffect } from "react";
import { uploadInvoice, listInvoices } from "../services/invoice";

export default function UploadInvoicePage() {
  const [file, setFile] = useState(null);
  const [invoices, setInvoices] = useState([]);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const token = localStorage.getItem("access_token");

  const handleUpload = async () => {
    if (!file) {
      setError("Please choose a file.");
      return;
    }
    try {
      setError("");
      setMessage("Uploading...");
      const res = await uploadInvoice(file, token);
      setMessage(res.message);
      fetchInvoices();
    } catch (err) {
      console.error(err);
      setError(err?.response?.data?.detail || "Upload failed.");
    }
  };

  const fetchInvoices = async () => {
    try {
      const data = await listInvoices(token);
      setInvoices(data);
    } catch (err) {
      console.error(err);
      setError("Failed to load invoices.");
    }
  };

  useEffect(() => {
    if (token) {
      fetchInvoices();
    }
  }, [token]);

  return (
    <div className="p-8 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Upload Invoice</h1>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button
        onClick={handleUpload}
        className="bg-green-600 text-white px-4 py-2 rounded"
      >
        Upload
      </button>

      {message && (
        <p className="text-green-600 mt-4">{message}</p>
      )}
      {error && (
        <p className="text-red-600 mt-4">{error}</p>
      )}

      <h2 className="text-xl font-bold mt-8 mb-2">Your Invoices</h2>
      {invoices.length === 0 ? (
        <p>No invoices yet.</p>
      ) : (
        <ul className="space-y-2">
          {invoices.map((inv) => (
            <li
              key={inv.id}
              className="border p-2 rounded bg-gray-100"
            >
              <span className="font-semibold">{inv.filename}</span>
              <br />
              <span className="text-sm text-gray-600">
                Uploaded at: {new Date(inv.uploaded_at).toLocaleString()}
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
