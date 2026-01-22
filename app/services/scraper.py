import httpx
from bs4 import BeautifulSoup
from app.models.quote import Quote


async def scrape_quotes():
    url = "https://saramro.com/quotes"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            soup = BeautifulSoup(response.text, "html.parser")

            # 사이트 구조에 맞는 선택자를 사용해야 합니다.
            # (예시 선택자이며, 실제 사이트 구조에 따라 .quote 등으로 수정 필요)
            quote_elements = soup.select('.quote-item')

            for el in quote_elements:
                content = el.select_one('.content').text.strip()
                author = el.select_one('.author').text.strip() if el.select_one('.author') else "익명"

                # 중복 저장 방지: 내용이 같으면 저장하지 않음
                await Quote.get_or_create(content=content, defaults={'author': author})

            print("명언 스크래핑 및 저장 완료!")
        except Exception as e:
            print(f"스크래핑 에러: {e}")