import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Eobly8up6eT6L1lhHCbGZywBn", 
    "wUyJtuAUq1BwdZjS2KgurnW9i8RLW77xkM7Ntm4sFVKrhELpw3")
auth.set_access_token("262170671-HRNsceYeHjd8jIPSaYIJ4ZepyEUG6lJ8K12t3nP7", 
    "wsBYB3iJXjECRBSItABRcwEQAH0AJ5DQV9GRFQNcltK7A")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")