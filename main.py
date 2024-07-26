import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, QGridLayout
from PyQt5.QtGui import QIcon

class Tela_pricipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.configura_tela()
        self.configura_widget()
        self.botoes()

    def configura_tela(self):
        #---------------------------CONFIGURAÇÃO TELA------------------------#
        self.setWindowTitle('Biblioteca PyQt5')
        self.setWindowIcon(QIcon('1200px-How_to_use_icon.png'))
        self.setGeometry(300, 100, 600, 600)
        self.setStyleSheet('''
                background-color: #191970;
                           ''')
        self.setMinimumSize(300, 300)

    def configura_widget(self):
        #-----------------------CONFIGURAÇÃO WIDGET---------------------#
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet('''
            QPushButton {
                background-color: white;
                color: black;
                padding: 10px;
                font-size: 16px
                           }
            QPushButton:hover {
                background-color: #FFE4E1;
                           }
            QPushButton:pressed {
                background-color: #FFF0F5;
                           }
                                          ''')
        self.layout1 = QGridLayout(self.central_widget)
        self.central_widget.setLayout(self.layout1)

        self.layout1.setColumnStretch(0, 1)
        self.layout1.setColumnStretch(1, 1)
        self.layout1.setRowStretch(0, 1)
        self.layout1.setRowStretch(1, 1)

    def botoes(self):
        #-------------------------BOTAO 1------------------------------#
        botao1 = QPushButton('LIVROS')
        botao1.clicked.connect(self.aperto_botao)
        self.layout1.addWidget(botao1, 0, 0)
        
        #--------------------------BOTAO 2-----------------------------#
        botao2 = QPushButton('FILMES')
        botao2.clicked.connect(self.aperto_botao)
        self.layout1.addWidget(botao2, 1, 2)

        #---------------------------------------------------------------#
    def aperto_botao(self):
        print('botao apertado')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Tela_pricipal()
    main_window.show()
    sys.exit(app.exec_())

