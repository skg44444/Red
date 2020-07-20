from . import Log
from . import Application

def main():
    EngineLog = Log.logger("Engine")

    app = Application.Application()

    EngineLog.info("Created Application")
    app.run()
    del app

if __name__ == "__main__":
    main()