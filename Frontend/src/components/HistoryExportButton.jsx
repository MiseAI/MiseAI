import React from "react";

const HistoryExportButton = ({ filter }) => {
  const handleExport = () => {
    let url = `/export_history`;
    if (filter) {
      url += `?filter_keyword=${encodeURIComponent(filter)}`;
    }
    window.open(url, "_blank");
  };

  return (
    <button onClick={handleExport} className="px-3 py-2 bg-blue-600 text-white rounded">
      Export Chat History
    </button>
  );
};

export default HistoryExportButton;
