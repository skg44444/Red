from . import Log

class Application:
    
    def __init__(self):
        self.logger = Log.logger("Application")
        self.logger.info("Created Application")
        pass

    def __del__(self):
        self.logger.info("Destroyed Application")

    def run(self):
        try:
            while(True):
                pass
        except:
            self.logger.error("Keyboard Interupt")
