import os
from threading import Thread


class Scrapper(Thread):

    def __init__(self, name, basePath, url, timestamp ):
        Thread.__init__(self)
        self.name = name
        self.basePath = basePath
        self.url = url
        self.timestamp = timestamp

    def save(self, data):

        dirs = self.basePath + '/' + self.name
        if not os.path.exists(dirs):
            os.makedirs(dirs)

        data.to_csv(dirs + "/" + str(self.timestamp) + '.csv')

    def run(self):
        print(self.name + ': No recipe found for scrapping. Skipping...')
        pass



