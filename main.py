from obj.questlog import Quest_log

liste = Quest_log('le kk')

liste.add_objective('Acheter des bananes')
liste.add_objective('KK')

liste.check_objective(0)

print(liste)
