import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import inquirer
import numpy as np
import sqlite3





class Sequence:
    def __init__(self):
        global variable
        global cur
        variable = {}
        con = sqlite3.connect("Math_Expression.db")
        cur = con.cursor()
        plt.ion()
        plt.rcParams['text.usetex'] = True
        plt.pause(0.0001)
        while True :
            operation = [inquirer.List
                          ("Que souhaitez-vous faire ?",
                           message="Que souhaitez-vous faire ?",
                           choices=['Suite', 'Fonction','Operation','Quitter'])]
            answers = inquirer.prompt(operation)
            if (answers["Que souhaitez-vous faire ?"]=="Suite"):
                self.ajouter_suite()
            elif (answers["Que souhaitez-vous faire ?"]=="Quitter"):
                break
    def ajouter_suite(self):
        while True:
            if len(variable) > 0:
                for suite in variable:
                    print(suite + " : " + variable[suite]["Expression"])
            expression = [inquirer.List
                          ("Suite",
                           message="[+] : ajouter une suite         [-] : supprimer une suite",
                           choices=['[+]', '[-]','Retour'])]
            answers = inquirer.prompt(expression)
            if answers['Suite'] == 'Retour':
                break
            elif answers['Suite'] == '[+]':
                sequence = [inquirer.List
                            ('Choix de l\'expression',
                             message="Quelle sera la forme de la suite ?",
                             choices=['Explicite', 'Récurrente'])]
                answers = inquirer.prompt(sequence)

                if answers['Choix de l\'expression'] == 'Récurrente':
                    name = input("nom de la variable :")
                    variable[name] = self.recurrence_sequence(name)
                if answers['Choix de l\'expression'] == 'Explicite':
                    name = input("nom de la variable :")
                    variable[name] = self.explicite_sequence(name)
            elif answers['Suite']=='[-]':
                delete = [inquirer.List
                            ('Choix de l\'expression',
                             message="Quelle sera la forme de la suite ?",
                             choices=[i for i in variable])]
                answer = inquirer.prompt(delete)
                if (variable[answer]!=None):
                    self.update(variable[answer])
    def explicite_sequence (self,name):
        u_0 = int(input("u_0 ="))
        u_n = (input(name + " : "))
        i = int(input("n="))
        value = []
        for n in range(i):
            value.append(eval(u_n))
        element = {"n": len(value), "Expression": u_n, "Valeur": value,"Modifiée":True}
        self.draw (element)
        return element
    def recurrence_sequence(self,name):
        u_0 = int(input("u_0 ="))
        u_n = u_0
        u_nplusun = (input(name + " : "))
        n = int(input("n="))
        value = [u_0]
        for i in range(n):
            u_n = eval(u_nplusun)
            value.append(u_n)
        element = {"n": len(value), "Expression": u_nplusun, "Valeur": value,"Modifiée":True}
        self.draw (element)
        return element

    def draw(self,element):
        #Graphique
        if (element!=None):
            n_max = []
            patch = []
            x = []
            y = []
            n_max.append(element["n"])
            col = (np.random.random(), np.random.random(), np.random.random())
            patch.append(mpatches.Patch(color=col, label=r'{}'.format(element["Expression"])))
            for i in range(element["n"]):
                x.append(i)
                y.append(element["Valeur"][i])
            plt.scatter(x, y, c=col)
            plt.draw()
        n_max = sorted(n_max)
        patch.append(mpatches.Patch(color='red', label=r'y=x'))
        plt.plot([i for i in range(n_max[-1])], [i for i in range(n_max[-1])], 'r')
        plt.legend(loc='upper right', handles=patch)
        #Base de donnée
e = Sequence()
