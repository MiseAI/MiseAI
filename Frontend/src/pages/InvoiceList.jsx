import React, { useEffect, useState } from "react";
import axios from "axios";

const InvoiceList = () => {
  const [invoices, setInvoices] = useState([]);

  useEffect(() => {
    const fetchInvoices = async () => {
      try {
        const token = localStorage.getItem("token");
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

    fetchInvoices();
  }, []);

  const downloadInvoice = async (invoiceId, filename) => {
    try {
      const token = localStorage.getItem("token");

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

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Your Invoices</h2>
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

export default InvoiceList;
import InvoiceList from "./InvoiceList";
