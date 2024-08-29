import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def estimate_birth_decade(website_url):
  """Estimates the birth decade from a personal website's content."""

  try:
    response = requests.get(website_url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')

    # Strategy 1: Look for explicit mentions of birth year or age
    birth_year_matches = re.findall(r'\bborn in (\d{4})\b', soup.get_text(), re.IGNORECASE)
    age_matches = re.findall(r'\b(\d+)\s*years?\s*old\b', soup.get_text(), re.IGNORECASE)

    if birth_year_matches:
      birth_year = int(birth_year_matches[0])
      return birth_year // 10 * 10  # Round down to the nearest decade

    if age_matches:
      current_year = datetime.now().year
      age = int(age_matches[0])
      birth_year = current_year - age
      return birth_year // 10 * 10

    # Strategy 2: Look for graduation years or other time-anchored events
    graduation_years = re.findall(r'\bgraduated in (\d{4})\b', soup.get_text(), re.IGNORECASE)

    if graduation_years:
      graduation_year = int(graduation_years[0])
      # Assume typical graduation age is around 22
      birth_year = graduation_year - 22
      return birth_year // 10 * 10

    # Strategy 3: Analyze the writing style and vocabulary (more complex)
    # This would require NLP techniques and a large dataset for training
    # ...

    return None  # Unable to determine

  except requests.exceptions.RequestException as e:
    print(f"Error fetching website: {e}")
    return None

# Example usage
website_url = "https://niznik-p.github.io/"
birth_decade = estimate_birth_decade(website_url)

if birth_decade:
  print(f"Estimated birth decade: {birth_decade}s")
else:
  print("Unable to estimate birth decade from the website.")