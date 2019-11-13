"""
Send an email notification that Flapjack Friday is tomorrow

"""

import win32com.client as win32

targetFile = 'flapgicians.txt'
flapgicians = []

def main():
   ############ DEV
   print 'instantiating handlers'

   # Handlers
   fHandler = FileHandler(targetFile)
   eHandler = EmailHandler()
   
   
   fHandler.parseAndUpdateFile()
   eHandler.sendEmails()


class FileHandler:
   def __init__( self, file ):
      self.file = file
      self.storage = []

   def parseFile(self):
      '''Reads file containing lineup, populates flapgicians with team up next,
         and stores the schedule, minus the entry being reported for later use
      '''
      ############ DEV
      print 'parsing file'





      with open( self.file, 'r' ) as info:
         # creates list of lines
         lines = info.readlines()

         # iterate through and parse each line
         for lineNum, line in enumerate( lines ):
            # remove new line characters
            line = line.strip('\n')
            # remove commas
            line = line.split(',')
            # parse out desired info
            parseInfo = {'date': line[0], 'partner1': line[1], 'partner2': line[2]}

            # store tomorrow's flapgicians
            if lineNum is 0:
               flapgicians.append(parseInfo['partner1'])
               flapgicians.append(parseInfo['partner2'])

            # store all but first line of file for later
            if lineNum > 0:
               self.storage.append( line )

   def updateFile(self):
      '''Overwrites lineup file to remove the entry being reported'''
      ############ DEV
      print 'updating file'






      with open(self.file, 'w') as update:
         for line in self.storage:
            for i, entry in enumerate(line):
               # add comma seperator for all but last entry in the line
               if i < 2:
                  entry += ','
                  # write line
               update.write(entry)
            # move to next line
            update.write('\n')

   def parseAndUpdateFile(self):
      '''handle all file parsing and updating. Basically cuts out the line of information we're interested in'''
      self.parseFile()
      self.updateFile()


class EmailHandler:
   def __init__( self):
      # list of deka emails without the isp info. This will be added later 
      self.emailList = ['rreihl', 'jlaplante']

   def addIsp(self):
      '''add @dekaresearch.com to each given email prefix'''
      for i, name in enumerate(self.emailList):
         self.emailList[i] += '@dekaresearch.com'
      print self.emailList

   def sendEmails(self):

      ######## DEV
      print 'generating message'


      '''sends out Flapjack Friday reminder email with names of the people cooking tomorrow'''
      line1 = 'Tomorrow is Flapjack Friday.\n\n'
      line2 = 'Flapgicians will be {0} and {1}.'.format(flapgicians[0], flapgicians[1])

      message = line1 + line2

      # open outlook
      outlook = win32.Dispatch('outlook.application')
      mail = outlook.CreateItem(0)

      # add handles
      self.addIsp()

      ############ DEV
      print 'preparing and sending email'


      mail.To = ('; '.join(self.emailList))
      mail.Subject = 'Flapjack Friday Reminder'
      mail.body = message
      mail.send


if __name__ == '__main__':
   main()
