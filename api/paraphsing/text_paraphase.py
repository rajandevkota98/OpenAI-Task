import openai
from api.utils import read_yaml

class TextParaphrasing:
    def __init__(self):
        self.credentials = read_yaml('/home/rajan/GPT-Work/crediantials/crediatial.yml')
        self.api_key = self.credentials['OPENAI_API_SECRET']
        openai.api_key = self.api_key
    
    def paraphrase_text(self, input_text: str, max_tokens: int = 50):
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=input_text,
            max_tokens=max_tokens,
            temperature=0.7 
        )
        return response.choices[0].text.strip()
