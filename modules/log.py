import logging
import colorlog

def init_logger():
    logName = "logs.txt"
    allLogger = logging.getLogger(__name__)
    allLogger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler(f"./{logName}",mode="a")
    fileHandler.setLevel(logging.INFO)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.INFO)

    AllFormatter = "%(log_color)s>[%(asctime)s] - %(levelname)s: %(message)s"
    log_colors = {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bg_red,bold_white'
            }
    fmt = colorlog.ColoredFormatter(AllFormatter,log_colors=log_colors)
    fileHandler.setFormatter(logging.Formatter(AllFormatter[13:]))
    streamHandler.setFormatter(fmt)

    #6.logger addHandler
    allLogger.addHandler(fileHandler)
    allLogger.addHandler(streamHandler)

    allLogger.info("Log Module loaded successful")
    return allLogger