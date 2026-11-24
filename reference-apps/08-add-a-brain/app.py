"""Optional AI categoriser. The app works without a key via a deterministic fallback."""
import json
import os
from urllib.request import Request, urlopen

VALID = {"food", "travel", "bills", "entertainment", "other"}

def fallback(description: str) -> str:
    text = description.lower()
    if any(word in text for word in ("coffee", "lunch", "supermarket")): return "food"
    if any(word in text for word in ("train", "bus", "uber")): return "travel"
    return "other"

def suggest_category(description: str) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key: return fallback(description)
    body = json.dumps({"model": "gpt-4.1-mini", "input": f"Reply with one category only: {', '.join(sorted(VALID))}. Expense: {description}"}).encode()
    request = Request("https://api.openai.com/v1/responses", data=body, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urlopen(request, timeout=10) as response: answer = json.load(response)["output"][0]["content"][0]["text"].strip().lower()
        return answer if answer in VALID else fallback(description)
    except Exception: return fallback(description)

if __name__ == "__main__": print(suggest_category(input("Expense: ")))
