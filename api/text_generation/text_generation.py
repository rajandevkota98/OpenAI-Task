import openai
from api.utils import read_yaml

class TextGeneration:
    def __init__(self, prompt: str):
        self.prompt = prompt
        self.credentials = read_yaml('/home/rajan/GPT-Work/crediantials/crediatial.yml')
        self.api_key = self.credentials['OPENAI_API_SECRET']
        openai.api_key = self.api_key
    
    def generate_text(self):
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=self.prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
