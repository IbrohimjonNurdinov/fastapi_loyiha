from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def bosh_sahifa():
    return {"xabar": "Salom, FastAPI!"}

@app.get("/salom/{ism}")
def salom(ism: str):
    return {"xabar": f"Salom, {ism}!"}


from pydantic import BaseModel

xarajatlar = {}

class Xarajat(BaseModel):
    nom: str
    summa: int

@app.get("/xarajatlar")
def hammasi():
    return xarajatlar

@app.post("/xarajatlar")
def qosh(x: Xarajat):
    xarajatlar[x.nom] = x.summa
    return {"xabar": "qo'shildi", "jami": sum(xarajatlar.values())}

@app.delete("/xarajatlar/{nom}")
def ochir(nom: str):
    if nom in xarajatlar:
        del xarajatlar[nom]
        return {"xabar": "o'chirildi", "jami": sum(xarajatlar.values())}
    return {"xabar": "topilmadi"}