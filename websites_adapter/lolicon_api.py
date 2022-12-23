from .ArtInfo import Image, ArtInfo
import requests
import logging
import json

async def get_setu(tag: str|list[str] = None, 
    r18: int = 0, 
    num: int = 1, 
    uid: int | list[int] = None, 
    proxy: str = "", 
    excludeAI: bool = False
) -> list[ArtInfo]:
    """
    https://api.lolicon.app/#/setu?id=%e8%af%b7%e6%b1%82
    """
    size = ["regular", "original"]

    url = "https://api.lolicon.app/setu/v2"

    params = {
        "r18": r18,
        "num": num,
        "uid": uid,
        "tag": tag,
        "size": size,
        "proxy": proxy, 
        "excludeAI": False
    }

    r = requests.post(url, json=params).json()

    if r["error"] != "":
        logging.error("获取失败！"+r)
        return []
    
    data: list[dict] = r["data"]

    list_artInfo = []

    for pic in data:
        image = Image(pic["urls"]["regular"], pic["urls"]["original"], pic["width"], pic["height"])
        pid = pic["pid"]
        post_url = "https://www.pixiv.net/artworks/"+str(pid)
        artInfo = ArtInfo("Pixiv", post_url, pic["title"], "", pic["author"], pic["uid"], 1, [image])
        list_artInfo.append(artInfo)
    
    return list_artInfo
