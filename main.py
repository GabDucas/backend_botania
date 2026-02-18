from climate_rules import compute_actions
import requests

def get_outdoor_temperature_north_hatley():

    latitude = 45.2667
    longitude = -71.9833

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current_weather=true"
        "&timezone=America/Toronto"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        temperature = data["current_weather"]["temperature"]
        return temperature

    except (requests.RequestException, KeyError) as e:
        print(f"Erreur lors de la récupération de la température : {e}")
        return None



def read_sensors():
    # On mettait normalement du code pour lire les capteurs, mais pour l'instant on va juste retourner des valeurs d'exemple
    t_ext = get_outdoor_temperature_north_hatley()
    print(f"Température extérieure récupérée : {t_ext}°C")
    return {
        "T_int": 35,   
        "T_ext": t_ext,   
        "HR_int": 80, 
        "HR_ext": 85   
    }

if __name__ == "__main__":
    sensors = read_sensors()

    actions = compute_actions(
        T_int = sensors["T_int"],
        T_ext = sensors["T_ext"],
        HR_int = sensors["HR_int"],
        HR_ext = sensors["HR_ext"]
    )

    for index, action in enumerate(actions):
        print(f"Action {index + 1}: {action}")
    