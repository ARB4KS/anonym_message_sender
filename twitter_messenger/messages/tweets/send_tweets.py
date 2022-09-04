import tweepy


api_key2 = "cw6elS3f8um1OLdQaHAQOUgCO"
#consumer key

api_key_secret2 = "Nn5UBgZ2nZIzp8rg0FnECDJ9ZRlVYaUiI3EJovPRPY54UYIHwo"



bearer_token ="AAAAAAAAAAAAAAAAAAAAAJzcggEAAAAAzMAfaTuDKWn9Ixf0cqVvImhX4Ao%3D0SbQld55OHBnMDiKcSahThtTqvvvxh9j2EtP4S6dvIXlWePag1"



acces_token2 ="1564683112629534720-Z1mYU2Dz6d6OF3XsDOEjLCvAnQli1g"

acces_token_secret2 = "N3UbNAk51I51FVVaRNWxnA68SsBwGZkN5nZtRCZ8BMchX"

auth = tweepy.OAuthHandler(api_key2,api_key_secret2)
auth.set_access_token(acces_token2,acces_token_secret2)
API = tweepy.API(auth)
client_id ="WTRXZkNKSHB4bmRtTXBuM01jQWM6MTpjaQ"
client_secret = "fxnWtLzsI_ZCdXjBBUFbQYKWEH2sxhqB_OGffM4WZrwetu57EL"

class Vamonos:
    @staticmethod
    def tweet(message,destinataire):
        print("la fonction est executée")
        auth = tweepy.OAuthHandler(api_key2, api_key_secret2)
        auth.set_access_token(acces_token2, acces_token_secret2)
        API = tweepy.API(auth)
        complete_message = message + "  adressé à: " + destinataire
        API.update_status(complete_message)