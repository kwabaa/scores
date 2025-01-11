import requests
import pandas as pd

# NBA API endpoint for player boxscores
API_URL = "https://stats.nba.com/stats/playergamelogs"

# Request headers (required for NBA stats API)
HEADERS = {
    "Host": "stats.nba.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true",
    "Referer": "https://www.nba.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9"
}

# Parameters for the API call
PARAMS = {
    "Season": "2024-25",
    "SeasonType": "Regular Season",  # Change to "Playoffs" for playoff data
    "PlayerOrTeam": "P",  # "P" for Player, "T" for Team
    "MeasureType": "Base",
    "PerMode": "Totals",  # "PerGame" for per-game stats
}

def fetch_nba_boxscores():
    # Make the API request
    response = requests.get(API_URL, headers=HEADERS, params=PARAMS)
    if response.status_code != 200:
        print("Failed to fetch data:", response.status_code)
        return None

    # Parse JSON response
    data = response.json()
    results = data.get("resultSets", [])[0]
    headers = results.get("headers", [])
    rows = results.get("rowSet", [])

    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=headers)
    return df

# Fetch and save data
if __name__ == "__main__":
    df = fetch_nba_boxscores()
    if df is not None:
        print(f"Fetched {len(df)} rows of data.")
        df.to_csv("nba_player_boxscores.csv", index=False)
        print("Data saved to nba_player_boxscores.csv")
