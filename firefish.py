#__import modules
import feedparser
import os

#__parse url
url = "https://kitty.social/@deletecat/rss"
feed = feedparser.parse(url)

entry_data = [] #__array will store entry dictionaries
entry_no = 0    #__variable will store number of entries
entry_max = 6   #__variable will store max number of entries displayed

username = feed.feed['title']
userlink = feed.feed['link']
userpfp = feed.feed.image['href']

#__repeat for every entry in the feed
for index in range(len(feed.entries)):
    #__set the entry to be the current entry
    entry = feed.entries[index]
    #__if the number of recent entries is equal to the max, end the loop
    if entry_no == entry_max:
        break
    #__split the title into an array
    title = entry.title.split(" ")
    #__if the last word in the title array == "says"
    if title[len(title)-1] == "says":
        entry_no += 1 #__add 1 to our number of entries
        #__add the entry data to a temporary variable
        entry_temp = {"entrylink": entry.link,
                      "published":entry.published,
                      "content":entry.content[0]['value']}
        entry_data.append(entry_temp) #__add our temporary dictionary to our array

#__split off the file extention
pfpType = userpfp.split(".")
#__if the file extension is gif, set the pfptype to 'pfp.gif'
if pfpType[len(pfpType)-1] == "gif":
    #__set userpfp to local file
    pfpType = "pfp.gif"
#__if the file extension is png, set the pfptype to 'pfp.png'
elif pfpType[len(pfpType)-1] == "png":
    pfpType = "pfp.png"
#__if the file extension is jpg, set the pfptype to 'pfp.jpg'
elif pfpType[len(pfpType)-1] == "jpg":
    pfpType = "pfp.jpg"

"""
Now that the data has been read into the array, 
and that we have our profile picture downloaded,
it's time to move onto making our html page.
"""
stylesheet = "style.css"
#__set initial lines of html
html_lines = f"""<!DOCTYPE html> 
<html lang="en"> 
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{stylesheet}">
    <title>RSS Feed</title>
</head>
<body>
"""

#__repeat for every entry in the feed
for index in range(len(entry_data)):
    #__repeat for every letter in the content of the entry
    for contIndex in range(len(entry_data[index]['content'])):
        #__removes <span> from the output
        if entry_data[index]['content'][contIndex] == "<" and entry_data[index]['content'][contIndex+1] == "s":
            content = entry_data[index]['content'][:contIndex-1]
            break #__the loop no longer has to continue
    #__replaces new lines with <br> tags
    content=content.replace("\n","<br>")
    #__add entry data to page
    html_lines += f'''<img src="{pfpType}"><h3><a href="{userlink}">{username}</a></h3>
    <h5>{entry_data[index]["published"]}</h5>
    <p>{content}</p>
    <span><a href="{entry_data[index]["entrylink"]}">Link to post</a></span><hr>\n'''
#__end page
html_lines += "</body>\n</html>"

old_html = "" #__store old html code

#__old html checking
old_file = os.path.isfile('index.html')
#__do this if the file does exist
if old_file == True:
    #__open the old file
    with open("index.html","r") as reader:
        #__add each line from old file to old_html
        for line in reader:
            old_html += line 

#__only make changes if needed
if old_html != html_lines:
    #__download pfp
    os.system(f"wget -O {pfpType} {userpfp}")
    updated = open("updated","x") #__create a file called updated - used in github action script
    updated.close() #__close the newly create file
    #__open the file in write mode, this will create the file if it doesn't already exist
    with open("index.html","w") as writer:
        #__write the page to file
        writer.write(html_lines)
#__if there hasn't been any change
else:
    #__delete updated - means the action script for updating the repo will not activate
    os.system("rm -rf updated")