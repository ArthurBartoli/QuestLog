from questlog import QuestLog

class Category():
    '''A category is a subfolder of a QuestLog and contains itself another QuestLog'''
    def __init__(self, title, ql_title, ql_parent, ql_desc=''):
        self.title = title
        self.questlog = QuestLog(ql_title, desc=ql_desc)
        self.ql_parent = ql_parent
        self._pos_parent = self.ql_parent.search_log(self.title)

    def __str__(self):
        return f"{self.questlog}"

    def __len__(self):
        return len(self.questlog)

    # Reader Functions
    def read_title(self):
        return self.title

    def read_ql_title(self):
        return self.questlog.read_name()

    def read_desc(self):
        return self.questlog.read_desc()

    # Access Functions
    def change_title(self, title):
        self.title = title
    
    def change_ql(self, ql_title, ql_desc):
        self.questlog = QuestLog(ql_title, desc=ql_desc)
    
    def change_parent(self, new_parent):
        self.ql_parent.remove_category(self)
        self.ql_parent = new_parent
        self.ql_parent.add_category(self)
        self._pos_parent = self.ql_parent.search_log(self.title)
    
    def correct_pos(self):
        self._pos_parent = self.ql_parent.search_log(self.title)
        
