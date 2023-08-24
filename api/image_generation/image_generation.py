import openai
from api.utils import read_yaml

class ImageGeneration:
    def __init__(self):
        self.credentials = read_yaml('/home/rajan/GPT-Work/crediantials/crediatial.yml')
        self.api_key = self.credentials['OPENAI_API_SECRET']
        openai.api_key = self.api_key
    
    def generate_image(self, input_text: str):
        response = openai.Image.create(
        prompt=input_text,
        n=1,
        size="1024x1024"
        )
        return response['data'][0]['url']
