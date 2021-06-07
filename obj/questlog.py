'''This contains the definition of the quest_log class.'''

from .objective import Objective
import regex as re

class QuestLog():
    '''Object that acts as an interactive list. Can have nested Quest logs.
    The element of each list is an objective object.'''

    OBJ = []    # Contains the main listing.

    def __init__(self, name):
        self.name = name

    def __str__(self):
        '''When printed, the object returns a listing of the current
        objectives.
        '''
        if self.OBJ == 0:
            print("There are no objectives in this Quest Log.")
            return None
        temp = []
        temp.append(f"=== {self.name} :")
        for item in self.OBJ:
            temp.append(f"{item}")
        return "\n".join(temp)

    def __len__(self):
        return len(self.OBJ)

    # Reader Functions
    def show_list(self):
        '''Prints the contents of the list.
        Not tested as it's for debug purposes only :P
        '''
        if len(self.OBJ) == 0:
            print("There are no objectives in this Quest Log.")
        else:
            print(f"=== {self.name} :")
            for item in self.OBJ:
                print(f"{item}")

    def is_done(self, pos):
        '''Return true or false if the objective at the given pos is done.'''
        temp = self.OBJ[pos]
        return temp.is_done()

    def read_quantity(self, pos):
        '''Returns a list of quantity and max quantity of the objective
        at position pos in the list of objectives.
        '''
        temp = self.OBJ[pos]
        return temp.read_quantity()

    def read_desc(self, pos):
        '''Returns a string containing the description of the objective
        at position pos in the list of objectives.
        '''
        temp = self.OBJ[pos]
        return temp.read_desc()

    def read_name(self):
        return self.name

    def read_title(self, pos):
        '''Returns a string containing the title of the objective at
        position pos in the list of objectives.
        '''
        temp = self.OBJ[pos]
        return temp.read_title()

    # Access methods
    def add_objective(self, obj_title, qty=0, desc=""):
        '''Adds an objective. Needs to be a string !! Will soon integrate
        quantities.
        '''
        if not isinstance(obj_title, str):
            raise TypeError("Only text is allowed as objective title !")

        obj = Objective(obj_title, qty=qty, desc=desc)

        self.OBJ.append(obj)

    def add_category(self, category):
        self.OBJ.append(category)

    def remove_category(self, category):
        try:
            self.OBJ.remove(category)
        except ValueError:
            print(f"No {category.read_title()} in the {self.read_name()} Quest Log.")


    def change_desc(self, pos, desc):
        '''Changes the description of an objective at a given position.'''
        temp = self.OBJ[pos]
        temp.change_desc(desc)

    def change_title(self, pos, title):
        '''Changes the title of an objective at a given position'''
        temp = self.OBJ[pos]
        temp.change_title(title)

    def change_quantity(self, pos, qty):
        '''Changes the quantity of an objective at a given position to q'''
        temp = self.OBJ[pos]
        temp.change_quantity(qty)

    def change_max_quantity(self, pos, qty_max):
        '''Changes the max quantity of an objective at a given position to q_max.'''
        temp = temp = self.OBJ[pos]
        temp.change_max_quantity(qty_max)

    def make_quantitative(self, pos, qty):
        '''Makes quantitative an objective at a given position and sets the quantity to q.'''
        temp = self.OBJ[pos]
        temp.make_quantitative(qty)

    def unmake_quantitative(self, pos):
        '''Unmakes an objective at a given position not quantitative anymore.'''
        temp = self.OBJ[pos]
        temp.unmake_quantitative()

    def check_objective(self, pos):
        '''Takes the position of the objective in the list and checks objective.'''
        temp = self.OBJ[pos]
        temp.check()

    # Utils
    def search_log(self, keyword):
        '''Takes a log as input and outputs the position of the most similar
        log.
        IS NOT TO BE USED IN ANY OTHER CASE THAN ROBUSTNESS OF POS FETCHING
        '''

        temp2 = []
        word = [keyword]

        # Unwrapping the listing to extract objective's name
        for item in self.OBJ:
            temp2.append(item.read_title())

        if not isinstance(keyword, str):
            raise TypeError('Keyword needs to be a string !')

        # List of x where x is "all words from temp that match the keyword".
        temp = [x for x in temp2 if all(re.search(r".*{}.*".format(w), x) for w in word)]

        # Results
        try:
            return temp2.index(temp[0])
        except IndexError:
            print("No match found.")
