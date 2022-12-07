from unittest import TestCase
from reverseImageSearch import *

class Tests(TestCase):
    # def test_all(self):
    #     urls = get_urls_from_img('https://cdn.discordapp.com/attachments/778280061245063198/1049380510897553448/dji_fly_20221202_152940_1_1670012994987_photo.jpg')
    #     print(urls)
    #     corpus = get_corpus_from_urls(urls)
    #     print(corpus)
    #     important_words = get_important_words(corpus, 50)
    #     print(important_words)

    def test_non_serp_parts(self):
        urls = ['https://en.wikipedia.org/wiki/Car', 'https://www.google.com/search?client=firefox-b-d&q=car+wheels&sa=X&ved=2ahUKEwjghZianuj7AhWfRjABHQRaDYEQ6BMoAHoECDMQAg', 'https://www.google.com/search?client=firefox-b-d&q=car+invented&sa=X&ved=2ahUKEwjghZianuj7AhWfRjABHQRaDYEQ6BMoAHoECDEQAg', 'https://www.google.com/search?client=firefox-b-d&q=car+inventor&sa=X&ved=2ahUKEwjghZianuj7AhWfRjABHQRaDYEQ6BMoAHoECDQQAg', 'https://www.google.com/search?client=firefox-b-d&q=Carl+Benz&stick=H4sIAAAAAAAAAONgVuLQz9U3MLGsSF_EyumcWJSj4JSaVwUAdpovChgAAAA&sa=X&ved=2ahUKEwjghZianuj7AhWfRjABHQRaDYEQmxMoAXoECDQQAw', 'https://www.google.com/search?client=firefox-b-d&q=car+application&sa=X&ved=2ahUKEwjghZianuj7AhWfRjABHQRaDYEQ6BMoAHoECDIQAg', 'https://www.google.com/search?client=firefox-b-d&q=Automotive+Segments&stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUoIxtESyk630k_Nzc_PzrFLyy_PKE4tSilcxCjqWluTn5pdklqU65yQWF6cWL2IVRogpBKem56bmlRTvYGUEADKoYlNXAAAA&sa=X&ved=2ahUKEwjghZianuj7AhWfRjABHQRaDYEQMSgAegQIKhAB', 'https://www.google.com/search?client=firefox-b-d&q=Car+Materials&stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUoIxtESyk630k_Nzc_PzrFLyy_PKE4tSilcxcvomlqQWZSbmFC9i5XVOLFKA83ewMgIA9bzMcEkAAAA&sa=X&ved=2ahUKEwjghZianuj7AhWfRjABHQRaDYEQMSgAegQIKxAB']
        corpus = get_corpus_from_urls(urls)
        print(corpus)
        important_words = get_important_words(corpus, 50)
        print(important_words)
