Q1: Que faut il ne pas oublier pour que le code s'execute? Que voyez vous au print?
R1 il faut passer sys.argv en argument à main lors de son apelle ,la console affiche `mainWindow.py execution du programme` c'est à dire l'argument passé  en ligne de commande et le print.


# 2e Etape: Créer une classe MainWindow

2.1: une erreur se produit à l'execution ? Que devez vous faire pour la corriger ?

R2.1:pour corriger l'erreur il faut appler le super constructeur de la classe mère 

Q2.2: Pourquoi la fenêtre ne s'affiche pas? que faut il rajouter?

R2.2: il faut creer une `QApplication()` et appler la méthode exec_() pour executer et afficher notre fenêtre.


# 3e Etape: rajouter des widgets à MainWindow






# 4e Etape: définir et connecter les slots

Q4: Comment connecter les actions aux slots ?
R4: on connecte les slot aux action 
`Action.Signal.connect ( Recepteur.slot )`
ici le signal est triggered


# 5e Etape: ouvrir une boîte de dialogue pour sélectionner un fichier

Q6: Le code ne s'execute pas correctement car vous n'avez pas acces au textEdit depuis la méthode open ou save. Comment résoudre ce problème?
R6 on peut résoudre ce problème en utilisant la method toHtml() du QTextEdit



# 6e Etape: ouvrir / sauver une page HTML






# 7e Etape: ouvrir une boîte de dialogue pour demander confirmation









