from bs4 import BeautifulSoup
import requests



if __name__ == "__main__":
    link='https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=brooklyn-nine-nine'
    response=requests.get(link,timeout=5)
    soup=BeautifulSoup(response.content,"html.parser")


    links=[]
    newText=soup.find_all("div",attrs={"class":'script-season-links'})
    for text in newText:
        for allLinks in text.findAll('a', href=True):
            links.append('https://www.springfieldspringfield.co.uk'+allLinks['href'])

    episodeLinks=[]
    for everyLink in links:
        response=requests.get(everyLink,timeout=5)
        soup=BeautifulSoup(response.content,"html.parser")
        newText=soup.find_all("div",attrs={"class":'season-episodes'})
        for each in newText:
            for allLinks in each.findAll('a', href=True):
                episodeLinks.append('https://www.springfieldspringfield.co.uk/'+allLinks['href'])
    episodeScripts=[]

    for myLinks in episodeLinks:
        response=requests.get(myLinks,timeout=5)
        soup=BeautifulSoup(response.content,"html.parser")
        newText=soup.find_all("div",attrs={"class":'scrolling-script-container'})
        for text in newText:
            hello=text.get_text()
            episodeScripts.append(hello.encode("utf-8"))

    episodeCounts=[22,23,23,22,22,50]
    seasonEp=1
    epCount=1
    i=0

    while i<127:
        if epCount==4 and seasonEp==12:
            seasonEp+=1
            continue
        f= open('*path*+'+str(epCount)+'\\s'+str(epCount)+'e'+str(seasonEp)+'.txt',"w+")
        #print('*path*+'+str(epCount)+'\\s'+str(epCount)+'e'+str(seasonEp)+'.txt')
        f.write(str(episodeScripts[i]))
        f.close()
        if seasonEp==episodeCounts[epCount-1]:
            seasonEp=1
            epCount+=1

        else:
            seasonEp+=1
        i+=1
