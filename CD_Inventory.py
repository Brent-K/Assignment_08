#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
#Brent Kieszling, 2020-Sep-03, Major updates include: Created CD class, added methods to IO: menu, menu choice, and add new cd.
#------------------------------------------#
import os
import pickle

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []
class CD:
    """Stores data about a CD:

    Args:
        cdNum: (int) CD collection ID
        cdTitle: (string) CD title
        cdArtist: (Artist) CD artist

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD

    methods:
        inventory (self): Returns the current attributes of the CD
        __str__(self): Customized string description of the object
    """
    # -- Fields -- #

    # -- Constructor -- #
    def __init__(self, cdNum, cdTitle, cdArtist):
        # -- Attributes -- #
        self.__order = cdNum
        self.__title = cdTitle
        self.__artist = cdArtist

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__order

    @cd_id.setter
    def cd_id(self, value):
        if str(value).isnumeric() == False:
            raise Exception('Integers only')
        else:
            self.__order = int(value)

    @property
    def cd_title(self):
        return self.__title

    @cd_title.setter
    def cd_title(self, value):
        if value.isstring():
            self.__title = value
        else:
            raise Exception('Not a valid input, string expected')

    @property
    def cd_artist(self):
        return self.__artist

    @cd_artist.setter
    def cd_artist(self, value):
        if value.isstring():
            self.__artist = value
        else:
            raise Exception('Not a valid input')

    # -- Methods -- #
    def inventory(self):
        return '{}\t{} (by:{})'.format(self.cd_id, self.cd_title, self.cd_artist)

    def __str__(self):
        return self.inventory()


# -- PROCESSING -- #
if os.path.exists(strFileName) != True:
    objFile = open(strFileName, 'ab')
    objFile.close()

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        write_file(file_name, lstCDs): Saves active list to binary file. No returns
        read_file(file_name, lstCDs): Returns a list of CD objects from the saved file

    """
    @staticmethod
    def read_file(file_name, lstCDs):
        """Function to import a list of objects (lstCDs) from a binary file.

        Args:
            file_name (string): name of file used to read the data from
            lstCDs (list of objects): list of CD objects to hold data during runtime.

        Returns:
            lstCDs (list of objects): list of CD objects
        """
        lstCDs.clear()
#The try statement handles an instance where there is no saved data
        try:
            with open(file_name, 'rb') as fileObj:
                lstCDs = pickle.load(fileObj)
        except:
            pass
        return lstCDs

    @staticmethod
    def write_file(file_name, lstCDs):
        """Function to save a list of objects (lstCDs) to a binary file

        Args:
            file_name (string): name of file used to read the data from
            lstCDs (list of objects): list of CD objects to hold data during runtime.

        Returns:
            None.
        """
        with open(file_name, 'wb') as fileObj:
                pickle.dump(lstCDs, fileObj)
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    """User interaction with the program
        Args:
        None.

    properties:
        None.

    methods:
        print_menu(): Displays menu options to user
        menu_choice(): Gets user menu choice. Returns the choice
        show_inventory(lstCDs): Displays each CD object in the current list of
            CDs.
        new_cd(): Gets user input for new CD information. Returns CD info.
        load_check(): Warns the user about the impact of loading and gives them 
            an option to stop. Returns a flag tracking the decision.
    """
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(lstCDs):
        """Displays current inventory table

        Args:
            lstCDs (list of objects): list of CD objects to hold data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lstCDs:
            print(row)
        print('======================================')

    @staticmethod
    def new_cd():
        """Allows the user to add a CD to the active inventory table

        Args:
            None.

        Returns:
            intID (interger): Serialized ID
            strTitle (string): Tittle of CD
            stArtist (string): Name of artist

        """
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID = input('Enter ID: ').strip()
        while True:
#This try handles the case where a non interger is entered
            try:
                intID = int(strID)
                break
            except:
                strID = input('Please enter an interger for the ID.')
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return intID, strTitle, stArtist

    @staticmethod
    def load_check():
        """Checks to see if the user wants to overwrite current data with saved data

        Args:
            None.

        Returns:
            flag (boolean): Tracks user response to the load check.

        """
        flag = False
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled. ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            flag = True
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        return flag



# -- Main Body of Script -- #

# Initialize the active list with saved data
lstOfCDObjects = FileIO.read_file(strFileName, lstOfCDObjects)

# start main loop
while True:
    IO.print_menu()
    strSlection = IO.menu_choice()
# exit first
    if strSlection == 'x':
        break

# load inventory
    if strSlection == 'l':
        answer = IO.load_check()
        if answer == True:
            lstOfCDObjects = FileIO.read_file(strFileName, lstOfCDObjects)
        else:
            pass
        pass

# add a CD
    elif strSlection == 'a':
        newCDID, newCDTitle, newCDArtist = IO.new_cd()
        objNewCD = CD(newCDID, newCDTitle, newCDArtist)
        lstOfCDObjects.append(objNewCD)
        continue  # start loop back at top.

# display current inventory
    elif strSlection == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

# save inventory to file
    elif strSlection == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')