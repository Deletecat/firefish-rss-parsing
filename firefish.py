#__import modules
import feedparser
import os

def start():
    try:
        #__parse url
        url = "https://kitty.social/@deletecat/rss"
        feed = feedparser.parse(url)
        #__declare variables variables
        username = feed.feed['title']
        userlink = feed.feed['link']
        userPFPUrl = feed.feed.image['href']
    except:
        #__this will only happen if a connection to the server fails and/or the url is incorrect
        exit("Error, no connection or incorrect url")
    else:
        return username, userlink, userPFPUrl, feed

def grabEntryData(feed):
    entry_data = [] #__array will store entry dictionaries
    entry_no = 0    #__variable will store number of entries
    entry_max = 6   #__variable will store max number of entries displayed
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
    return entry_data

def getPFPName(userPFPUrl):
    #__declare variables
    pfpName = "" #__used to store the file name of the profile picture
    endOfName = len(userPFPUrl) - 1 #__initially stores the position of the last character in the url, later used to find where the file name begins
    #__repeat for every character in the url
    for index in range(endOfName):
        #__check if the next character is a forward slash
        if userPFPUrl[endOfName] == "/":
            #__set the file name to every character after the forward slash
            pfpName = userPFPUrl[endOfName+1:]
            #__end the loop
            break
        #__otherwise, go back a character
        else:
            endOfName -= 1
    #__return the file name stored in pfpName
    return pfpName

def generatePage(entry_data, pfpName, userlink, username):
    stylesheet = "style.css"
    javascript = "script.js"
    #__set initial lines of html
    html_lines = f"""<!DOCTYPE html> 
    <html lang="en"> 
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{stylesheet}">
        <script src="{javascript}"></script>
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
        html_lines += f'''<img src="{pfpName}" class="pfp"><h3><a href="{userlink}">{username}</a></h3>
        <h5>{entry_data[index]["published"]}</h5>
        <p>{content}</p>
        <span><a href="{entry_data[index]["entrylink"]}">Link to post</a></span><hr>\n'''
    #__end page
    html_lines += "</body>\n</html>"
    old_html = oldHTMLChecking()
    return old_html, html_lines

def oldHTMLChecking():
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
    return old_html

def createPage(pfpName, userpfp, html_lines):
    #__check if the current profile picture doesn't exist - this should only download a new pfp if neccessary 
    if os.path.exists(pfpName) == False:
        #__remove old pfps
        os.system("rm -rf *.gif *.png *.jpg")
        #__download pfp
        os.system(f"wget {userpfp}")
    #__open the file in write mode, this will create the file if it doesn't already exist
    with open("index.html","w") as writer:
        #__write the page to file
        writer.write(html_lines)
        print("Page created successfully!")

def main():
    username, userlink, userPFPUrl, feed = start()
    entry_data = grabEntryData(feed)
    pfpName = getPFPName(userPFPUrl)
    old_html, html_lines = generatePage(entry_data, pfpName, userlink, username)
    if old_html != html_lines:
        createPage(pfpName, userPFPUrl, html_lines)
    else:
       print("No changes needed.")
    
if __name__ == "__main__":
    main()