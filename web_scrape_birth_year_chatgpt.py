import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve website content from {url}")

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Remove script and style elements
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()
    # Get text
    text = soup.get_text()
    return text

# Example usage
url = "https://niznik-p.github.io"
html_content = scrape_website(url)
text_content = extract_text_from_html(html_content)

def estimate_birth_decade(text):
    current_year = datetime.now().year
    # Look for years mentioned in the text
    years = re.findall(r'\b(19|20)\d{2}\b', text)
    birth_years = []

    for year in years:
        year = int(year)
        if 1920 <= year <= current_year:
            # Assume people typically talk about their birth or coming-of-age years
            birth_years.append(year)

    if birth_years:
        # Estimate the birth year based on the median of the extracted years
        birth_year_estimate = int(median(birth_years))
        birth_decade = (birth_year_estimate // 10) * 10
        return birth_decade
    else:
        return None


# Example usage
birth_decade = estimate_birth_decade(text_content)
if birth_decade:
    print(f"The person was likely born in the {birth_decade}s.")
else:
    print("Could not determine the birth decade.")
