# firefish-rss-parsing

This is intended to be used for my own site - deletecat.com - though you might find it useful!

## Requirements

- Python 3.11
- Python3-feedparser
- wget

### Setup

If you are using Debian, you can run the following commands to setup python to use this script:

```
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-feedparser wget
```

This may be different for the distribution you may be using.

## What data does trhis script use?

This script uses the following data from the rss feed:
- feed['title'] - this contains the display name and the username of the firefish account
- feed['link'] - this contains a link to the firefish account's page
- feed['image']\['href'] - this contains a link to the firefish account's profile picture stored on the instance's CDN
- entry['title'] - this contains the display name of the account and one of two words; 'says' or 'replies'
- entry['link'] - this contains a link to the post shown in the entry
- entry['published'] - this contains the date the post was published
- entry['content']\['value'] - this contains the content stored in the entry

## What can I change in this script to use it on my website?

My code is a bit shit, but you can change the following variables:
- url - replace with your account url / rss feed
- stylesheet - replace with the name of your stylesheet

The script will overwrite the previous `index.html` everytime it is run. It also downloads your profile picture from the cdn every time it is run. I am using an <iframe\> to display this on my site's home page without using up the instance's bandwidth. 

The script ignores any replies and will also remove the <span\> tag from the end of `entry['content']['value']`.

I intend to use this with a Github action's script to update whenever there is a new entry on the rss feed.