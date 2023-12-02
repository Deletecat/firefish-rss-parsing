# firefish-rss-parsing

This is intended to be used for my own site - deletecat.com - though you might find it useful!

It pulls data and media from a firefish rss feed, then spits out a html page. I started this as the theme of the instance I am signed up to doesn't really fit the theme of my website. Using an iframe to embed my profile from that instance would look odd, so I wrote this script which allows me to style it the way I want!

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

This may be different for the distribution you are using.

An example CSS file has been included with the releases, feel free to tweak it if you so wish!

## What data does this script use?

This script uses the following data from the rss feed:
- feed['title'] - this contains the display name and the username of the firefish account
- feed['link'] - this contains a link to the firefish account's page
- feed['image']\['href'] - this contains a link to the firefish account's profile picture stored on the instance's CDN
- entry['title'] - this contains the display name of the account and one of these words; 'says', 'renotes' or 'replies'
- entry['link'] - this contains a link to the post shown in the entry
- entry['published'] - this contains the date the post was published
- entry['content']\['value'] - this contains the content stored in the entry

## What can I change in this script to use it on my website?

You can change the following variables in the script to use your firefish account instead:
- url - replace with your firefish's account rss feed
- stylesheet - replace with the name of your stylesheet (css)
- entry_max - if you want more entries to be displayed, change this value.

### This project is currently on hold, I plan to work on it again when I have more free time :)
