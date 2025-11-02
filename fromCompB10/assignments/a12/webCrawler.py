# Ashmeet Kaur
# CompB10 Fall 2025
# Web Crawler
# Build a web crawler application that will scan web pages for links, and follow them,
# scanning for more links until the application doesn’t find any new web pages on the website.

# For the following program: it is divided in 3 function: toHTML(), scanHTML(), linkToPath()
# Each function is connected to one another and basically use recursive for toHTML
# A link is read as HTML, then HTML is scanned to find related links, and this link path is printed to txt file


import os
import urllib.request, ssl

def toHTML(strURL):                                     # the function reads and decodes a url as HTML file
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(strURL, headers={'User-Agent': 'Chrome/35.0.1916.47'})
    page = urllib.request.urlopen(req, context=ctx)
    strPage = page.read().decode("UTF-8")
    #print(strPage)
    with open("htmlFile.txt", "w") as f:                # read HTML is written to txt file for ease to read files using readlines()
        f.write(strPage)
        f.close()
    scanHTML(strURL)                                          # links to next function


def scanHTML(strUrl):                                         # function scans HTML file to find related links
    with open("htmlFile.txt", "r") as f:                # the read html file is opened in read mode
        requiredText = "https://www.bmoseley.com/"      # required url which will be needed for further scan in given links
        lineList = f.readlines()                        # returns list of lines from HTML text file
        oneSiteLink = []                                # stores total unique links from given HTML file
        for line in lineList:                           # reads each line as string from list
            present = line.find(requiredText)           # if line contains URL which has given requiredText url sub
            if present != -1:                           # if appropriate url is present
                indexStart = present                    # indexes needed to filter url substring from line
                indexEnd = line.find("html\">") + 4
                requiredLink = line[indexStart:indexEnd]
                if(requiredLink not in oneSiteLink):    # checks if same link is not already present
                    oneSiteLink.append(requiredLink)
        if len(oneSiteLink) > 0:                        # this particular syntax allows to only print paths which has further link
            linkToPath(oneSiteLink, strUrl)             # links to next function


def linkToPath(oneSiteLink, strUrl):                    # this function prints pathway linked to given url from html file
    if not os.path.exists("linkPath.txt"):              # if file is not found
        with open("linkPath.txt", "w") as file:         # a new file is created, hence stores original link pathway from og HTML file
            file.write(f"Original path:\n{strUrl}")
    else:                                               # else next prints will be sub link pathways/sub url page
        with open("linkPath.txt", "a") as file:
            file.write(f"\n\nSub Link from prior path:\n{strUrl}") # prints the head url for this pathway
    for link in oneSiteLink:                            # works to print subLinks for the given url page
        with open("linkPath.txt", "a") as file:
            file.write(f" ------> {link}")
    for link in oneSiteLink:                            # works as recursive function
        print("Reaching to sub link:")                   # traverses one allowed link at a time given on th given page
        print(link)
        toHTML(link)                                    # leads back to reading new url page as HTML


# Main program / original url to be read
strUrl = 'https://www.bmoseley.com/test.html'
toHTML(strUrl)
