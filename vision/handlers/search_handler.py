import webbrowser

from googlesearch import search


class SearchHandler:
    results = []

    def search(self, query):
        self.results = []
        for i, result in enumerate(search(query, num=1, stop=1, pause=.5)):
            self.results.append(result)
        self.open_url(self.results[0])

    def open_url(self, url):
        webbrowser.open_new(url)
