from serpapi import GoogleSearch
from bs4 import BeautifulSoup
from requests import get
from statistics import mode

def get_urls_from_img(imgPath:str)  -> list[str]:
    """
    get the list of links to relevant webpages based on the image uploaded

    :param imgPath: Path to the image put in
    :return: list of urls to the webpages
    """
    params = {
        "engine": "google_reverse_image",
        "image_url": imgPath,
        "api_key": "29420d534203b31c11a7a15289d8e86c80dff57fde091c4600b6a4a31136d6e7"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    # How to make urlList:
    urlList = []
    # 1. look through the knowledge_graph dict keys
    knowledge_graph = results['knowledge_graph']
    for key in knowledge_graph.keys():
        # 2. If any key has 'link' with no s, add it to urlList
        if 'link'in key and not key[len(key) - 1] == 's':
            urlList.append(knowledge_graph[key])
        # 3. If any key has 'links' loop through its value and extract the 'link' from each to add to list
        elif 'link' in key:
            for linkDict in knowledge_graph[key]:
                link = linkDict['link']
                urlList.append(link)
        # 4. If any key is has 'source' extract it's value's 'link' value and add to list
        elif 'source' in key:
            link = knowledge_graph[key]['link']
            urlList.append(link)
    return urlList
    #  TODO: In future, pass 'description' and 'title' and 'type' values to get_corpus to add more important words.



def get_corpus_from_urls(urlList:list[str]) -> str:
    """
    scrape each site in the urlList to create one mass of text representing all of the words about this image online

    :param urlList: list of urls for relevant webpages
    :return: large string of all the text in webpages provided combined into a single string
    """
    pass


def get_important_words(corpus:str, numWords:int) -> list[str]:
    """
    :param corpus: Large body of text from which to extract important words
    :param numWords: number of important words to return
    :return: list of the numWords most important words
    """
