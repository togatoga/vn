import requests
import pprint
import crayons

BASE_URL = "https://glosbe.com/gapi/{}"

class Glosbe(object):
    def __init__(self, from_lng, dest_lng):
        self.from_lng = from_lng
        self.dest_lng = dest_lng

    def _translate(self, phrase, tm=False):
        params = dict({
            "from": self.from_lng,
            "dest": self.dest_lng,
            "phrase": phrase,
            "format": 'json',
            "pretty": True,
        })
        if tm:
            params['tm'] = True
        r = requests.get(BASE_URL.format("translate"), params=params)
        if r.status_code != 200:
            return
        return r.json()
    def translate(self, phrase, tm=False):
        json = self._translate(phrase, tm)
        if not json['result'] == 'ok':
            return
        self.result = json
    def get_translations(self):
        translations = []
        values = set()
        for translation in self.result['tuc']:
            if 'phrase' in translation:
                if translation['phrase']['text'] in values:
                    continue
                values.add(translation['phrase']['text'])
                translations.append(translation['phrase']['text'])
        return translations

    def get_examples(self):
        examples = []
        for example in self.result['examples']:
            examples.append([example['first'], example['second']])
        return examples
        
            
