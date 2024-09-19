import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books_on_page(page_number):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Überprüfe, ob die Seite existiert
    if soup.title and "404" in soup.title.text:
        return None

    books = []
    all_books = soup.find_all("li", class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    if not all_books:  # Wenn keine Bücher gefunden werden, gib None zurück
        return None

    for book in all_books:
        item = {
            'Title': book.find("img").get("alt"),
            'Link': "https://books.toscrape.com/catalogue/" + book.find("a").get("href"),
            'Price': book.find("p", class_="price_color").text.strip().replace('£', ''),
            'Stock': book.find("p", class_="instock availability").text.strip(),
        }
        books.append(item)

    return books



def save_to_files(data, excel_file="books.xlsx", csv_file="books.csv"):
    """Saves the scraped data to Excel and CSV files."""
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)
    df.to_csv(csv_file, index=False)

def main():
    current_page = 1
    all_books = []

    while True:
        print(f"Scraping Page {current_page}...")
        books = scrape_books_on_page(current_page)
        if not books:
            print("No more pages to scrape. Exiting.")
            break
        all_books.extend(books)
        current_page += 1

    save_to_files(all_books)
    print(f"Scraping completed. Data saved to 'books.xlsx' and 'books.csv'.")

if __name__ == "__main__":
    main()
