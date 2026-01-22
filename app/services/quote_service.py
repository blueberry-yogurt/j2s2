
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
    #quotes_elements = soup.select(".bo_tit a")
    quotes_elements = soup.select(".bo_tit a")
    for elem in quotes_elements:
        print(elem.get_text(strip=True))
        """
        content = elem.select_one(".text").text.strip()
        author = elem.select_one(".author").text.strip()
        print(content, author)
        await Quote.create(content=content, author=author)
        """


async def get_random_quote():
    quotes = await Quote.all()
    if not quotes:
        return {"content": "명언이 없습니다.", "author": ""}
    q = random.choice(quotes)
    return {"content": q.content, "author": q.author}
