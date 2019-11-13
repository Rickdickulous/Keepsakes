import logging
import logging2



def main():
   logging.basicConfig(filename='logFile.log',
                             level=logging.INFO,
                             format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

   logger = logging.getLogger(__name__)

   #
   # At this point, strings sent to logger are printed only to the file specified in basicConfig
   #
   print "dir(logger):", dir(logger)
   print

   logger.info('test info message')

   #
   # Now enable stream handler. This will make the things sent to logs print to the console
   #
   enableStreamHandler(logger)

   logger.info('this should print to console')


def enableStreamHandler(logger_arg):
   """Setups a stream handler so that information logged to a file is also sent to the console.
      No argument for StreamHandler() puts everything into stderr"""
   console_handler = logging.StreamHandler()
   console_handler.setLevel(logging.INFO)

   formatter = logging.Formatter(fmt="%(asctime)s- %(name)s - %(message)s",
                                 datefmt="%Y-%m-%d %H:%M:%S")
   console_handler.setFormatter(formatter)

   logger_arg.addHandler(console_handler)


def printInformation():
   print "loggingModule logger name:", logger.name
   print

   print "loggingModule logger parent:", logger.parent
   print


main()
