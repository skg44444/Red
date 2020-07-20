from . import Log
from . import Application

def main():
    EngineLog = Log.logger("Engine")

    app = Application.Application()
    app.run()
    del app

    EngineLog.info("Exiting Main function")

if __name__ == "__main__":
    main()