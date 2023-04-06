#AUTOR -> Rubén Mansanet 2on DAM SEMI
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys, math
from math import *



SCREEN_W = 400
SCREEN_H = 440

'''
#vista de la calculadora Cientifica
class calculadoraCientifica(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pràctica 2: Calculadora Científica")
        self.setGeometry(700, 100, SCREEN_W, SCREEN_H)

        #definim els layouts
        self.mainLayout = QVBoxLayout()
        self.buttonsLayout = QGridLayout()

        #self.mainLayout.setContentsMargins(5,5,5,5)
        self.mainLayout.setSpacing(3)
        self.buttonsLayout.setSpacing(2)

        #anyadim els layouts al widget
        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        #self.setCentralWidget(self.widget)
        self.mainLayout.addLayout(self.buttonsLayout)

        self.result = QLabel("(4+3)*2^3", self)#el text que se pasarà serà l'acció del cada botó apretat
        self.result.setWordWrap(True)
        self.result.setGeometry(5,45,390,50)
        self.result.setStyleSheet("QLabel {border:2px solid black;background:white;}")
        self.result.setAlignment(Qt.AlignRight)
        self.result.setFont(QFont("consolas", 35))

        self.fuente = QFont()
        self.fuente.setPointSize(15)

        operadors = ["^", "CE", "C", "Borrar", "sqtr", "PI", "^2", "n!", "(", ")", "%", "/", "*", "-", "+", "="]
        contadorOperacions = 0
        contadorNumeric = 7
        
        #print(len(operadors))

        for i in range(0, 10):
            for x in range(0, 4):
                if contadorOperacions<=10:
                    self.buttons = QPushButton(operadors[contadorOperacions])
                    self.buttons.setMinimumSize(0, 50)
                    self.buttonsLayout.addWidget(self.buttons, i , x)
                    contadorOperacions = contadorOperacions + 1
                    self.buttons.setFont(self.fuente)
                elif (i>2 and i<6) and (x<3):
                    self.buttons = QPushButton(str(contadorNumeric))
                    self.buttons.setMinimumSize(0, 50)
                    self.buttonsLayout.addWidget(self.buttons, i , x)
                    contadorNumeric = contadorNumeric+1
                    self.buttons.setFont(self.fuente)
                    if contadorNumeric == 10 or contadorNumeric == 7:
                        contadorNumeric = contadorNumeric - 6
                elif i>1 and x==3 and contadorOperacions>10 and contadorOperacions<16:
                    self.buttons = QPushButton(operadors[contadorOperacions])
                    self.buttons.setMinimumSize(0, 50)
                    self.buttonsLayout.addWidget(self.buttons, i , x)
                    contadorOperacions = contadorOperacions + 1
                    self.buttons.setFont(self.fuente)
                elif i == 6 and x >= 0 and x<3:
                    self.buttons = QPushButton("0")
                    self.buttons.setMinimumSize(0, 50)
                    self.buttonsLayout.addWidget(self.buttons, 6, 0, 1, 2)
                    self.buttons.setFont(self.fuente)
                    self.buttons = QPushButton(".")
                    self.buttons.setMinimumSize(0, 50)
                    self.buttonsLayout.addWidget(self.buttons, 6, 2)
                    self.buttons.setFont(self.fuente)


#vista de la calculadora estandar
class calculadoraEstandar(QWidget):
    def __init__(self):
        super().__init__()
'''        


#classe principal on anyadim les dos calculadores
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #self.window1 = calculadoraEstandar()
        #self.window2 = calculadoraCientifica()
        self.setWindowTitle("Pràctica 2: Calculadora Estandar")
        self.setGeometry(700, 100, SCREEN_W, SCREEN_H)

        #self.fuente dels botons
        self.fuente = QFont()
        self.fuente.setPointSize(15)
        
        
        #definim els layouts 
        self.mainLayout = QVBoxLayout()
        self.buttonsLayout = QGridLayout()

        

        self.mainLayout.setContentsMargins(5,45,5,5)
        self.mainLayout.setSpacing(3)
        self.buttonsLayout.setSpacing(2)

        #anyadim els layouts al widget
        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)
        self.mainLayout.addLayout(self.buttonsLayout)
        
        
        #creem els botons numèrics
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button0 = QPushButton("0")
       
        
        #botons del operadors i altres
        self.buttonSuma = QPushButton("+")
        self.buttonResta = QPushButton("-")
        self.buttonMult = QPushButton("*")
        self.buttonDiv = QPushButton("/")
        self.buttonDecimal = QPushButton(".")
        self.buttonIgual = QPushButton("=")
        self.buttonPercent = QPushButton("%")
        self.buttonParentesiObert = QPushButton("(")
        self.buttonParentesiTancat = QPushButton(")")
        self.buttonPotencia = QPushButton("^")
        self.buttonCE = QPushButton("CE")
        self.buttonC = QPushButton("C")
        self.buttonBorrar = QPushButton("Borrar")
        

        #anyadim els botons del gridlayout al widget
        #numèrics
        self.buttonsLayout.addWidget(self.button7, 2, 0)
        self.buttonsLayout.addWidget(self.button8, 2, 1)
        self.buttonsLayout.addWidget(self.button9, 2, 2)
        self.buttonsLayout.addWidget(self.button4, 3, 0)
        self.buttonsLayout.addWidget(self.button5, 3, 1)
        self.buttonsLayout.addWidget(self.button6, 3, 2)
        self.buttonsLayout.addWidget(self.button1, 4, 0)
        self.buttonsLayout.addWidget(self.button2, 4, 1)
        self.buttonsLayout.addWidget(self.button3, 4, 2)
        self.buttonsLayout.addWidget(self.button0, 5, 0, 1, 2)
        
        
        #operacions i altres
        self.buttonsLayout.addWidget(self.buttonSuma, 4, 3)
        self.buttonsLayout.addWidget(self.buttonResta, 3, 3)
        self.buttonsLayout.addWidget(self.buttonMult, 2, 3)
        self.buttonsLayout.addWidget(self.buttonDiv, 1, 3)
        self.buttonsLayout.addWidget(self.buttonIgual, 5, 3)
        self.buttonsLayout.addWidget(self.buttonDecimal, 5, 2)
        self.buttonsLayout.addWidget(self.buttonPercent, 1, 2)
        self.buttonsLayout.addWidget(self.buttonParentesiObert, 1, 0)
        self.buttonsLayout.addWidget(self.buttonParentesiTancat, 1, 1)
        self.buttonsLayout.addWidget(self.buttonPotencia, 0, 0)
        self.buttonsLayout.addWidget(self.buttonCE, 0, 1)
        self.buttonsLayout.addWidget(self.buttonC, 0, 2)
        self.buttonsLayout.addWidget(self.buttonPercent, 1, 2)
        self.buttonsLayout.addWidget(self.buttonBorrar, 0, 3)
        
        #Anyadim el tamany dels botons, la seua self.fuente i les entrades per teclat
        self.button1.setMinimumSize(0, 50)
        self.button1.setFont(self.fuente)
        self.button1.setShortcut("1")

        self.button2.setMinimumSize(0, 50)
        self.button2.setFont(self.fuente)
        self.button2.setShortcut("2")

        self.button3.setMinimumSize(0, 50)
        self.button3.setFont(self.fuente)
        self.button3.setShortcut("3")

        self.button4.setMinimumSize(0, 50)
        self.button4.setFont(self.fuente)
        self.button4.setShortcut("4")

        self.button5.setMinimumSize(0, 50)
        self.button5.setFont(self.fuente)
        self.button5.setShortcut("5")

        self.button6.setMinimumSize(0, 50)
        self.button6.setFont(self.fuente)
        self.button6.setShortcut("6")

        self.button7.setMinimumSize(0, 50)
        self.button7.setFont(self.fuente)
        self.button7.setShortcut("7")

        self.button8.setMinimumSize(0, 50)
        self.button8.setFont(self.fuente)
        self.button8.setShortcut("8")

        self.button9.setMinimumSize(0, 50)
        self.button9.setFont(self.fuente)
        self.button9.setShortcut("9")

        self.button0.setMinimumSize(0, 50)
        self.button0.setFont(self.fuente)
        self.button0.setShortcut("0")

        self.buttonSuma.setMinimumSize(0, 50)
        self.buttonSuma.setFont(self.fuente)
        self.buttonSuma.setShortcut("+")

        self.buttonResta.setMinimumSize(0, 50)
        self.buttonResta.setFont(self.fuente)
        self.buttonResta.setShortcut("-")

        self.buttonMult.setMinimumSize(0, 50)
        self.buttonMult.setFont(self.fuente)
        self.buttonMult.setShortcut("*")

        self.buttonDiv.setMinimumSize(0, 50)
        self.buttonDiv.setFont(self.fuente)
        self.buttonDiv.setShortcut("/")

        self.buttonDecimal.setMinimumSize(0, 50)
        self.buttonDecimal.setFont(self.fuente)
        self.buttonDecimal.setShortcut(".")

        self.buttonIgual.setMinimumSize(0, 50)
        self.buttonIgual.setFont(self.fuente)
        self.buttonIgual.setShortcut("Enter")

        self.buttonPercent.setMinimumSize(0, 50)
        self.buttonPercent.setFont(self.fuente)
        self.buttonPercent.setShortcut("p")

        self.buttonParentesiObert.setMinimumSize(0, 50)
        self.buttonParentesiObert.setFont(self.fuente)
        self.buttonParentesiObert.setShortcut(QKeySequence("shift+8"))

        self.buttonParentesiTancat.setMinimumSize(0, 50)
        self.buttonParentesiTancat.setFont(self.fuente)
        self.buttonParentesiTancat.setShortcut(QKeySequence("shift+9"))

        self.buttonPotencia.setMinimumSize(0, 50)
        self.buttonPotencia.setFont(self.fuente)
        self.buttonPotencia.setShortcut("space")
        #he ficat 'space' perque no se com ficar la tecla correcta amb el 'shift+grave_accent'

        self.buttonCE.setMinimumSize(0, 50)
        self.buttonCE.setFont(self.fuente)
        self.buttonCE.setShortcut("del")

        self.buttonC.setMinimumSize(0, 50)
        self.buttonC.setFont(self.fuente)
        self.buttonC.setShortcut("del")

        self.buttonBorrar.setMinimumSize(0, 50)
        self.buttonBorrar.setFont(self.fuente)
        self.buttonBorrar.setShortcut("backspace")


        #Requadre del resultat en el layout principal
        self.result = QLabel("(4+3)*2^3", self)#el text que se pasarà serà l'acció del cada botó apretat
        self.result.setWordWrap(True)
        self.result.setGeometry(5,50,390,50)
        self.result.setStyleSheet("QLabel {border:2px solid black;background:white;}")
        self.result.setAlignment(Qt.AlignRight)
        self.result.setFont(QFont("consolas", 35))
        
        #accions per a cada boto
        #números
        self.button1.clicked.connect(self.action1)
        self.button2.clicked.connect(self.action2)
        self.button3.clicked.connect(self.action3)
        self.button4.clicked.connect(self.action4)
        self.button5.clicked.connect(self.action5)
        self.button6.clicked.connect(self.action6)
        self.button7.clicked.connect(self.action7)
        self.button8.clicked.connect(self.action8)
        self.button9.clicked.connect(self.action9)
        self.button0.clicked.connect(self.action0)
        
        #operacions i altres
        self.buttonSuma.clicked.connect(self.actionSuma)
        self.buttonResta.clicked.connect(self.actionResta)
        self.buttonMult.clicked.connect(self.actionMult)
        self.buttonDiv.clicked.connect(self.actionDiv)
        self.buttonDecimal.clicked.connect(self.actionPunt)
        self.buttonPotencia.clicked.connect(self.actionPotencia)
        self.buttonParentesiObert.clicked.connect(self.actionParentesiObert)
        self.buttonParentesiTancat.clicked.connect(self.actionParentesiTancat)
        self.buttonCE.clicked.connect(self.actionCE)
        self.buttonC.clicked.connect(self.actionC)
        self.buttonBorrar.clicked.connect(self.actionBorrar)
        self.buttonIgual.clicked.connect(self.evaluar)
        

        #Main menu
        toolbar = QToolBar("Toolbar principal")
        self.addToolBar(toolbar)
        toolbar.addWidget(QLabel("Guardar Operacions"))
        self.saveData = QCheckBox()
        self.saveData.setCheckable(True)
        toolbar.addWidget(self.saveData)
        #self.statusBar(QStatusBar(self))

        self.saveData.clicked.connect(self.saveOperations)
        
        menu = self.menuBar()

        file_menu = menu.addMenu("&Aplicacions")
        
        buttonCalculadoraBasica = QAction("Estandar", self)
        buttonCalculadoraBasica.setStatusTip("Calculadora Estandar")
        buttonCalculadoraBasica.setCheckable(True)
        buttonCalculadoraBasica.triggered.connect(MainWindow)
        
        buttonCalculadoraCientifica = QAction("Científica", self)
        buttonCalculadoraCientifica.setStatusTip("Calculadora Científica")
        buttonCalculadoraCientifica.setCheckable(True)
        buttonCalculadoraCientifica.triggered.connect(self.calculadora)

        options = file_menu.addMenu("&Mode")
        options.addAction(buttonCalculadoraBasica)
        options.addAction(buttonCalculadoraCientifica)

        self.eixir = QAction("Eixir")
        menu.addAction(self.eixir)
        self.eixir.triggered.connect(self.close)

        

    #funcio per a evaluar el resultat
    def evaluar(self):
        evalua = self.result.text()

        try:
            evaluaResultat = eval(evalua)
            self.result.setText(str(evaluaResultat))
        except:
            self.result.setText("Error de la operació")  
        
        self.buttonIgual.clicked.connect(self.saveOperations)

    #funcions de les accions dels botons
    def action0(self):
        text = self.result.text()
        self.result.setText(text + "0")
        self.button0.clicked.connect(self.saveOperations)

    def action1(self):
        text = self.result.text()
        self.result.setText(text + "1")
        self.button1.clicked.connect(self.saveOperations)

    def action2(self):
        text = self.result.text()
        self.result.setText(text + "2")
        self.button2.clicked.connect(self.saveOperations)

    def action3(self):
        text = self.result.text()
        self.result.setText(text + "3")
        self.button3.clicked.connect(self.saveOperations)

    def action4(self):
        text = self.result.text()
        self.result.setText(text + "4")
        self.button4.clicked.connect(self.saveOperations)

    def action5(self):
        text = self.result.text()
        self.result.setText(text + "5")
        self.button5.clicked.connect(self.saveOperations)

    def action6(self):
        text = self.result.text()
        self.result.setText(text + "6")
        self.button6.clicked.connect(self.saveOperations)

    def action7(self):
        text = self.result.text()
        self.result.setText(text + "7")
        self.button7.clicked.connect(self.saveOperations)

    def action8(self):
        text = self.result.text()
        self.result.setText(text + "8")
        self.button8.clicked.connect(self.saveOperations)

    def action9(self):
        text = self.result.text()
        self.result.setText(text + "9")
        self.button9.clicked.connect(self.saveOperations)

    def actionSuma(self):
        text = self.result.text()
        self.result.setText(text + "+")
        self.buttonSuma.clicked.connect(self.saveOperations)

    def actionResta(self):
        text = self.result.text()
        self.result.setText(text + "-")
        self.buttonResta.clicked.connect(self.saveOperations)
    
    def actionMult(self):
        text = self.result.text()
        self.result.setText(text + "*")
        self.buttonMult.clicked.connect(self.saveOperations)

    def actionDiv(self):
        text = self.result.text()
        self.result.setText(text + "/")
        self.buttonDiv.clicked.connect(self.saveOperations)

    def actionPercent(self):
        text = self.result.text()
        self.result.setText(text + "%")
        self.buttonPercent.clicked.connect(self.saveOperations)

    def actionCE(self):
        self.result.setText("")

    def actionC(self):
        self.result.setText("") 
    
    def actionBorrar(self):
        text = self.result.text()
        self.result.setText(text[:len(text)-1])

    def actionPunt(self):
        text = self.result.text()
        self.result.setText(".")
        self.buttonDecimal.clicked.connect(self.saveOperations)

    def actionPotencia(self):
        text = self.result.text()
        self.result.setText(text + "^")
        self.buttonPotencia.clicked.connect(self.saveOperations)
    
    def actionParentesiObert(self):
        text = self.result.text()
        self.result.setText(text + "(")
        self.buttonParentesiObert.clicked.connect(self.saveOperations)

    def actionParentesiTancat(self):
        text = self.result.text()
        self.result.setText(text + ")")
        self.buttonParentesiTancat.clicked.connect(self.saveOperations)

    def actionRaizCuadrada(self):
        text = self.result.text()
        num = math.sqrt(float(text))
        self.result.setText(str(num))
        self.buttonRaizCuadrada.clicked.connect(self.saveOperations)

    def actionPI(self):
        num = round(2*acos(0.0), 8)
        self.result.setText(str(num))
        self.buttonPi.clicked.connect(self.saveOperations)

    def actionNumCuadrado(self):
        text = self.result.text()
        num = math.pow((float(text), 2))
        self.result.setText(str(num))
        self.buttonNumCuadrado.clicked.connect(self.saveOperations)
    
    def actionNumFactorial(self):
        text = self.result.text()
        num = math.factorial(float(text))
        self.result.setText(str(num))
        self.buttonNumFactorial.clicked.connect(self.saveOperations)


    def saveOperations(self):
        #print(self.saveData.isChecked())
        if self.saveData.isChecked() == True:
            if self.result.text != "":
                f = open("operacions.txt", "a")
                f.write(self.result.text())
                f.write("\n")

    #funcions per a eixir de la aplicació
    def closeEvent(self, event):
        close = QMessageBox.question(self, "Eixir", "Vols eixir de la aplicació?", 
        QMessageBox.Ok | QMessageBox.Cancel)
        if close == QMessageBox.Ok:
            event.accept()
        else:
            event.ignore()
    
        
    #calculadora científica
    def calculadora(self):
        self.buttonRaizCuadrada = QPushButton("sqrt")
        self.buttonPi = QPushButton("PI")
        self.buttonNumCuadrado = QPushButton("x^2")
        self.buttonNumFactorial = QPushButton("n!")

        self.buttonsLayout.addWidget(self.buttonRaizCuadrada, 7, 0)
        self.buttonsLayout.addWidget(self.buttonPi, 7, 1)
        self.buttonsLayout.addWidget(self.buttonNumCuadrado, 7, 2)
        self.buttonsLayout.addWidget(self.buttonNumFactorial, 7, 3)

        self.buttonRaizCuadrada.setMinimumSize(0, 50)
        self.buttonRaizCuadrada.setFont(self.fuente)
        self.buttonPi.setMinimumSize(0, 50)
        self.buttonPi.setFont(self.fuente)
        self.buttonNumCuadrado.setMinimumSize(0, 50)
        self.buttonNumCuadrado.setFont(self.fuente)
        self.buttonNumFactorial.setMinimumSize(0, 50)
        self.buttonNumFactorial.setFont(self.fuente)

        self.buttonRaizCuadrada.clicked.connect(self.actionRaizCuadrada)
        self.buttonPi.clicked.connect(self.actionPI)
        self.buttonNumCuadrado.clicked.connect(self.actionNumCuadrado)
        self.buttonNumFactorial.clicked.connect(self.actionNumFactorial)

  

if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()