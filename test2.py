api_response = {
    "id": "chatcmpl-123",
    "": [
        {"tool": "search", "status": "success", "content": "Kết quả A"},
        {"tool": "calculator", "status": "failed", "content": "Lỗi chia 0"},
        {"tool": "weather", "status": "success", "content": "Hà Nội 25 độ"},
    ],
}

results = [
    m["content"]
    for m in api_response.get("tool_results", [])
    if m.get("status") == "success"
]
print(results)