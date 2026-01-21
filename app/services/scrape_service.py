import requests
from bs4 import BeautifulSoup
from app.db.session import SessionLocal
from app.models.quote import Quote

def scrape_quotes():
    url = "https://saramro.com/quotes"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes_html = soup.select('.quote-list .quote-item')

    db = SessionLocal()
    try:
        for q in quotes_html:
            content = q.select_one('.quote-content').text.strip()
            author = q.select_one('.quote-author').text.strip()
            quote = Quote(content= content, author= author)

            db.add(quote)
        db.commit()
        print("명언 저장 완료")

    except Exception as e:
        db.rollback()
        print("오류:",e)

    finally:
        db.close()