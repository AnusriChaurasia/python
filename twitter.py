import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "JS7bbVBAo0j5ZDDMq5nJMVJV1",
    "consumer_secret"     : "7bTkI1c06sf8j2uDtRehCAkSQLuhUWACCLuG1FgKgrmImQODxM",
    "access_token"        : "967252071517970433-IsKl2YTxcjtUhE8LkFpXRXzcF6SNl3B",
    "access_token_secret" : "F3BAuVQfciu7EaSncW7T68WLXSIVROM78Y4G8lsVKg7xK" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
