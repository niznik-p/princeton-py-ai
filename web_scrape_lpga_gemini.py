import requests
from bs4 import BeautifulSoup
from datetime import datetime

# By my count, to get this working I only needed to change about 5ish lines of code!
# I did also ask ChatGPT and Copilot, but they preferred working with an API that doesn't exist as their first guess.

def get_next_lpga_event(today):
    """Fetches the next LPGA event from the LPGA website.

    Args:
        today: A datetime object representing the current date.

    Returns:
        A dictionary containing the name, location, and dates of the next LPGA event, or None if no event is found.
    """

    url = "https://www.lpga.com/tournaments"  # Replace with the actual LPGA tournaments page URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all tournament elements (replace with the appropriate CSS selector)
    # tournament_elements = soup.find_all('div', class_='tournament-card')
    tournament_elements = soup.find_all('div', class_='tournament-schedule')

    for tournament in tournament_elements:
        # Extract tournament details (replace with the appropriate CSS selectors)

        # MYEDIT: Update the class for the tournament name
        # name = tournament.find('h3', class_='tournament-name').text.strip()
        name = tournament.find('h3', class_='tournament-title').text.strip()
        # MYEDIT: Location is going to be too complicated based on the HTML structure, so ignore
        # location = tournament.find('p', class_='tournament-location').text.strip()
        # MYEDIT: Update the class for the tournament month and days - see below
        # dates_str = tournament.find('p', class_='tournament-dates').text.strip()

        # Parse the date string (adjust the format as needed)
        # MYEDIT start_date_str, end_date_str = dates_str.split(' - ')
        month = tournament.find('div', class_='month').text
        day_list = tournament.find('div', class_='day').text.split('-')

        start_date_str = month + ' ' + day_list[0] + ', 2024'
        end_date_str = month + ' ' + day_list[1] + ', 2024'

        start_date = datetime.strptime(start_date_str, '%b %d, %Y')
        end_date = datetime.strptime(end_date_str, '%b %d, %Y')

        # Check if the tournament is after today
        if start_date >= today:
            return {
                'name': name,
                # MYEDIT 'location': location,
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d')
            }

    # No upcoming events found
    return None

# Set today's date (replace with the actual date)
today = datetime(year=2024, month=9, day=5)

next_event = get_next_lpga_event(today)

if next_event:
    print(f"The next LPGA event is: {next_event['name']}")
    # print(f"Location: {next_event['location']}")
    print(f"Dates: {next_event['start_date']} to {next_event['end_date']}")
else:
    print("No upcoming LPGA events found.")