import httpx
from bs4 import BeautifulSoup
from app.models.quote import Quote
import random
import asyncio

async def scrape_random_quote():
    base_url = "https://saramro.com/quotes"
    total_pages = 1013  # The website has 1013 pages

    random_page = random.randint(1, total_pages)
    url = f"{base_url}?page={random_page}"

    print(f"Attempting to scrape a random quote from page {random_page}...")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            rows = soup.select("div.tbl_head01 tbody tr")

            if not rows:
                print(f"No quotes found on the randomly selected page {random_page}.")
                return

            scraped_quotes = []
            for i in range(0, len(rows), 2):
                if i + 1 >= len(rows):
                    continue

                title_row = rows[i]
                content_row = rows[i + 1]

                title_element = title_row.select_one("div.bo_tit a")
                content_element = content_row.select_one("td")

                if not title_element or not content_element:
                    continue

                # --- Author Extraction ---
                title_text = title_element.text.strip()
                parts = title_text.split(" - ")
                author = "익명"
                if len(parts) > 1:
                    author = parts[-1].strip()

                # --- Content Extraction ---
                for br in content_element.find_all("br"):
                    br.replace_with("\n")

                full_content_text = content_element.get_text().strip()
                lines = [line.strip() for line in full_content_text.split("\n") if line.strip()]

                if not lines:
                    continue

                content_lines = []
                author_found_in_content = False
                for line in reversed(lines):
                    if line.startswith("- "):
                        author_in_content = line[2:].strip()
                        if author_in_content:
                            author = author_in_content # Prefer author from content
                            author_found_in_content = True
                    else:
                        content_lines.insert(0, line)

                content = "\n".join(content_lines).strip()

                if not content and lines:
                    last_line = lines[-1]
                    if " - " in last_line and not author_found_in_content:
                        parts = last_line.split(" - ")
                        content = " - ".join(parts[:-1]).strip()
                        author = parts[-1].strip()
                    elif not content:
                        content = "\n".join(lines).strip()

                if content:
                    scraped_quotes.append({"content": content, "author": author})

            if not scraped_quotes:
                print(f"Could not parse any quotes from page {random_page}.")
                return

            # Select one random quote from the list of scraped quotes
            random_quote = random.choice(scraped_quotes)
            content = random_quote["content"]
            author = random_quote["author"]

            # Save the single random quote to the database
            await Quote.get_or_create(content=content, defaults={"author": author})

            print(f"✅ Successfully scraped and saved a random quote from page {random_page}.")
            print(f"  - Author: {author}")
            print(f"  - Content: {content[:80]}...")
            value = [author, content[:80]]
            return value


        except httpx.HTTPStatusError as e:
            print(f"❌ HTTP error while scraping page {random_page}: {e}")
        except Exception as e:
            print(f"❌ An error occurred while scraping a random quote: {e}")

# Note: The original function was named scrape_quotes.
# It has been replaced with scrape_random_quote.
# You will need to update the call in `app/main.py` to use this new function name.
async def scrape_quotes():
    # This function now calls the new random quote scraper.
    # This avoids having to change the call in `app/main.py`.
    await scrape_random_quote()