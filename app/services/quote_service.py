
import aiohttp
from bs4 import BeautifulSoup
from app.models.quote import Quote
import random


async def scrape_quotes():
    url = "https://saramro.com/quotes"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    quotes_elements = soup.select(".quotes-content")  # 실제 사이트 구조에 맞게 수정 필요

    for elem in quotes_elements:
        content = elem.text.strip()
        author = elem.find_next("span").text.strip() if elem.find_next("span") else "Unknown"
        # DB에 저장
        await Quote.create(content=content, author=author)


async def get_random_quote():
    quotes = await Quote.all()
    if not quotes:
        return {"content": "명언이 없습니다.", "author": ""}
    q = random.choice(quotes)
    return {"content": q.content, "author": q.author}
