from wordcloud import WordCloud
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# Scaper
search_term = "pizza"
url = "https://www.google.com/search?q={0}&source=lnms&tbm=nws".format(search_term)
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
headlines = soup.find_all("div", {"class": "st"})

with open(search_term + ".txt", 'w') as v:
    for h in headlines:
        v.write(h.text)

v.close()


# Formatting text into single words
with open(search_term + ".txt", "r") as f:
    # make sentences into a list ["xxx xx xxx"]
    x = [line.rstrip("/n") for line in f]
    print(x)

    # y returns list in a list thus not hashable in Counter(): [["1", "2"], ["1", "2"]]
    y = [line.split(" ") for line in x]

    # z returns a single list that is hashable in Counter(): ["1", "2", "3"]
    for line in x:
        z = line.split()
        print(z)
        c = Counter(z)


# Removing stopwords
sw = stopwords.words('english')
sw.extend(("A", "a", "if"))
# adding in other words that are not inside the nltk library
# extend() takes only one argument, thus ((one, two, three))
for stopwords in sw:
    del c[stopwords]


# Wordcloud generation
wordcloud = WordCloud()
wordcloud.generate_from_frequencies(frequencies=c)
plt.figure()  # instantiate figure
plt.imshow(wordcloud, interpolation='lanczos')  # using imshow to show wordcloud on figure
plt.axis('off')
plt.show()
