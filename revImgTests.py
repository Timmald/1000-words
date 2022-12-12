from unittest import TestCase
from reverseImageSearch import *

class Tests(TestCase):
    def test_all(self):
        desc = get_elements_from_img('https://cdn.discordapp.com/attachments/778280061245063198/1049380510897553448/dji_fly_20221202_152940_1_1670012994987_photo.jpg')
        print(desc)
        corpus = get_corpus_from_desc(desc)
        print(corpus)
        important_words = get_important_words(corpus, 50)
        print(important_words)

    def test_non_ai_parts(self):
        desc = 'a parking lot filled with lots of parked cars, a tilt shift photo by Andrew Domachowski, tumblr, hudson river school, anamorphic lens flare, photo taken with provia, photo taken with ektachrome'
        corpus = get_corpus_from_desc(desc)
        print(corpus)
        important_words = get_important_words(corpus, 150)
        print(important_words)

    def test_important_words(self):
        with open('testCorpus.txt', 'r') as reader:
            corpus = reader.read()
        print(get_important_words(corpus, 150))
