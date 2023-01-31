from unittest import TestCase
from reverseImageSearch import *

class Tests(TestCase):
    def test_all_from_url(self):
        """
        Uses a picture of a ford mustang to test the full process
        """
        url = 'https://www.ford.com/is/image/content/dam/vdm_ford/live/en_us/ford/nameplate/mustang/2022/collections/dm/21_FRD_MST_wdmp_200510_02298.tif?croppathe=1_21x9&wid=1440'
        desc = get_elements_from_img(url)
        corpus = get_corpus_from_desc(desc)
        important_words = get_important_words(corpus, 150)
        print(important_words)

    def test_non_ai_parts(self):
        """
        A faster test to run. Starts with a description of patrick hartman in maid outfit with guy in red shirt in background.
        """
        desc = 'a man in a red shirt and a woman in a black and white dress, a stock photo by Minerva J. Chapman, trending on cg society, vancouver school, renaissance painting, colorized, masculine'
        corpus = get_corpus_from_desc(desc)
        print(corpus)
        important_words = get_important_words(corpus, 150)
        print(important_words)

# TODO: Selenium Tests