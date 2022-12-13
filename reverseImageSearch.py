import time

from bs4 import BeautifulSoup
from requests import get
from statistics import mode
import replicate
import re
import os.path
from urllib.parse import quote
from os import environ
import discord
from PIL.Image import Image
import PIL.Image


def compress_image(imgPath: str) -> str:
    """
    Compress an image to get under discord upload limit
    :param imgPath: The path to the original file
    :return: The path to the compressed file
    """
    img = PIL.Image.open(imgPath)
    if img.size[0] >= img.size[1]:
        greaterEdge = 0
        lesserEdge = 1
    else:
        greaterEdge = 1
        lesserEdge = 0
    ratio = img.size[greaterEdge] / img.size[lesserEdge]
    newSize = [None, None]
    newSize[lesserEdge] = 720
    newSize[greaterEdge] = round(720 * ratio)
    newSize = tuple(newSize)
    img = img.resize(newSize)
    img.save(f'compressed {os.path.basename(imgPath)}')
    return 'compressed ' + os.path.basename(imgPath)


async def upload_image(imgPath: str):
    """
    Upload the image at imgPath to discord
    Writes url to a text file for later use

    :param imgPath: The path of the image to upload
    """
    # TODO: rewrite to work with image bytes
    # TODO; rewrite to give a url on this website
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    url = ''

    @client.event
    async def on_ready():
        global url
        channel = client.get_channel(691423966773903403)
        file = discord.File(imgPath)
        message = await channel.send(file=file)
        url = message.attachments[0].url
        with open('url.txt', 'w') as writer:
            writer.write(url)
        await client.close()

    await client.start('NzQ5NzI3NzYwODk2ODg0Nzg2.GHDz1M.iJ3XSjKS4iw_P2zd1c5AY1-ALzL9Y4LyQl-Omk')
    await client.close()
    return

def get_elements_from_img(imgPath: str) -> list[str]:
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


def get_corpus_from_desc(imgDesc: str) -> str:
    """
    Use Wikipedia to get info on each part of the image description, and assemble it all into one massive corpus of text

    :param imgDesc: description of elements and style in image, comma-separated
    :return: large string of all the text in wiki articles combined into one string
    """
    #TODO: When it is asked about a white house this goes to the white house. Fix.
    elems = imgDesc.split(', ')
    corpus = ""
    # google the first thing mentioned in the description
    url = f'https://www.google.com/search?client=firefox-b-1-d&q={elems[0]}'
    html = get(url).text
    # find wikipedia pages to add to corpus
    wikiLinks = re.findall('https://en.wikipedia.org/wiki/\w+', html)
    for link in wikiLinks:
        # Scrape each wiki page to add all the article text to corpus
        wiki = BeautifulSoup(get(str(link)).content, 'html.parser')
        paragraphs = wiki.find_all('p')
        for p in paragraphs:
            corpus += p.text
    # If there were no wikiLinks found
    if corpus == "":
        # search directly on wikipedia for first part of description
        url = f'https://en.wikipedia.org/wiki/Special:Search?search={elems[0]}&sourceid=Mozilla-search&ns0=1'
        html = get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        # Find all the search results
        linkDivs = soup.find_all('div', class_='mw-search-result-heading')
        # Use the first 3 articles that come up
        wikiLinks = ['https://en.wikipedia.org' + i.find('a').attrs['href'] for i in linkDivs][:3]
        for link in wikiLinks:
            # Extract text from each wiki article and add to corpus
            wiki = BeautifulSoup(get(str(link)).content, 'html.parser')
            paragraphs = wiki.find_all('p')
            for p in paragraphs:
                corpus += p.text
    return corpus


def get_important_words(corpus: str, numWords: int) -> list[str]:
    """
    :param corpus: Large body of text from which to extract important words
    :param numWords: number of important words to return
    :return: list of the numWords most important words
    """
    # for equivalence checking, lowercase everything in the corpus
    # Split corpus into a list with each individual word
    wordList = corpus.lower().split()
    commonList = []
    # remove (modified list of) fry first 100 common words
    with open('fryFirst100.txt', 'r') as reader:
        fry100 = reader.read().split(', ')
    for word in fry100:
        # remove all occurences of the word from the wordList
        while (word in wordList):
            wordList.remove(word)
    # throw out all words with length 1
    wordList = [i for i in wordList if len(i) > 1]
    # throw out any punctuation
    for word in wordList:
        if re.search('\W|\d', word) is not None or word[
                                                   :len(word) - 1] in wordList:  # also remove plurals with singulars in the list
            while word in wordList:
                wordList.remove(word)

    # find and return numWords most common words
    for i in range(numWords):
        mostCommon = mode(wordList)
        commonList.append(mostCommon)
        while (mostCommon in wordList):
            wordList.remove(mostCommon)
    return commonList
