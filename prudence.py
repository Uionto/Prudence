#This is my frist python program, be kind with me plz
import trio
import httpx
import string
import os
from termcolor import colored
from holehe.modules.social_media.instagram import instagram

print(colored('======================================================', 'yellow'))
print(colored('[!] Be sure to have downloaded holehe before run this.', 'yellow'))
print(colored('[!] >>> https://github;com/megadose/holehe', 'yellow'))
print(colored('======================================================', 'yellow'))
print(colored('= =    / _ \_ __ _   _  __| | ___ _ __   ___ ___   = =', 'yellow'))
print(colored('= =   / /_)/  __| | | |/ _` |/ _ \  _ \ / __/ _ \  = =', 'yellow'))
print(colored('= =  / ___/| |  | |_| | (_| |  __/ | | | (_|  __/  = =', 'yellow'))
print(colored('= =  \/    |_|   \__,_|\__,_|\___|_| |_|\___\___|  = =', 'yellow'))
print(colored('======================================================', 'yellow'))
print(colored('Made by aet in July 2021 -- https://github.com/novitae', 'yellow'))
print(colored('S/o https://githhub.com/megadose for the module holehe', 'yellow'))
print(colored('======================================================', 'yellow'))

#Choosing the program between simple email lookup or list of email lookup
programchoice = input(colored('[1] - Single email lookup\n[2] - List of email lookup\n >>> ', 'yellow'))

#Stopping the program if the int(input) is < than 1 or > than 2
if int(programchoice) > 2:
      print(colored('Invalid choice', 'red'))
if int(programchoice) < 1:
      print(colored('Invalid choice', 'red'))

#Launching the first program
if int(programchoice) == 1:
      email = input(colored('Enter the email adress.\n >>> ', 'yellow'))
      print(colored('\nResult (True = is used on Instagram - False = is not used on Instagram):\n', 'yellow'))
      #Using holehe module

      async def main():
          out = []
          client = httpx.AsyncClient()
          await instagram(email, client, out)

          #Writing down the raw result in a temporary txt file
          with open('out.txt', 'w') as txt:
              print(out, file=txt)

          await client.aclose()

      trio.run(main)

      #Clear the raw file to get only the True or False response
      tri = open('out.txt', 'rt')
      for line in tri:
          entri = (line.replace("[{'name': 'instagram', 'domain': 'instagram.com', 'method': 'register', 'frequent_rate_limit': True, 'rateLimit': False, 'exists': ", ''))
          triade = (entri.replace(", 'emailrecovery': None, 'phoneNumber': None, 'others': None}]", ''))
          print(email + ' = ' + triade)

      #Deleting temporary txt file
      os.remove('out.txt')

#Launching the second program
if int(programchoice) == 2:
    print(colored('Paste the path to your email list.', 'yellow'))
    print(colored('[!] Delete every spaces in the name of the file,', 'red'))
    print(colored('[!] or/and at the end of the path.', 'red'))
    file = input(colored(' >>> ', 'yellow'))
    print(colored('\nResults (True = is used on Instagram - False = is not used on Instagram):\n', 'yellow'))
    with open(file, 'r') as f:
        #Making the program running in loop for each lines
        for line in f:
            email = line.rstrip()
            #Using holehe module
            async def main():
                out = []
                client = httpx.AsyncClient()

                await instagram(email, client, out)
                #Writing down the raw result in a temporary txt file
                with open('out.txt', 'w') as txt:
                    print(out, file=txt)

                await client.aclose()

            trio.run(main)

            tri = open('out.txt', 'rt')
            #Making some clear in the raw file response (just keeping the "True" or "False" of the 'exists:'
            for line in tri:
                  entri = (line.replace("[{'name': 'instagram', 'domain': 'instagram.com', 'method': 'register', 'frequent_rate_limit': True, 'rateLimit': False, 'exists': ", ''))
                  triade = (entri.replace(", 'emailrecovery': None, 'phoneNumber': None, 'others': None}]", ''))
                  print(email + ' = ' + triade)
                        
            #Deleting "out.txt" file
            os.remove('out.txt')

#Writing the list of problems happening to fill it in the help. If you found some problems, write them in the Issue section of this repo in Github and ill write them down here.
errorlist = (colored("[Prudence] * Error #1:\n   Getting 'email = [{'name': 'instagram', 'domain': 'instagram.com', 'method': 'register', 'frequent_rate_limit': True, 'rateLimit': True, 'exists': False' instead of 'email = True / False'\n\n   You used to many time the program and Instagram blocked your Ip to get these informations :/\n   Try to wait and try again later.", 'yellow'))

#Ask for help
needhelp = input(colored('Do you need help ?\n[1] - Yes\n[2] - No\n >>> ', 'red'))
if int(needhelp) > 2:
      print(colored('Invalid choice', 'red'))
if int(needhelp) < 1:
      print(colored('Invalid choice', 'red'))

if int(needhelp) == 1:
      print(errorlist)
