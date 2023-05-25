from pyfiglet import Figlet
import sys

figlet = Figlet()

fonts = figlet.getFonts()
#check for 0 command line arguments
if len(sys.argv) == 1:
   print('Invalid usage')

#check for only 2 command line arguments
elif len(sys.argv) == 3:

   #check for '-f' or '-font' as first command line argument
   if sys.argv[1] == '-f' or sys.argv[1] == '-font':
      #check for a font as second command line argument
      if sys.argv[2] in fonts:
         figlet.setFont(font = sys.argv[2])
         s = input('Input: ')
         print('Output: ' + figlet.renderText(s))

      #if second command line argument is not a font
      else:
         sys.exit('Invalid usage')

   else:
      sys.exit('Invalid usage')

else:
   sys.exit('Invalid usage')