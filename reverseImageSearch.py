from bs4 import BeautifulSoup
from requests import get
from statistics import mode
import replicate
import re
from urllib.parse import quote
from os import environ

def get_elements_from_img(imgPath:str)  -> list[str]:
    """
    get the list of things in an image using img2prompt

    :param imgPath: Path to the image put in
    :return: words describing the contents and style of an image
    """
    environ["REPLICATE_API_TOKEN"] = '4a7bcad11f59b9945a213ed97d91f7e87b9882d3'
    model = replicate.models.get("methexis-inc/img2prompt")
    version = model.versions.get("50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5")
    output = version.predict(image=imgPath)
    return output

def get_corpus_from_desc(imgDesc:str) -> str:
    """
    Use Wikipedia to get info on each part of the image description, and assemble it all into one massive corpus of text

    :param imgDesc: description of elements and style in image, comma-separated
    :return: large string of all the text in wiki articles combined into one string
    """
    elems = imgDesc.split(', ')
    corpus = ""
    #


    # for elem in elems:
    url = f'https://www.google.com/search?client=firefox-b-1-d&q={elems[0]}'
    html = get(url).text
    wikiLinks = re.findall('https://en.wikipedia.org/wiki/\w+', html)
    for link in wikiLinks:
        wiki = BeautifulSoup(get(str(link)).content, 'html.parser')
        paragraphs = wiki.find_all('p')
        for p in paragraphs:
            corpus += p.text
    return corpus



def get_important_words(corpus:str, numWords:int) -> list[str]:
    """
    :param corpus: Large body of text from which to extract important words
    :param numWords: number of important words to return
    :return: list of the numWords most important words
    """
    wordList = corpus.lower().split()
    commonList = []
    # remove fry first 100
    with open('fryFirst100.txt','r') as reader:
        fry100 = reader.read().split(', ')
    for word in fry100:
        while(word in wordList):
            wordList.remove(word)
    # throw out all words with length 1
    wordList = [i for i in wordList if len(i) > 1]
    # throw out any punctuation
    for word in wordList:
        if re.search('\W|\d', word) is not None or word[:len(word) - 1] in wordList:
            while word in wordList:
                wordList.remove(word)

    # find numWords most common words
    for i in range(numWords):
        mostCommon = mode(wordList)
        commonList.append(mostCommon)
        while(mostCommon in wordList):
            wordList.remove(mostCommon)
    return commonList



