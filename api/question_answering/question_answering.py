import openai
from api.utils import read_yaml

class QASystem:
    def __init__(self):
        self.credentials = read_yaml('/home/rajan/GPT-Work/crediantials/crediatial.yml')
        self.api_key = self.credentials['OPENAI_API_SECRET']
        openai.api_key = self.api_key
    
    def get_answer(self, question: str, context: str):
        prompt = f"Question: {question}\nContext: {context}\nAnswer:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        answer = response.choices[0].text.strip()
        return answer
