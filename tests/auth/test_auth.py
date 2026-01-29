"""
Petit test d'authentification pour l'API fastapi de sentiment analysis
objectif : vérifier que les identifiants marchent bien
et que un mauvais mot de passe renvoie bien une erreur
"""

import os
import time
import requests

API_ADDRESS = os.environ.get("API_ADDRESS", "api")
API_PORT = os.environ.get("API_PORT", "8000")
BASE_URL = f"http://{API_ADDRESS}:{API_PORT}"

LOG = os.environ.get("LOG", "0") == "1"
LOG_PATH = "/reports/api_test.log"


def log(msg):
    print(msg)
    if LOG:
        try:
            os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
            with open(LOG_PATH, "a") as f:
                f.write(msg)
        except Exception as e:
            print("probleme ecriture log:", e)


def wait_for_api():
    print("attente que l'api soit prete...")
    for i in range(30):
        try:
            r = requests.get(f"{BASE_URL}/status")
            if r.status_code == 200:
                print("api ok !")
                return True
        except:
            pass
        time.sleep(2)
    print("api pas dispo apres 1 min...")
    return False


def test_user(username, password, expected_code):
    print(f"Test de connexion pour {username}")
    try:
        r = requests.get(f"{BASE_URL}/permissions", params={
            "username": username,
            "password": password
        })
        code = r.status_code
        if code == expected_code:
            result = "SUCCES"
        else:
            result = "ECHEC"
        msg = f"\n[AUTH TEST] {username} → attendu {expected_code}, obtenu {code} : {result}\n"
        log(msg)
        return code == expected_code
    except Exception as e:
        log(f"Erreur pendant le test de {username}: {e}\n")
        return False


def main():
    print("==== DEMARRAGE DU TEST D'AUTHENTIFICATION ====")

    if not wait_for_api():
        log("L'API ne répond pas, j'arrete les tests.\n")
        return

    all_ok = True
    all_ok &= test_user("alice", "wonderland", 200)
    all_ok &= test_user("bob", "builder", 200)
    all_ok &= test_user("clementine", "mandarine", 403)

    if all_ok:
        print("Tous les tests AUTH sont OK")
    else:
        print("Certains tests AUTH ont echoué")
        exit(1)


if __name__ == "__main__":
    main()

