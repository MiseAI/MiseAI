// src/services/invoice.js

import axios from "axios";

const API_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

/**
 * Uploads a single invoice file.
 * @param {File} file - The file to upload
 * @param {string} token - JWT token
 * @returns {Promise<any>}
 */
export const uploadInvoice = async (file, token) => {
  if (!token) {
    throw new Error("Missing token. User may not be logged in.");
  }

  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(`${API_URL}/api/invoice/upload`, formData, {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "multipart/form-data",
    },
  });

  return res.data;
};

/**
 * Fetches list of invoices for the current user.
 * @param {string} token - JWT token
 * @returns {Promise<any>}
 */
export const listInvoices = async (token) => {
  if (!token) {
    throw new Error("Missing token. User may not be logged in.");
  }

  const res = await axios.get(`${API_URL}/api/invoice/list`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return res.data;
};