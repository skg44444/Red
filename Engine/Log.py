from datetime import datetime
import os

logColors = {
    "TRACE" : 32,
    "INFO"  : 32,
    "WARN"  : 33,
    "ERROR" : 31,
    "FATAL" : 31
}

class logger:
    def __init__(self, name):
        self.name = name
        initMsg = f"{self.name} Logger created"
        self.info(initMsg)
        
    def consoleLog(self, level, message):
        time = datetime.now().strftime('%H:%M:%S')
        print(f"\u001b[{logColors[level]}m[{level}]\t{time} : ({self.name}) - {message}\u001b[37m")

    def trace(self, log):
        self.consoleLog("TRACE", log)

    def info(self, log):
        self.consoleLog("INFO", log)

    def warn(self, log):
        self.consoleLog("WARN", log)

    def error(self, log):
        self.consoleLog("ERROR", log)

    def fatal(self, log):
        self.consoleLog("FATAL", log)