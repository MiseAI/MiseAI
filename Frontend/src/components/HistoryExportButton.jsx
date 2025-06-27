import React from "react";

function HistoryExportButton({ filter }) {
  const handleExport = () => {
    const data = [
      {
        timestamp: new Date().toISOString(),
        user: "User",
        message: "Sample chat message matching filter: " + filter,
      },
    ];

    const lines = data.map(
      (item) => `${item.timestamp}\t${item.user}\t${item.message}`
    );

    const fileContent = lines.join("\n");
    const blob = new Blob([fileContent], { type: "text/plain" });

    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    const date = new Date().toISOString().split("T")[0];
    link.download = `miseai_history_${date}.txt`;
    link.click();

    URL.revokeObjectURL(link.href);
  };

  return (
    <button onClick={handleExport}>
      Export History
    </button>
  );
}

export default HistoryExportButton;