import nltk


class AplSuporteSintaxe():

    def __init__(self):
        nltk.download()

    def teste(self):
        stopwords = nltk.corpus.stopwords.words('portuguese')