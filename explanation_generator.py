import google.generativeai as genai

# Initialize Gemini with your API key (replace with your key)
genai.configure(api_key="YOUR_KEY_HERE")

class ExplanationGenerator:
    def __init__(self, model_name="gemini-2.0-flash"):
        self.model = genai.GenerativeModel(model_name)

    def generate(self, query, context):
        prompt = (
            "You are a legal expert. Explain the clause below in clear, simple terms so that a common man can understand it easily. "
            "Keep the explanation concise, direct, and focused. Provide the important points in bullet format without adding legal jargon.\n\n"
            f"Context (similar clauses for reference):\n{context}\n\n"
            f"Clause:\n{query}\n\n"
            "Explanation (in bullet points):"
        )

        response = self.model.generate_content(prompt)
        return response.text.strip() if response.text else "No legal explanation generated."
