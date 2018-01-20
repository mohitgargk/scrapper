import os
import json
from threading import Thread


class Scrapper(Thread):

    def __init__(self, conf, basePath, timestamp):
        Thread.__init__(self)

        self.name = conf['name']
        self.urlBase = conf['urlBase']

        if 'urlOpt' in conf :
            self.urlOpt = conf['urlOpt']
        if 'urlFut' in conf:
            self.urlFut = conf['urlFut']

        self.basePath = basePath
        self.timestamp = timestamp

    def preprocess(self):
        pass

    def save(self, data):
        dirs = self.basePath + '/' + self.name
        if not os.path.exists(dirs):
            os.makedirs(dirs)

        jsonStr = data.to_json(orient='records')
        data = json.loads(jsonStr)
        path = dirs + "/" + str(self.timestamp) + '.json'

        with open(path, 'w') as outfile:
           json.dump(data, outfile,encoding='utf-8')

    def run(self):
        print(self.name + ': No recipe found for scrapping. Skipping...')
        pass



