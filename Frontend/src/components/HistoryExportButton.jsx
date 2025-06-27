import React from "react";

const HistoryExportButton = ({ filter }) => {
  const handleExport = async () => {
    const apiUrl = import.meta.env.VITE_API_URL;

    try {
      const response = await fetch(`${apiUrl}/chat/export?filter=${encodeURIComponent(filter)}`);
      if (!response.ok) {
        throw new Error("Failed to export history.");
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;

      const dateStr = new Date().toISOString().split("T")[0];
      link.download = `miseai_history_${dateStr}.txt`;

      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error(error);
      alert("Export failed.");
    }
  };

  return (
    <button
      onClick={handleExport}
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      Export Chat History
    </button>
  );
};

export default HistoryExportButton;
