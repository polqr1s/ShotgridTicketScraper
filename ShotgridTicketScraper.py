

import shotgun_api3
#studio_globals will need to replaced with your studio's global module that contains your entities
import studio_globals

#the following will need to be replaced with your shotgrid connection info
SG = Shotgun('https://my-site.shotgrid.autodesk.com', 'script_name', '0123456789abcdef0123456789abcdef0123456')

def scrape():
    ticketLink = (input('Enter the ticket URL:'))
    ticketNumber = int(ticketLink.split('/')[-1])

    filters = [['id', 'is', ticketNumber]]
    fields = ['title', 'description']
    result = SG.find_one(studio_globals.TICKET, filters, fields)

    print('Title: \n' + result['title'])
    print('Ticket ID: \n' + str(result['id']))
    print('Description: \n' + result['description'])

    scrape()

scrape()