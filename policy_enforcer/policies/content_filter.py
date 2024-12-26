class ContentFilter:
    def __init__(self):
        self.filters = {
            "HATE": ["racist", "bigot", "dehumanize"],
            "VIOLENCE": ["kill", "harm", "assault"],
            "SEXUAL": ["explicit", "porn", "nudity"],
            "INSULTS": ["stupid", "idiot", "fool"],
        }

    def check(self, text: str) -> str:
        for category, keywords in self.filters.items():
            for keyword in keywords:
                if keyword.lower() in text.lower():
                    return f"Blocked by content filter: {category} (Keyword: {keyword})"
        return None
