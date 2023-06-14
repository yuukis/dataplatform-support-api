from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/token")
def get_token():
    url = "https://idm.dataplatform-yamanashi.jp/auth/realms/Smartcity/protocol/openid-connect/token"

    payload='grant_type=client_credentials'
    headers = {
        'Authorization': 'Basic ["クライアントID:クライアント・シークレット"をBase64エンコードした文字列]',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()