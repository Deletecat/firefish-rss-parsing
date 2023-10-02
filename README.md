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

This may be different for the distribution you are using.

## What data does this script use?

This script uses the following data from the rss feed:
- feed['title'] - this contains the display name and the username of the firefish account
- feed['link'] - this contains a link to the firefish account's page
- feed['image']\['href'] - this contains a link to the firefish account's profile picture stored on the instance's CDN
- entry['title'] - this contains the display name of the account and one of two words; 'says' or 'replies'
- entry['link'] - this contains a link to the post shown in the entry
- entry['published'] - this contains the date the post was published
- entry['content']\['value'] - this contains the content stored in the entry

## What can I change in this script to use it on my website?

You can change the following variables in the script to use your firefish account instead:
- url - replace with your firefish's account rss feed
- stylesheet - replace with the name of your stylesheet
- javascript - replace with the name of your scipt
- entry_max - if you want more entries to be displayed, change this value.

## What does the script do?

The script will do the following:
1. Use feedparsers parse() function to get data from the account's rss feed.
    - If no data has been retrieved, the script will exit with an error message (`Error, no connection or incorrect url`)
1. Sift through each entry in the rss feed and grab necessary data to display the entry.
    - Data is only taken from entries where the title of the post ends with `says`. It will not take any data from replies or quote posts.
1. Find out what the file name for the account's profile picture is and save it for later.
1. Generate each line of the page and store it in the variable `html_lines`.
1. Check to see if there is an existing file called `index.html`
    - If there is, read the file into a variable called `old_html`.
    - If there isn't, create an empty variable called `old_html`.
1. Check to see if `html_lines` and `old_html` match
    - If they match, the script will end by printing out a message saying `No changes needed.`.
    - If they don't match, the data stored in `html_lines` is written to `index.html`.
        - The script will also check to see if the profile picture exists with the name stored from earlier, if it does not, the old profile picture is deleted and a new one is downloaded. 


As of right now, I am running this script on my personal site; <https://deletecat.com>. Feel free to look there if you want to see the script in action!