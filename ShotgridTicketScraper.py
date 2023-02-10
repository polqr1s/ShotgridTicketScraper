import shotgun_api3
# studio_globals will need to replaced with your studio's global module that contains your entities
import studio_globals
import re

# the following will need to be replaced with your shotgrid connection info
SG = Shotgun('https://my-site.shotgrid.autodesk.com', 'script_name', '0123456789abcdef0123456789abcdef0123456')

def scrape():
    ticketNumber = int(ticketLink.split('/')[-1])

    filters = [['id', 'is', ticketNumber]]
    fields = ['title', 'description']
    result = SG.find_one(studio_globals.TICKET, filters, fields)

    print('TICKET ID INPUTTED: ' + str(result['id']))
    print('TICKET TITLE: ' + result['title'])

    return result

ticket = (input('Enter the ticket URL:'))
data = scrape(ticket)

# use below to print the entire ticket description for testing
# print('\nFull Description: \n' + data['description'])

slashList = ["\\", "//", "/"]
if any(slashes in data['description'] for slashes in slashList):
    print('\nPaths were found:')
    filter = re.findall('\\\\.*', data['description'])
    print(*filter, sep = "\n")
else:
    print('No paths found')