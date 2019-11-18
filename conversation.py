import random

import spacy
from spacy.symbols import VERB, nsubj
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from messages import Messsages
from jokes import get_random_joke

analyser = SentimentIntensityAnalyzer()
nlp = spacy.load('en_core_web_sm')
stop_words = set(stopwords.words('english'))


class Conversation:
    def __init__(self):
        self.state = {
            "depth": -1,
            "keywords": [],
            "question": False
        }

    def _clean(self, text):
        text = text.lower()
        words = word_tokenize(text)
        cleaned = [w for w in words if w not in stop_words]
        return ' '.join(cleaned)

    def response(self, text):
        '''
            Returns an appropriate response according to the current
            state and the message received.
        '''
        self.state['depth'] += 1

        if not self.state['depth']:
            return random.choice(Messsages['greeting'])

        s_score = analyser.polarity_scores(text)

        text = self._clean(text)
        doc = nlp(text)

        subs = list(doc.noun_chunks)
        score = s_score['compound']

        if self.state['question'] or s_score['compound'] >= 0.2:
            self.state['keywords'].extend(subs)

        reply = None

        if self.state['question']:
            self.state['question'] = False

            return random.choice(Messsages['subject_responses'])

        if score >= 0 and score < 0.4:
            c = random.randrange(0,  1)

            if c < 0.5 or self.state['keywords'].__len__() == 0:
                self.state['question'] = True
                reply = random.choice(Messsages['informative'])
            else:
                reply = random.choice(Messsages['positive_subject']).format(
                    random.choice(self.state['keywords']))

        elif score > 0:
            reply = random.choice(Messsages['positive'])
        else:
            if score >= -0.3:
                reply = random.choice(Messsages['negative'])
            else:
                reply = random.choice(Messsages['911'])
                reply += '\n'
                reply = "Here's a joke to cheer you up: \n"
                reply += get_random_joke()

        print(self.state)

        return reply

    def handle_neutral(self, message):
        if not self.state['depth']:
            return random.choice(Messsages['greeting'])


if __name__ == '__main__':
    doc = nlp('naman bad')

    verbs = set()

    print(list(doc.noun_chunks))
    print(verbs)
