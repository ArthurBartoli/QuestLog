from obj.questlog import QuestLog

liste = QuestLog('le kk')

liste.add_objective('Acheter des bananes')
liste.add_objective('KK')

liste.check_objective(0)

print(liste)
