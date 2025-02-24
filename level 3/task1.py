# Task: Build a Web Scraper

# Develop a web scraper that extracts
# specific data from websites using libraries
# like BeautifulSoup or Scrapy. This task will
# improve their knowledge of web scraping
# techniques and handling HTML/XML data.


import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Scrapes the given website and extracts all types of content.
    :param url: URL of the website to scrape
    """
    try:
        # Send an HTTP GET request to fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for failed requests
        
        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all headings
        print("Headings:")
        for i in range(1, 7):
            headings = soup.find_all(f'h{i}')
            for heading in headings:
                print(f"H{i}: {heading.get_text(strip=True)}")
        
        # Extract all paragraphs
        print("\nParagraphs:")
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            print(p.get_text(strip=True))
        
        # Extract all links
        print("\nLinks:")
        links = soup.find_all('a', href=True)
        for link in links:
            print(f"Text: {link.get_text(strip=True)}, URL: {link['href']}")
        
        # Extract all images
        print("\nImages:")
        images = soup.find_all('img', src=True)
        for img in images:
            print(f"Image Source: {img['src']}")
        
        # Extract all lists
        print("\nLists:")
        lists = soup.find_all(['ul', 'ol'])
        for lst in lists:
            for item in lst.find_all('li'):
                print(f"- {item.get_text(strip=True)}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the website URL: ")  # User inputs the URL to scrape
    scrape_website(url)  # Call function to scrape data
