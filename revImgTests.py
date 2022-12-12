from unittest import TestCase
from reverseImageSearch import *

class Tests(TestCase):
    def test_all(self):
        desc = get_elements_from_img('https://cdn.discordapp.com/attachments/888457393179070494/1045107756652302366/IMG_2988.jpg')
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
