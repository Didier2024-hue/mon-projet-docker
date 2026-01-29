"""
Test du contenu : on vérifie que les scores de sentiment sont cohérents
"""

import os
import time
import requests

API = f"http://{os.environ.get('API_ADDRESS','api')}:{os.environ.get('API_PORT','8000')}"
LOG = os.environ.get("LOG", "0") == "1"
LOG_PATH = "/reports/api_test.log"

def log(msg):
    print(msg)
    if LOG:
        try:
            os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
            with open(LOG_PATH, "a") as f:
                f.write(msg)
        except:
            pass

def wait_for_api():
    print("attente de l'api...")
    for i in range(30):
        try:
            r = requests.get(f"{API}/status")
            if r.status_code == 200:
                print("api ok")
                return True
        except:
            pass
        time.sleep(2)
    print("api pas prete")
    return False

def test_sentence(version, sentence, expect_positive=True):
    r = requests.get(f"{API}/{version}/sentiment", params={
        "username": "alice",
        "password": "wonderland",
        "sentence": sentence
    })
    if r.status_code != 200:
        log(f"Erreur HTTP {r.status_code} sur {sentence}\n")
        return False
    data = r.json()
    score = data.get("score", 0)
    if expect_positive:
        ok = score > 0
    else:
        ok = score < 0
    result = "SUCCES" if ok else "ECHEC"
    log(f"[CONTENT TEST] {version} | '{sentence}' → score={score} : {result}\n")
    return ok

def main():
    if not wait_for_api():
        log("API non prete, test annulé\n")
        return
    ok = True
    ok &= test_sentence("v1", "life is beautiful", True)
    ok &= test_sentence("v2", "life is beautiful", True)
    ok &= test_sentence("v1", "that sucks", False)
    ok &= test_sentence("v2", "that sucks", False)

    if ok:
        print("Tests de contenu OK")
    else:
        print("Erreur dans les tests de contenu")
        exit(1)

if __name__ == "__main__":
    main()

