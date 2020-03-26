#urllib allows downloading URLs
import urllib.request
#sys allows to capture errors
import sys

#dummy url such that the while-loops works on the first time
urlToRead = 'http://wwww.google.com'

#Dictionary to save the shortnames (Key) and the corresponding URL (value)
crawledWebLinks = {}

while urlToRead != '':
    try:
        urlToRead = input('Please enter the next URL to crawl!\n')
        #By entering no URL the user indicates that they want to end
        if urlToRead == '':
            print('OK, exciting the loop')  
            break
        #If a real URL was entered, the user is asked for a shortname of the URL
        shortName = input('Please enter a short name for that URL: ' + urlToRead +'\n')
        #Crucial Function which does the downloading
        #urlopen() goes the website for that url, downloads the contents (which are in the form of HTML()
        #The webpage is stored in a string variable webFile
        #The read-function displays/returns the data
        webFile = urllib.request.urlopen(urlToRead).read()

        #Content and URL are now saved in the dictionary
        crawledWebLinks[shortName] = webFile
    except:
        print('Unexpected error')
        #The sys.exc_info()[0] returns information about the last error that occured
        print(sys.exc_info()[0])
        stopOrProceed = input('An error occured. \n Do you want to stop, then enter 1. \n Enter anything else to continue.' )
        if stopOrProceed == 1:
            print('stopping')
        else:
            print("Cool!...Let's continue")
            #This continue will skip out of the current iteration of this loop and move to the next
            continue

print(crawledWebLinks.keys())
