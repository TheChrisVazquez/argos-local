from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import argostranslate.translate

app = FastAPI()

@app.get("/translate", response_class=PlainTextResponse)
def translate(
    text: str,
    from_lang: str = Query(alias="from"),
    to_lang: str = Query(alias="to")
):
    return argostranslate.translate.translate(
        text,
        from_lang,
        to_lang
    )