import React from "react";

function HistoryExportButton({ filter }) {
  const handleExport = () => {
    const mockHistory = [
      { id: 1, user: "Hello AI", ai: "Hello Chef!" },
      { id: 2, user: "Cost out recipe?", ai: "Sure, send me ingredients." }
    ];

    const filtered = filter
      ? mockHistory.filter(
          (item) =>
            item.user.includes(filter) || item.ai.includes(filter)
        )
      : mockHistory;

    const rows = filtered.map(
      (entry) => `${entry.id}\t${entry.user}\t${entry.ai}`
    );

    const fileContent = rows.join("\n");

    const blob = new Blob([fileContent], { type: "text/plain" });
    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = `miseai_history_${new Date().toISOString().split("T")[0]}.txt`;
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <button onClick={handleExport}>
      Export Chat History
    </button>
  );
}

export default HistoryExportButton;