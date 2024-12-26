from policies.content_filter import ContentFilter
from policies.denied_topics import DeniedTopics
from policies.sensitive_info import SensitiveInfo
from policies.contextual_grounding import ContextualGrounding
from models.open_llm import generate_response

class PolicyEnforcer:
    def __init__(self):
        self.content_filter = ContentFilter()
        self.denied_topics = DeniedTopics()
        self.sensitive_info = SensitiveInfo()
        self.contextual_grounding = ContextualGrounding()

    def enforce_policies(self, user_input: str, model_response: str) -> dict:
        # Apply content filter
        content_result = self.content_filter.check(user_input)
        if content_result:
            return {"error": content_result}

        # Check denied topics
        topic_result = self.denied_topics.check(user_input)
        if topic_result:
            return {"error": topic_result}

        # Mask sensitive information in user input
        masked_input = self.sensitive_info.mask(user_input)

        # Mask sensitive information in model response
        masked_response = self.sensitive_info.mask(model_response)

        # Check contextual grounding
        grounding_result = self.contextual_grounding.check_relevance(user_input, model_response)
        if grounding_result:
            return {"error": grounding_result}

        return {"input": masked_input, "response": masked_response}

def main():
    enforcer = PolicyEnforcer()
    while True:
        user_input = input("Enter your query (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        model_response = generate_response(user_input)

        # Enforce policies
        result = enforcer.enforce_policies(user_input, model_response)

        if "error" in result:
            print(f"Policy Error: {result['error']}")
        else:
            print(f"Masked Input: {result['input']}")
            print(f"Model Response: {result['response']}")

if __name__ == "__main__":
    main()
