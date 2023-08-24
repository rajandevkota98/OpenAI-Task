from api.text_generation.text_generation import TextGeneration

text = TextGeneration("hello")
if __name__ == '__main__':
    text1 = text.generate_text()
    print(text1)
