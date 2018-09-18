from bs4 import BeautifulSoup
import requests
search = ""
while search == "":
    search = input("Enter what you want to search ")
    try:
        print("Searching.. ")
    except ValueError:
        print ("Sorry, you cannot put an empty string")
        print ("try again.")



params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id":"b_results"})
links = results.findAll("li", {"class":"b_algo"})
for item in links:
    item_text = item.find("a").text
    item_links = item.find("a").attrs["href"]
    if item_text and item_links:
        print (item_text)
        print(item_links)
        # to find parents
        print ("Parent: ", item.find("a").parent)
        print ("Summary", item.find("a").parent.parent.find ("p").text)#go back one more parent
        children = item.children
        for child in children:
            print ("Child: ", child)
        children = item.find("h2")
        print ("Next sibling of the h2  is...", children.next_sibling)