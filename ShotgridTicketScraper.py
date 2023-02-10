import shotgun_api3
# studio_globals will need to replaced with your studio's global module that contains your entities
import studio_globals
import re
import pyperclip

# the following will need to be replaced with your shotgrid connection info
SG = Shotgun('https://my-site.shotgrid.autodesk.com', 'script_name', '0123456789abcdef0123456789abcdef0123456')

def scrape():
    ticketNumber = int(re.search('[0-9]+', ticketLink).group(0))

    filters = [['id', 'is', ticketNumber]]
    fields = ['title', 'description']
    result = SG.find_one(studio_globals.TICKET, filters, fields)

    print('TICKET ID INPUTTED: ' + str(result['id']))
    print('TICKET TITLE: ' + result['title'])

    return result

# Takes the ticket entity from scrape(), then finds and returns any file paths
def filter(raw_ticket):
    data = scrape(raw_ticket)
    slashList = ["\\", "//", "/"]
    if any(slashes in data['description'] for slashes in slashList):
        print('\nPaths were found')
        filteredPaths = re.findall('\\\\.*|//.*', data['description'])
        organizedPaths = '\n'.join(filteredPaths)
        return organizedPaths
    else:
        print('No paths found')

# Takes the file paths from filter(), and converts them to zsh format for Isilon
def convert():
    ticketURL = (input('Enter the ticket URL:'))
    paths = filter(ticketURL)
    print(paths)

    storageServer = input("Enter the storage server this data belongs to:")
    if storageServer not in paths:
        print("Warning: " + storageServer + " was not found in one or more paths. Check the paths and try again")
        convert()
    flipSlashes = paths.replace("\\", "/")
    addIfs = flipSlashes.replace(storageServer, "ifs")
    final = addIfs.replace("//", "/")

    print("\n \n" + final)
    pyperclip.copy("\n \n" + final)
    print("The converted output has been copied to your clipboard")
    print("Delete this data on " + storageServer)
    convert()

convert()