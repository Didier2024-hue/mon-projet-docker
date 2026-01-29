"""
Test d'autorisation : on vérifie que les utilisateurs ont les bons droits
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

def test_sentiment(version, user, pwd, expected):
    print(f"Test {user} sur {version}")
    r = requests.get(f"{API}/{version}/sentiment", params={
        "username": user,
        "password": pwd,
        "sentence": "hello world"
    })
    code = r.status_code
    ok = (code == expected)
    status = "SUCCES" if ok else "ECHEC"
    log(f"[AUTHORIZATION TEST] {user} - {version} attendu {expected}, obtenu {code} : {status}\n")
    return ok

def main():
    if not wait_for_api():
        log("API non prete, test annulé\n")
        return

    ok = True
    ok &= test_sentiment("v1", "bob", "builder", 200)
    ok &= test_sentiment("v2", "bob", "builder", 403)
    ok &= test_sentiment("v1", "alice", "wonderland", 200)
    ok &= test_sentiment("v2", "alice", "wonderland", 200)

    if ok:
        print("Tous les tests d'autorisation sont OK")
    else:
        print("Erreur dans un test d'autorisation")
        exit(1)

if __name__ == "__main__":
    main()

