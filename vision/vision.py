from spotify import SpotifyHandler


class Vision:

    online = False
    spot_handler = SpotifyHandler()

    def start(self):
        self.online = True
        self.spot_handler.start()

    def stop(self):
        self.online = False


if __name__ == "__main__":
    Vision().start()
