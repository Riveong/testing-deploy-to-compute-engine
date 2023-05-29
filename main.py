import uvicorn
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel

app = FastAPI()
port = int(os.getenv("PORT"))

class Item(BaseModel):
    game: str



def isChad(game):
    res="unknown"
    said = game

    if (said == "genshin impact"):
        res = "virgin"
    elif (said == "fortnite"):
        res = "a 5 y old"
    elif (said == "league of legends"):
        res = "virgin + pls take shower"
    elif (said == "valorant"):
        res = "either a edater or downbad af"
    
    return res


@app.get("/")
def hello_world():
    return ("hello world")

@app.post("/")
def create_item(item: Item):
    result = isChad(item.game)
    return result


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port, timeout_keep_alive=1200)