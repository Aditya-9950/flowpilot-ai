def search_web(query: str):
    print(f"[WEB SEARCH] Searching for: {query}")

    # Simulate primary tool failure for the hackathon demo
    raise Exception("Primary search service unavailable")


def alternate_search(query: str):
    print(f"[FALLBACK SEARCH] Using alternate search for: {query}")

    return [
        {
            "title": "AI Intern",
            "company": "Fallback AI Company",
            "location": "Remote",
        },
        {
            "title": "Machine Learning Intern",
            "company": "Fallback Tech Company",
            "location": "India",
        },
    ]