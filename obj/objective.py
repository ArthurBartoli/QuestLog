'''This contains the definition of the Objective class.'''

class Objective():
    '''An objective object is the basic element of a Questlog.
    Each has a title and a "done" string (which kinda acts as a flag too)
    There can also be a description (which presence is checked w/ =="")
    If a quantity is specified, then a quantity, a max quantity and a q flag is made.
    '''

    def __init__(self, title, qty=0, desc=""):
        self.title = title
        self.desc = desc
        self.done = "[ ]"

        self.qty = 0
        self.qty_max = 0
        self._qty_flag = False

        if qty != 0:
            self.qty = 0
            self.qty_max = qty
            self._qty_flag = True

    def __str__(self):
        if self.desc == "":
            if self._qty_flag:
                return f"{self.done} - {self.title} ({self.qty}/{self.qty_max})"
            return f"{self.done} - {self.title}"
        if self._qty_flag:
            return f"{self.done} - {self.title}: {self.desc} ({self.qty}/{self.qty_max})"
        return f"{self.done} - {self.title}: {self.desc}"

    # Reader Functions
    def read_obj(self):
        '''Function that prints all there is to know about the objective.'''
        if self.desc == "":
            if self._qty_flag:
                print(f"{self.done} ({self.qty}/{self.qty_max}) - {self.title}")
            else:
                print(f"{self.done} - {self.title}")
        else:
            if self._qty_flag:
                print(f"{self.done} ({self.qty}/{self.qty_max}) - {self.title}: {self.desc}")
            else:
                print(f"{self.done} - {self.title}: {self.desc}")

    def is_done(self):
        '''Returns True if the objective is done.'''
        if self.done == "[x]":
            return True
        else:
            return False

    def read_quantity(self):
        '''Returns a list of quantity and max quantity of the objective.'''
        if not self._qty_flag:
            print("This objective is not quantitative. Use make_quantitative to do so.")
            return None
        return [self.qty, self.qty_max]

    def read_desc(self):
        '''Returns description if there is any.'''
        return self.desc

    def read_title(self):
        '''Returns the title of the objective.'''
        return self.title

    # Access Functions
    def check(self):
        '''Checks the objective by replacing the done attribute
        of the data [ ] by [x].
        '''
        self.done = "[x]"

    def uncheck(self):
        '''Does the opposite of the check function.'''
        self.done = "[ ]"

    def change_title(self, title):
        '''Changes the title of the objective.'''
        self.title = title

    def change_desc(self, desc):
        '''Changes the description of the objective.'''
        self.desc = desc

    def change_quantity(self, qty):
        '''Changes the quantity of the objective.
        Checks it if qty >= qty_max.
        Unchecks it if qty < qty_max
        '''
        if not self._qty_flag:
            print(f"The objective '{self.title}' is not quantitative.")
            print("Please use the make_quantitative function to do so.")
            return False
        self.qty = qty
        if self.qty >= self.qty_max and not self.is_done():
            self.check()
            print(f"{self.qty}/{self.qty_max} - The objective '{self.title}' is now complete !")
            return None
        if self.qty < self.qty_max and self.is_done():
            self.uncheck()
            print(f"{self.qty}/{self.qty_max} - The objective '{self.title}' is now incomplete !")
            return None
        return None

    def change_max_quantity(self, qty_max):
        '''Changes the quantity of the objective.
        Checks it if q <= qty_max.
        Unchecks it if q > qty_max
        '''
        if not self._qty_flag:
            print(f"The objective '{self.title}' is not quantitative.")
            print("Please use the make_quantitative function to do so.")
            return False
        self.qty_max = qty_max
        if self.qty <= self.qty_max and self.is_done():
            self.uncheck()
            print(f"{self.qty}/{self.qty_max} - The objective '{self.title}' is now incomplete !")
            return None
        if self.qty > self.qty_max and not self.is_done():
            print(f"{self.qty}/{self.qty_max} - The objective '{self.title}' is now complete !")
            self.check()
            return None
        return None

    def make_quantitative(self, qty_max):
        '''Makes that objective quantitative'''
        if self._qty_flag:
            print(f"The objective '{self.title}' is already quantitative.")

        self.qty = 0
        self.qty_max = qty_max
        self._qty_flag = True
        self.uncheck()

    def unmake_quantitative(self):
        '''Makes that objective not quantitative'''
        if not self._qty_flag:
            print(f'The objective {self.title} is not quantitative.')
            print('Please use make_quantitative to do so.\n')

        self._qty_flag = False
        self.qty = 0
        self.qty_max = 0
