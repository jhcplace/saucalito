import requests
import webbrowser

class Oauth(object):
    client_id = "735992049236574340"
    client_secret = "UktnEPiLsoryEQhb-svJpkObQdvBAZ-H"
    scope = "identify%20email"
    redirect_uri = "https://jhcplace.github.io/saucalito/saucalitowebsite"
    discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=735992049236574340&redirect_uri=https%3A%2F%2Fjhcplace.github.io%2Fsaucalito%2Fsaucalitowebsite%2Findex.html&response_type=code&scope=identify%20email"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"


    @staticmethod
    def get_access_token(code):
        payload = {
            'client_id':Oauth.client_id,
            'client_secret':Oauth.client_secret,
            'grant_type':"authorization_code",
            'code':code,
            'redirect_uri':Oauth.redirect_uri,
            'scope':Oauth.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = requests.post(url = Oauth.discord_token_url, data = payload, headers = headers)
        json = access_token.json()
        return json.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = Oauth.discord_api_url+"/users/@me"

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        user_object = requests.get(url = url, headers = headers)
        user_json = user_object.json()
        return user_json
        