from twython import Twython, TwythonError

C_KEY = "your own API KEY"
C_SECRET= "your API SECRET"
A_TOKEN = "your ACCESS TOKEN"
A_SECRET = "your ACCESS TOKEN SECRET"

pipitan = Twython(C_KEY, C_SECRET, A_TOKEN, A_SECRET)
message= 'This is my Raspberry Pi tweeting. #myFirstTweet'
try:
    pipitan.update_status(status= message)
except TwythonError as e:
    print e

print(status +" ------tweeted")

