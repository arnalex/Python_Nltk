# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:11:38 2015

@author: amaurygrillr
"""

from boilerpipe.extract import Extractor
import nltk
import feedparser
import os
import sys
import io, json
from BeautifulSoup import BeautifulStoneSoup
from nltk import clean_html

#URL que l'on souhaite traiter
URL = 'https://fr.wikipedia.org/wiki/Accueil'

#Extrait le contenu de l'URL sans balises
def extractor(URL):

    extractor = Extractor(extractor='ArticleExtractor', url=URL)

    data = extractor.getText()

    file = open("data.txt", "w")
    file.write(data.encode('UTF-8'))
    file.close()

    #Scinde la contenu en phrase
    with open('data.txt', 'r') as f:
        s = f.read()
        sentences = s.split('.')

    #Liste de mot vide
    w=[]

    #Scinde les phrase en mots
    for sentence in sentences :
        w.extend(sentence.split(' '))

    print w

    #Retourne la liste de Mot
    return w
    
#Appel de la fonction d'extraction du contenu
extractor(URL)

#NLP en 5 étapes :
def nlp():
    #Customize your list of stopwords as needed. Here, we add common
    # punctuation and contraction artifacts.
    stop_words = nltk.corpus.stopwords.words('english') + [
    '.',
    ',',
    '--',
    '\'s',
    '?',
    ')',
    '(',
    ':',
    '\'',
    '\'re',
    '"',
    '-',
    '}',
    '{',
    u'—',
    ]

    #Tokenisation --> Scinde les phrases en mots
    for post in blog_data:
        sentences = nltk.tokenize.sent_tokenize(post['content'])

        words = [w.lower() for sentence in sentences for w in
                nltk.tokenize.word_tokenize(sentence)]

        fdist = nltk.FreqDist(words)

    # Basic stats
    num_words = sum([i[1] for i in fdist.items()])
    num_unique_words = len(fdist.keys())

    # Hapaxes are words that appear only once
    num_hapaxes = len(fdist.hapaxes())

    top_10_words_sans_stop_words = [w for w in fdist.items() if w[0]
                                    not in stop_words][:10]

    print post['title']
    print '\tNum Sentences:'.ljust(25), len(sentences)
    print '\tNum Words:'.ljust(25), num_words
    print '\tNum Unique Words:'.ljust(25), num_unique_words
    print '\tNum Hapaxes:'.ljust(25), num_hapaxes
    print '\tTop 10 Most Frequent Words (sans stop words):\n\t\t', \
            '\n\t\t'.join(['%s (%s)'
            % (w[0], w[1]) for w in top_10_words_sans_stop_words])
    print

    #POT taggins --> Permet de concevoir la grammaire (noms, adjectifs, verbes...)


    #Chunking --> Analyse ?

    #Extraction --> Arbre de décision avec chaque composantes
