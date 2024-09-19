import unittest
from unittest.mock import patch, MagicMock  # Füge MagicMock hier hinzu
from io import StringIO
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.main import scrape_books_on_page, save_to_files
class TestScraping(unittest.TestCase):


    @patch('main.requests.get')
    def test_scrape_books_on_page(self, mock_get):
        # Mock HTML response for a single book
        mock_html = '''
        <html>
            <head><title>Books to Scrape</title></head>
            <body>
                <li class='col-xs-6 col-sm-4 col-md-3 col-lg-3'>
                    <article>
                        <img alt="Test Book Title" src="test.jpg">
                        <h3><a href="test-book-url.html">Test Book</a></h3>
                        <p class="price_color">£51.77</p>
                        <p class="instock availability">In stock</p>
                    </article>
                </li>
            </body>
        </html>
        '''
        # Configure the mock response
        mock_response = MagicMock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        # Call the function
        books = scrape_books_on_page(1)

        # Check that the book details are correct
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['Title'], "Test Book Title")
        self.assertEqual(books[0]['Link'], "https://books.toscrape.com/catalogue/test-book-url.html")
        self.assertEqual(books[0]['Price'], "51.77")
        self.assertEqual(books[0]['Stock'], "In stock")

    @patch('main.requests.get')
    def test_scrape_books_on_invalid_page(self, mock_get):
        # Mock HTML response for a 404 page
        mock_html = '''
        <html>
            <head><title>404 Not Found</title></head>
        </html>
        '''
        # Configure the mock response
        mock_response = MagicMock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        # Call the function and expect None for a non-existent page
        books = scrape_books_on_page(9999)
        self.assertIsNone(books)

    @patch('pandas.DataFrame.to_excel')
    @patch('pandas.DataFrame.to_csv')
    def test_save_to_files(self, mock_to_csv, mock_to_excel):
        # Test data to save
        test_data = [
            {'Title': 'Book 1', 'Link': 'link1', 'Price': '10.00', 'Stock': 'In stock'},
            {'Title': 'Book 2', 'Link': 'link2', 'Price': '15.00', 'Stock': 'Out of stock'}
        ]

        # Call the function
        save_to_files(test_data)

        # Check that the functions to save data were called
        self.assertTrue(mock_to_excel.called)
        self.assertTrue(mock_to_csv.called)

if __name__ == "__main__":
    unittest.main()
