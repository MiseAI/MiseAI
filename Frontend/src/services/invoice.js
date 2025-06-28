import axios from "axios";

const API_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export const uploadInvoice = async (file, token) => {
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

export const listInvoices = async (token) => {
  const res = await axios.get(`${API_URL}/api/invoice/list`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return res.data;
};
