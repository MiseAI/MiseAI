import React, { useState, useEffect } from "react";
import axios from "axios";

const UploadInvoicePage = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [invoices, setInvoices] = useState([]);

  const token = localStorage.getItem("token");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage("Please select a file.");
      return;
    }

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await axios.post(
        "http://127.0.0.1:8000/api/invoice/upload",
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setMessage(response.data.message || "File uploaded successfully!");
      setFile(null);
      fetchInvoices();

    } catch (error) {
      console.error("Upload error:", error);
      setMessage("Error uploading file.");
    }
  };

  const fetchInvoices = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/invoice/list",
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setInvoices(response.data);
    } catch (error) {
      console.error("Error fetching invoices:", error);
    }
  };

  const downloadInvoice = async (invoiceId, filename) => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/invoice/download/${invoiceId}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
          responseType: "blob",
        }
      );

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", filename);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

    } catch (error) {
      console.error("Download error:", error);
      alert("Error downloading invoice.");
    }
  };

  useEffect(() => {
    fetchInvoices();
  }, []);

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Upload Invoice</h1>
      <form onSubmit={handleUpload} className="space-y-4">
        <input
          type="file"
          onChange={handleFileChange}
          className="block w-full border rounded p-2"
        />
        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Upload
        </button>
      </form>
      {message && (
        <p className="mt-2 text-blue-700 font-semibold">{message}</p>
      )}

      <h2 className="text-xl font-bold mt-8 mb-4">Your Invoices</h2>
      <ul className="space-y-2">
        {invoices.map((invoice) => (
          <li
            key={invoice.id}
            className="flex justify-between items-center border p-2 rounded"
          >
            <span>{invoice.filename}</span>
            <button
              onClick={() => downloadInvoice(invoice.id, invoice.filename)}
              className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
            >
              Download
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UploadInvoicePage;
