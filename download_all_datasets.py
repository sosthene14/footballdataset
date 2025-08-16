import os
import requests

BASE_OUTPUT_DIR = "datasets"
os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)

competitions = {
    "E0": {"name": "Premier League", "dir": "premier_league"},
    "F1": {"name": "Ligue 1", "dir": "ligue1"},
    "D1": {"name": "Bundesliga 1", "dir": "bundesliga1"},
    "I1": {"name": "Serie A", "dir": "seriea"}
}

seasons = [
    "2425", "2324", "2223", "2122", "2021", "1920", "1819", "1718", "1617", "1516",
    "1415", "1314", "1213", "1112", "1011", "0910", "0809", "0708", "0607", "0506",
    "0405", "0304", "0203", "0102", "0001", "9900", "9899", "9798", "9697", "9596",
    "9495", "9394"
]

BASE_URL = "https://www.football-data.co.uk/mmz4281/{}/{}.csv"
NOTES_URL = "http://freebets.football-data.co.uk/notes.txt"

for code, info in competitions.items():
    output_dir = f"{BASE_OUTPUT_DIR}/{info['dir']}"
    os.makedirs(output_dir, exist_ok=True)

    for season in seasons:
        url = BASE_URL.format(season, code)
        filename = f"{output_dir}/{season}_{code}.csv"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200 and len(r.content) > 100:
                with open(filename, "wb") as f:
                    f.write(r.content)
                print(f"✅ Téléchargé : {filename}")
            else:
                print(f"⚠️ Pas de données pour {season} {info['name']}")
        except Exception as e:
            print(f"❌ Erreur {season} {code}: {e}")

notes_filename = f"{BASE_OUTPUT_DIR}/notes.txt"
try:
    r = requests.get(NOTES_URL, timeout=10)
    if r.status_code == 200:
        with open(notes_filename, "wb") as f:
            f.write(r.content)
        print(f"✅ Téléchargé : {notes_filename}")
    else:
        print(f"⚠️ Pas de données pour notes.txt")
except Exception as e:
    print(f"❌ Erreur notes.txt: {e}")