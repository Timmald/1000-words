from unittest import TestCase
from reverseImageSearch import *
import asyncio as aio

class Tests(TestCase):
    def test_from_url(self):
        url = 'https://www.ford.com/is/image/content/dam/vdm_ford/live/en_us/ford/nameplate/mustang/2022/collections/dm/21_FRD_MST_wdmp_200510_02298.tif?croppathe=1_21x9&wid=1440'
        desc = get_elements_from_img(url)
        corpus = get_corpus_from_desc(desc)
        important_words = get_important_words(corpus, 150)
        print(important_words)
    def test_all(self):
        path = 'IMG_5669.jpeg'
        path = compress_image(path)
        print('compressed')
        aio.run(get_file_info(path))
        with open('url.txt','r') as reader:
            url = reader.read()
        print(f'uploaded at {url}')
        desc = get_elements_from_img(url)
        print(desc)
        corpus = get_corpus_from_desc(desc)
        print(corpus)
        important_words = get_important_words(corpus, 50)
        print(important_words)

    def test_non_ai_parts(self):
        desc = 'a man in a red shirt and a woman in a black and white dress, a stock photo by Minerva J. Chapman, trending on cg society, vancouver school, renaissance painting, colorized, masculine'
        corpus = get_corpus_from_desc(desc)
        print(corpus)
        important_words = get_important_words(corpus, 150)
        print(important_words)

    def test_important_words(self):
        with open('testCorpus.txt', 'r') as reader:
            corpus = reader.read()
        print(get_important_words(corpus, 150))
