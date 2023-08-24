import os
from api.utils.common import read_yaml


class TextGeneration:
    def __init__(self,promt:str):
        self.promt =promt
        self.creiantials = read_yaml('crediantials/crediatial.yml')
        self.api = self.creiantials['OPENAI_API_SECRET']

    def print_(self,):
        print(self.api)


text = TextGeneration("hello")
text.print_()



    
if __name__=='main':
    text = TextGeneration("hello")
    text.print_()

    

