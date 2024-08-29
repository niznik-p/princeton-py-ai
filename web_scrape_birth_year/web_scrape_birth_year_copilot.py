import requests
from bs4 import BeautifulSoup
import re


def fetch_website_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()


def extract_birth_year(text):
    # Look for patterns like "born in 1985" or "age 35"
    birth_year_pattern = re.compile(r'\b(born in|born|age)\s*(\d{4}|\d{1,2})\b', re.IGNORECASE)
    matches = birth_year_pattern.findall(text)

    for match in matches:
        if match[1].isdigit():
            year_or_age = int(match[1])
            if year_or_age > 1900:  # Likely a birth year
                return year_or_age
            elif year_or_age < 100:  # Likely an age
                current_year = 2023
                return current_year - year_or_age
    return None


def determine_decade(year):
    if year:
        decade = (year // 10) * 10
        return f"{decade}s"
    return "Unknown"


def main(url):
    content = fetch_website_content(url)
    text = parse_html(content)
    birth_year = extract_birth_year(text)
    decade = determine_decade(birth_year)
    print(f"The person was likely born in the {decade}.")


# Example usage
url = "https://importmattie.github.io/"
main(url)