from unittest import TestCase
from reverseImageSearch import *

class Tests(TestCase):
    def test_get_urls_from_img(self):
        print(get_urls_from_img('/Users/nathanwolf/Documents/Coding/PycharmProjects/1000-words/IMG_5669.jpeg'))

    def test_get_corpus_from_urls(self):
        print(get_corpus_from_urls(get_urls_from_img('/Users/nathanwolf/Documents/Coding/PycharmProjects/1000-words/IMG_5669.jpeg')))

    def test_get_important_words(self):
        print(get_important_words(get_corpus_from_urls(get_urls_from_img('/Users/nathanwolf/Documents/Coding/PycharmProjects/1000-words/IMG_5669.jpeg'))))
