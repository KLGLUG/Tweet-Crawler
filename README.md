# Tweet-Crawler

This is a python script used to download Tweets of a #tag from the Twitter API.

To run this script we require consumer_key, consumer_secret, access_token, and
access_token_secret

To obtain these you need to go dev.twitter.com, login and create a new application
Then Create an access token. This will give you all four of the above.

**Do not share these credentials with anyone.As they can be misused.**

fill these credentials in between quotes before running the script
This script downloads the tweets removing Retweets,hyperlinks and Hashtags.

Limitation of Twitter API is we can download the tweets limited to that current week.

### To run in Terminal :
```sh
# Install pip
$ sudo apt install python3-pip
# Install twitter
$ pip3 install twitter
# Run the script
$ python3 Tweet_crawler.py

```
