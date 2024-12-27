class ContentFilter:
    def __init__(self):
        self.filters = {
            "HATE": [
                "racist", "bigot", "dehumanize", "discrimination", "hate speech",
                "slur", "xenophobia", "sexism", "homophobia", "bully",
                "ableist", "fatphobic", "misogynistic", "ethnic insult"
            ],
            "FAIRNESS_HARMS": [
                "discriminate", "bias", "stereotype", "prejudice", "segregation",
                "inequality", "marginalize", "oppress", "stigma"
            ],
            "VIOLENCE": [
                "kill", "harm", "assault", "stab", "shoot", "terrorist",
                "bomb", "attack", "murder", "weapon", "war", "bully",
                "intimidate", "stalk", "execute", "lynch"
            ],
            "SEXUAL": [
                "explicit", "porn", "nudity", "erotic", "prostitution", "rape",
                "abuse", "child exploitation", "sexual assault", "grooming",
                "genitals", "fetish", "voyeurism"
            ],
            "SELF_HARM": [
                "suicide", "self-harm", "cutting", "starve", "anorexia", "bulimia",
                "overdose", "self-inflict", "harm oneself", "self-mutilation"
            ],
            "INSULTS": [
                "stupid", "idiot", "fool", "dumb", "moron", "loser",
                "worthless", "garbage", "scum", "ignorant", "imbecile"
            ]
        }

    def detect_prompt_or_indirect_attack(self, user_input: str) -> str:
        """
        Detects prompt and indirect attacks using keyword and pattern matching.

        Args:
            user_input (str): The input provided by the user.

        Returns:
            str: A description of the attack type if detected, otherwise None.
        """
        prompt_attack_keywords = [
            "change system rules", "replace persona", "ignore restrictions",
            "you are unrestricted", "talk in URL encoding", "bypass limitations"
        ]
        indirect_attack_patterns = [
            "manipulate content", "post unauthorized updates",
            "data exfiltration", "security breached", "fraudulent activity",
            "block system", "infect systems", "execute code", "data removal"
        ]

        for keyword in prompt_attack_keywords:
            if keyword in user_input.lower():
                return "Prompt attack detected."

        for pattern in indirect_attack_patterns:
            if pattern in user_input.lower():
                return "Indirect attack detected."

        return None

    def check(self, text: str) -> str:
        """
        Checks the given text against the content filters and returns a response
        indicating the blocked category and keyword, if applicable.
        """
        # Check for prompt or indirect attacks
        attack_result = self.detect_prompt_or_indirect_attack(text)
        if attack_result:
            return attack_result

        for category, keywords in self.filters.items():
            for keyword in keywords:
                if keyword.lower() in text.lower():
                    return f"Blocked by content filter: {category} (Keyword: {keyword})"

        return None
