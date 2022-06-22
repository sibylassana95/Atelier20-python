devise = input("Devise : ")
montant = int (input ("Montant : "))
# 1 euro = 665 CFA
facteur_euro_CFA = 655
if devise == 'E' :
 print ("%f CFA" % (montant * facteur_euro_CFA))
elif devise == 'CFA' :
 print ("%f Euros" % (montant / facteur_euro_CFA))
else :
 print ("Je n'ai rien compris") # affichage d'un message d'erreur
