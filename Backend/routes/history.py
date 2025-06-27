from fastapi import APIRouter, Query, Response
from datetime import datetime
from io import StringIO

router = APIRouter()

# Dummy data for demonstration
dummy_history = [
    {"timestamp": "2025-06-26 10:00", "user": "Alice", "message": "Hello AI!"},
    {"timestamp": "2025-06-26 10:01", "user": "AI", "message": "Hi Alice, how can I help?"},
    {"timestamp": "2025-06-26 10:02", "user": "Alice", "message": "Show me sales forecast."},
]

@router.get("/history/export")
def export_history(
    filter_text: str = Query(default=None, description="Filter history by keyword"),
):
    """
    Export chat history as tab-separated file.
    If filter_text is provided, filter only messages containing that text.
    """

    # Filter data if filter_text present
    history_data = dummy_history
    if filter_text:
        history_data = [
            row for row in dummy_history
            if filter_text.lower() in row["message"].lower()
        ]

    # Prepare TSV data
    output = StringIO()
    output.write("timestamp\tuser\tmessage\n")
    for item in history_data:
        output.write(f"{item['timestamp']}\t{item['user']}\t{item['message']}\n")

    file_content = output.getvalue()

    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"miseai_history_{date_str}.txt"

    return Response(
        content=file_content,
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )
