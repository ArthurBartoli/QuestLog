from obj.questlog import QuestLog

liste = QuestLog('hello')

liste.add_objective('Acheter des bananes')
liste.add_objective('hello')

liste.check_objective(0)

print(liste)
