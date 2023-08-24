from fastapi import FastAPI, Form, HTTPException
from starlette.responses import RedirectResponse,FileResponse
from api.text_generation.text_generation import TextGeneration
from api.text_summarization.text_summarization import TextSummarization
from api.paraphsing.text_paraphase import TextParaphrasing
from api.constant import APP_HOST,APP_PORT
from uvicorn import run as app_run


app = FastAPI()
origins = ["*"]

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

text_gen = TextGeneration()
text_sum = TextSummarization()
text_para = TextParaphrasing()

@app.post("/generate_text/")
def generate_text(text: str = Form(...)):
    generated_text = text_gen.generate_text(text)
    return {"generated_text": generated_text}


@app.post("/generate_summary/")
def generate_text(text: str = Form(...)):
    generated_sum = text_sum.summarize_content(text)
    return {"generated_text": generated_sum}


@app.post("/text_paraphase/")
def generate_text(text: str = Form(...)):
    generated_paraphase = text_para.paraphrase_text(text)
    return {"generated_text": generated_paraphase}


        
if __name__ == "__main__":
    app_run(app,host=APP_HOST,port=APP_PORT)