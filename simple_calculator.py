from PySide2 import QtGui, QtWidgets
from functools import partial
from calcul_s.simple_calculator import Ui_calculator
import math


class Simple_Calculator(Ui_calculator, QtWidgets.QWidget):
    def __init__(self):
        super(Ui_calculator, self).__init__()

        self.mem = ''
        self.btns_nombres = []
        self.setupUi(self)
        self.buttonPressed()
        self.modificationSetupUi()
        self.setupConnections()
        self.setupRaccourciClavier()
        self.memories()
        self.css()
        self.show()

    def modificationSetupUi(self):

        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setStyleSheet('QPushButton:hover {color: White;'
                                     'background-color: white;}')
                # widget.setFont(Custom_font)
            if isinstance(widget, QtWidgets.QPushButton) and widget.text().isdigit():
                self.btns_nombres.append(widget)

    def setupConnections(self):
        for btn in self.btns_nombres:
            btn.clicked.connect(partial(self.btnNombrePressed, str(btn.text())))

        self.btn_moins.clicked.connect(partial(self.btnOperationPressed, str(self.btn_moins.text())))
        self.btn_plus.clicked.connect(partial(self.btnOperationPressed, str(self.btn_plus.text())))
        self.btn_mult.clicked.connect(partial(self.btnOperationPressed, str(self.btn_mult.text())))
        self.btn_div.clicked.connect(partial(self.btnOperationPressed, str(self.btn_div.text())))
        self.btn_log.clicked.connect(self.log)
        self.btn_sin.clicked.connect(self.sin)
        self.btn_cos.clicked.connect(self.cos)
        self.btn_tan.clicked.connect(self.tan)
        self.btn_exp.clicked.connect(self.exp)
        self.btn_racine.clicked.connect(self.wurzel)
        self.btn_puissance.clicked.connect(self.puissance)
        self.btn_degree.clicked.connect(self.degree)
        self.btn_percent.clicked.connect(partial(self.btnOperationPressed, str(self.btn_percent.text())))
        self.btn_inv.clicked.connect(self.inversed)
        self.btn_off.clicked.connect(self.close)
        self.btn_mr.clicked.connect(self.memoriesR)
        self.btn_mc.clicked.connect(self.memories)
        self.btn_mPlus.clicked.connect(self.memoriesP)
        self.btn_backspace.clicked.connect(self.buttonPressed)

        self.btn_equal.clicked.connect(self.calculOperation)
        self.btn_reset.clicked.connect(self.supprimerResultat)

    def setupRaccourciClavier(self):
        for btn in range(10):
            QtWidgets.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self.btnNombrePressed, str(btn)))
        # for btns in :

        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_plus.text())), self,
                            partial(self.btnOperationPressed, str(self.btn_plus.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_moins.text())), self,
                            partial(self.btnOperationPressed, str(self.btn_moins.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_div.text())), self,
                            partial(self.btnOperationPressed, str(self.btn_div.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence(str(self.btn_mult.text())), self,
                            partial(self.btnOperationPressed, str(self.btn_mult.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence('Enter'), self, self.calculOperation)
        QtWidgets.QShortcut(QtGui.QKeySequence('Del'), self, self.supprimerResultat)
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self, self.close)
        QtWidgets.QShortcut(QtGui.QKeySequence('Backspace'), self, self.buttonPressed)
        QtWidgets.QShortcut(QtGui.QKeySequence('.'), self,
                            partial(self.btnOperationPressed, str(self.btn_point.text())))

    def btnOperationPressed(self, operation):
        """
        Fonction activee quand l'utilisateur appuie sur
        une touche d'operation (+, -, /, *)
        """

        # On recupere le texte dans le LineEdit operation
        operationText = str(self.operation.text())
        # On recupere le texte dans le LineEdit resultat
        resultats = str(self.resultat.text())

        # On additionne l'operation en cours avec le texte dans le resultat
        # et on ajoute a la fin le signe de l'operation qu'on a choisie
        if resultats == '0':
            self.resultat.setText(operationText + operation)
        elif operationText == '':
            self.resultat.setText(operationText + resultats + operation)
        else:
            self.resultat.setText(resultats + operation)

    def buttonPressed(self):
        get = str(self.resultat.text())
        if len(get) == 1:
            self.resultat.setText('0')
        else:
            self.resultat.setText(get[:-1])

    def inversed(self):
        state = self.btn_inv.text()
        if state == 'Inv':
            self.btn_cos.setText('cos^-1')
            self.btn_sin.setText('sin^-1')
            self.btn_tan.setText('tan^-1')
            self.btn_inv.setText('inv')
        else:
            self.btn_cos.setText('cos')
            self.btn_sin.setText('sin')
            self.btn_tan.setText('tan')
            self.btn_inv.setText('Inv')

    def btnNombrePressed(self, bouton):
        """Activated when we press 0 .. 9"""

        # On recupere le texte dans le LineEdit resultat
        resultats = str(self.resultat.text())

        if resultats == '0' or resultats == '':
            # Si le resultat est egal a 0 on met le nombre du bouton
            # que l'utilisateur a presse dans le LineEdit resultat
            self.resultat.setText(bouton)
        else:
            # Si le resultat contient autre chose que zero,
            # On ajoute le texte du bouton a celui dans le LineEdit resultat
            self.resultat.setText(resultats + bouton)

    def supprimerResultat(self):
        """On reset le texte des deux LineEdit"""

        self.resultat.setText('0')
        self.operation.setText('')

    def calculOperation(self):
        # On recupere le texte dans le LineEdit resultat
        resultats = str(self.resultat.text())

        # On ajoute le nombre actuel dans le LineEdit resultat
        # au LineEdit operation
        if self.operation.text() == '':
            str(self.operation.setText(self.operation.text() + resultats))
        str(self.operation.setText(resultats))
        res = self.operation.text()
        self.resultat.setText(str(eval(res)))

    def puissance(self):
        get = self.resultat.text()
        self.operation.setText('10^(' + get + ')')
        res = str(math.pow(10, float(eval(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def degree(self):
        if self.btn_degree.text() == 'Deg':
            self.btn_degree.setText('Grd')
        elif self.btn_degree.text() == 'Grd':
            self.btn_degree.setText('Deg')

    def wurzel(self):
        get = (self.resultat.text())
        self.operation.setText('√' + str(get))
        res = str(math.sqrt(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def sin(self):
        state = self.btn_sin.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'sin':
            if self.btn_degree.text() != 'Deg':
                res = str(math.sin(eval(str(math.degrees(float(eval(get)))))))
            else:
                res = str(math.sin(eval(str(get))))
        else:
            res = str(math.asin(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def cos(self):
        state = self.btn_cos.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'cos':
            res = str(math.cos(eval(str(get))))
        else:
            res = str(math.acos(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def tan(self):
        state = self.btn_tan.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'tan':
            res = str(math.tan(eval(str(get))))
        else:
            res = str(math.atan(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def log(self):
        state = self.btn_log.text()
        get = (self.resultat.text())
        self.operation.setText(state + '(' + str(get) + ')')
        if state == 'log':
            res = str(math.log10(eval(str(get))))
        else:
            res = str(math.pow(10, eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def exp(self):
        # state = self.btn_log.text()
        get = (self.resultat.text())
        self.operation.setText('e^(' + str(get) + ')')
        res = str(math.exp(eval(str(get))))
        if res.endswith('.0'):
            self.resultat.setText(res[:-2])
        else:
            self.resultat.setText(res)

    def memories(self):
        self.mem = self.resultat.text()

    def memoriesR(self):
        try:
            self.resultat.setText(self.mem)
        except IndexError:
            print('Keine Daten wurden gespeichert')

    def memoriesP(self):
        if self.resultat.text() == '':
            self.operation.setText(self.mem)
            self.resultat.setText(self.mem)
        else:
            self.operation.setText(self.mem + '+' + self.resultat.text())
            self.resultat.setText(str(int(self.mem) + int(self.resultat.text())))

    def css(self):
        self.setStyleSheet('''
        background-color: #86c2fe;
        ''')
        self.resultat.setStyleSheet('''
        background-color: White;
        color: sky;
        ''')
        self.operation.setStyleSheet('''
        background-color: white;
        ''')


app = QtWidgets.QApplication([])
win = Simple_Calculator()
app.exec_()
