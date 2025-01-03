import requests
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os

load_dotenv()

DB_URI = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}"
    f"/{os.getenv('DB_NAME')}"
)

POKEAPI_BASE_URL = os.getenv("POKEAPI_BASE_URL")

def connect_to_db():
    try:
        print("Connecting to database...")
        conn = psycopg2.connect(DB_URI)
        print("Connected to database successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_pokemon_batch(next_url):
    response = requests.get(next_url)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return [], None
    data = response.json()
    return data["results"], data.get("next")

def fetch_pokemon_details(pokemon_list):
    detailed_data = []
    for pokemon in pokemon_list:
        response = requests.get(pokemon["url"])
        if response.status_code == 200:
            details = response.json()
            detailed_data.append({
                "id": details["id"],
                "name": details["name"],
                "base_experience": details.get("base_experience", 0),
                "height": details.get("height", 0),
                "abilities": [
                    {"name": ability["ability"]["name"], "effect": None}
                    for ability in details["abilities"]
                ]
            })
    return detailed_data

def store_pokemon_data(conn, pokemon_data):
    print(f"Inserting {len(pokemon_data)} Pokémon into the database...")
    with conn.cursor() as cursor:
        execute_values(
            cursor,
            "INSERT INTO pokemon (id, name, base_experience, height) VALUES %s ON CONFLICT (id) DO NOTHING",
            [(p["id"], p["name"], p["base_experience"], p["height"]) for p in pokemon_data],
        )

        abilities = []
        for p in pokemon_data:
            for ability in p["abilities"]:
                abilities.append((ability["name"], ability["effect"], p["id"]))

        execute_values(
            cursor,
            "INSERT INTO abilities (name, effect, pokemon_id) VALUES %s ON CONFLICT DO NOTHING",
            abilities,
        )
        conn.commit()
    print("Data insertion completed for this batch.")

def main():
    print("✅ Application is starting...")

    conn = connect_to_db()
    if not conn:
        return

    next_url = f"{POKEAPI_BASE_URL}?limit=100"
    while next_url:
        pokemon_batch, next_url = fetch_pokemon_batch(next_url)
        if not pokemon_batch:
            break

        detailed_pokemon = fetch_pokemon_details(pokemon_batch)
        store_pokemon_data(conn, detailed_pokemon)

    conn.close()
    print("Database connection closed. All Pokémon data has been stored.")

if __name__ == "__main__":
    main()
