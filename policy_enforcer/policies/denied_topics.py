import re

class DeniedTopics:
    def __init__(self):
        self.topics = [
            {
                "name": "Politics",
                "definition": "Discussion about political parties or elections.",
                "keywords": ["politics", "election", "political party"]
            },
            {
                "name": "Finance Advice",
                "definition": "Personalized investment advice or strategies.",
                "keywords": ["finance advice", "investment advice", "financial planning", "portfolio"]
            },
            {
                "name": "Hacking",
                "definition": "Topics related to unauthorized access to systems, networks, or data.",
                "keywords": ["hack", "hacking", "hacked", "exploiting", "exploit"]
            },
            {
                "name": "Impersonation",
                "definition": "Attempts or discussions about pretending to be someone else for malicious purposes.",
                "keywords": ["impersonate", "impersonation", "pretend to be", "identity theft"]
            },
            {
                "name": "Social Engineering",
                "definition": "Topics involving manipulation techniques to gain sensitive information.",
                "keywords": ["social engineering", "phishing", "manipulate", "deception"]
            },
            {
                "name": "Illegal Activities",
                "definition": "Discussions promoting illegal actions or violating laws.",
                "keywords": ["illegal", "unlawful", "crime", "criminal activity"]
            }
        ]

    def check(self, text: str) -> str:
        for topic in self.topics:
            for keyword in topic["keywords"]:
                if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):  # Match full words, case insensitive
                    return f"Blocked by denied topic: {topic['name']} - {topic['definition']}"
        return None
