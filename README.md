# Books Web Scraper
This project is a simple web scraper built using Python. It scrapes book information from the website [Books to Scrape](http://books.toscrape.com/) and saves the data into Excel and CSV files. The scraper collects details such as the title, link, price, and availability of the books.

## Features
- Scrapes book information from multiple pages of the website.
- Saves the scraped data in two formats: Excel (`.xlsx`) and CSV (`.csv`).
- Simple and easy-to-understand code, suitable for beginners.

## Project Structure
python_web_scraper/
- books.csv # CSV file containing the scraped data
- books.xlsx # Excel file containing the scraped data
- main.py # Main script for scraping and saving the data
- test.py # Script to check the current IP address
- README.md # Project documentation (this file)

## Requirements
- Python 3.x
- `requests`
- `BeautifulSoup4`
- `pandas`
- `openpyxl` (for Excel file support)

You can install the required Python packages using:
pip install requests beautifulsoup4 pandas openpyxl

## How to Run
1. Clone the repository:
git clone https://github.com/junesdream/web_scraper.git
cd python_web_scraper
2. Run the scraper
Execute the main.py script to start scraping the books data:
python main.py
The script will scrape the book details from the website and save them into books.xlsx and books.csv.
3. Check your current IP:
You can use the test.py script to check your current IP address:
python test.py
This can be useful if you need to troubleshoot connectivity issues.

## Customization
Modify the number of pages to scrape: By default, the script scrapes all available pages until it encounters a 404 error. You can customize this behavior by adjusting the loop in the main() function.
Change output file names: You can change the names of the output files by passing custom filenames to the save_to_files() function.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, feel free to create an issue or submit a pull request.

## License
This project is open-source and available under the MIT License.


