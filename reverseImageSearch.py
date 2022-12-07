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
    pass


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
