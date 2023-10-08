import paralleldots

class MyApi:

    def __init__(self):
        paralleldots.set_api_key('exsQSy6lrCFS7KZaOBF2WBql6eBgSOOGTzqg3XNgVWU')

    def sentiment_analysis(self,text):
        res = paralleldots.sentiment(text)
        return res

    def name_entity(self,text):
        res = paralleldots.ner(text)
        return res

    def emotion_rec(self,text):
        res = paralleldots.emotion(text)
        return res


