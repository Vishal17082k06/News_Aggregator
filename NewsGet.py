import feedparser
import html
from bs4 import BeautifulSoup
url=""
choice=input()
if (choice=="Top Stories"):
    url="https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
elif (choice=="World News"):
    url="https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"
elif (choice=="Business News"):
    url="https://timesofindia.indiatimes.com/rssfeeds/1898055.cms"
elif (choice=="Sports News"):
    url="https://timesofindia.indiatimes.com/rssfeeds/4719148.cms"
elif (choice=="Entertainment News"):
    url="https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms"
elif (choice=="Tech News"):
    url="http://feeds.bbci.co.uk/news/technology/rss.xml"


def clean_summary(summary):
    
    if summary is None:
        return ""
    summary = html.unescape(summary)
    sum = BeautifulSoup(summary, "html.parser")
    return sum.get_text()
def getnews(url):
    summary=""
    try:
        feed=feedparser.parse(url)
        if feed.bozo==1:
            print("Error in sparsing:")
            return []
        news_art=[]
        for entry in feed.entries:
            news_art.append({
                    'Title':entry.title,
                    'Summary':clean_summary(entry.summary)
                })
        return news_art
    except Exception as e:
        print(e)
        return []
def print_news(news_list):
    if len(news_list)==0:
        print("News not available at the moment.Please try again later :(")
    for news in news_list:
        print("Title:",news['Title'])
        print("Summary:",news['Summary'])
        print("-"*40)
news=getnews(url)
print_news(news)


            

