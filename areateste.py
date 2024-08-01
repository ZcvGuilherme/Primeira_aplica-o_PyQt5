import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QToolButton, QWidget, QVBoxLayout, QSizePolicy, QMenu, QAction, QLabel, QStackedLayout, QStackedWidget, QPushButton, QBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QRect
#CLASSE PARA TELA DOS EVENTOS
class TelaEventos(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.Tela_Widget_Evento()
    def Tela_Widget_Evento(self):
        layout = QHBoxLayout()
        left_side_layout = QVBoxLayout()

        left_side_layout.setSpacing(10)
        left_side_layout.setContentsMargins(10, 10, 10, 10)

        self.left_sidebar = QWidget()
        self.left_sidebar.setLayout(left_side_layout)
        self.left_sidebar.setStyleSheet('''
                    background-color: #B0E0E6;
                    border: 1px solid black;
                    border-radius:5px
                                        ''')
        self.left_sidebar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.left_sidebar.setMinimumSize(50, 50)
        self.botoes(layout=left_side_layout)

        #configura o widget
        self.WidEvento = QWidget()

        self.WidEvento.setStyleSheet('''
                background-color: #f5f5f5;  
                border: 1px solid #d0d0d0;  
                border-radius: 5px;         
                padding: 10px;              
                margin: 20px;               
                font-family: Arial, sans-serif; 
                font-size: 14px;           
                color: #333333;
                text-align: center;         
                ''')
        self.WidEvento.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.evento_layout = QVBoxLayout()
        self.evento_layout.addWidget(QLabel('                                                  CONTEUDO DO WID GRANDE'))
        self.WidEvento.setLayout(self.evento_layout)

        layout.addWidget(self.left_sidebar)
        layout.addWidget(self.WidEvento)

        self.setLayout(layout)
    def botoes(self, layout):
        #---------------BOTAO-------------------#
        botao_1 = QPushButton('Adicionar\n Evento')
        botao_1.setStyleSheet('''
                QPushButton{
                    background-color: #4CAF50;
                    border: 1px solid black;
                    border-radius: 5px;
                    font-size: 16px;
                    text-align: center;
                              }
                QPushButton:hover {
                    background-color: #45A049;
                              }
                QPushButton:pressed{
                    background-color: #388E3C;
                              }
                            ''')
        botao_1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        botao_1.setMinimumSize(QSize(100, 100))
        botao_1.clicked.connect(self.click_button)
        layout.addWidget(botao_1, alignment=Qt.AlignTop)
        #------------------------------------------#
        botao_2 = QPushButton('Remover')
        botao_2.setStyleSheet('''
                QPushButton{
                    background-color: #F44336; 
                    border: 1px solid black;
                    border-radius: 5px; 
                    font-size: 16px;
                    text-align: center;
                              }
                QPushButton:hover {
                    background-color: #E53935;
                              }
                QPushButton:pressed{
                    background-color: #D32F2F;
                              }
                            ''')
        botao_2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        botao_2.setMinimumSize(QSize(100, 100))
        
        botao_2.clicked.connect(self.click_button)
        layout.addWidget(botao_2, alignment=Qt.AlignTop)
        #-----------------------BOTAO 3---------------------------#
        botao_3 = QPushButton('Modificar')
        botao_3.setStyleSheet('''
                QPushButton{
                    background-color: #2196F3;
                    border: 1px solid black;
                    border-radius: 5px;
                    font-size: 16px;
                    text-align: center;
                              }
                QPushButton:hover {
                    background-color: #1976D2;
                              }
                QPushButton:pressed{
                    background-color: #1565C0;
                              }
                            ''')
        botao_3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        botao_3.setMinimumSize(QSize(100, 100))
        botao_3.clicked.connect(self.click_button)
        layout.addWidget(botao_3, alignment=Qt.AlignTop)
        #-----------------------------#BOTAO 4#---------------------------------#
        botao_4 = QPushButton('Ajustes\nEvento')
        botao_4.setStyleSheet('''
                QPushButton{
                    background-color: #FF9800;
                    border: 1px solid black;
                    border-radius: 5px;
                    font-size: 16px;
                    text-align: center;
                              }
                QPushButton:hover {
                    background-color: #F57C00;
                              }
                QPushButton:pressed{
                    background-color: #EF6C00;
                              }
                            ''')
        botao_4.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        botao_4.setMinimumSize(QSize(100, 100))
        botao_4.clicked.connect(self.click_button)
        layout.addWidget(botao_4, alignment=Qt.AlignTop)
    def click_button(self):
        print('Clicou!!!')
#CLASSE PARA TELA DOS DADOS 
class Tela_Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.configura_tela()
        self.configura_toolbar()
        self.cria_telas()
    def configura_tela(self):
        #---------------------------CONFIGURAÇÃO TELA------------------------#
        self.setWindowTitle('Primeira Aplicação')
        self.setWindowIcon(QIcon('icone.png'))
        self.setGeometry(300, 100, 800, 600)
        self.setStyleSheet('''
                background-color: white;
                           ''')
        self.setMinimumSize(300, 300)
    def configura_toolbar(self):
        self.toolbar = QToolBar('EasterEgg YaY')
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setStyleSheet('''
                QToolButton {
                    text-align: center;
                    border: 1px solid #d0d0d0;
                    border-radius: 5px;
                    padding: 5px;
                             }
                QToolButton:hover {
                    background-color: #F8F8FF
                                   }
                QToolButton:pressed {
                    background-color: #F0F8FF
                                   }
                             ''')
        #espaçadores aqui:
        spacer_left = QWidget()
        spacer_right = QWidget()
        spacer_left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        spacer_right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.toolbar.addWidget(spacer_left)

        #----------------------#BOTAO 1#--------------------#
        botao1 = QToolButton()
        botao1.setText('Eventos')
        botao1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        botao1.setMinimumSize(QSize(100, 30))
        botao1.clicked.connect(self.abrir_tela_eventos)
        self.toolbar.addWidget(botao1)
        botao1.setPopupMode(QToolButton.InstantPopup)

        #----------------------#BOTAO 2#--------------------#
        botao2 = QToolButton()
        botao2.setText('Dados')
        botao2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        botao2.setMinimumSize(QSize(100, 30))
        self.toolbar.addWidget(botao2)
        #---------------------#MENU 2#-----------------------#
        menu2 = QMenu()
        menu2.setStyleSheet('''
                QMenu {
                    border: 1px solid black;
                    border-radius: 5px;
                        }
                QMenu::item{
                    padding: 0 10px;
                    min-height: 30px;
                    text-align: center;
                            }
                QMenu::item:selected {
                    background-color: #87CEFA;
                    color: black;
                           }
                QMenu::item:disabled {
                    color: #d0d0d0;
                           }
                           ''')
        exportar_menu = QMenu('Exportar', self)
        exportar_menu.setStyleSheet('''
                QMenu {
                border: 1px solid black;
                border-radius: 5px;
            }
            QMenu::item {
                padding: 0 10px;
                min-height: 30px;
                text-align: center;
            }
            QMenu::item:selected {
                background-color: #87CEFA;
                color: black;
            }
            QMenu::item:disabled {
                color: #d0d0d0;
            }
                                    ''')
        exportar_menu.addActions([
            QAction('CSV', self),
            QAction('PDF', self),
            QAction('JSON', self)
        ])
        menu2.addMenu(exportar_menu)
        actions = [
            QAction('Importar', self),
            QAction('Vizualização HTML', self)
        ]
        menu2.addActions(actions)

        botao2.setMenu(menu2)
        botao2.setPopupMode(QToolButton.InstantPopup)
        #----------------------#BOTAO 3#--------------------#
        botao3 = QToolButton()
        botao3.setText('Clientes')
        botao3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        botao3.setMinimumSize(QSize(100, 30))
        self.toolbar.addWidget(botao3)

        #----------------------#BOTAO 4#--------------------#
        botao4 = QToolButton()
        botao4.setText('Configurações')
        botao4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        botao4.setMinimumSize(QSize(100, 30))
        self.toolbar.addWidget(botao4)

        menu4 = QMenu()
        menu4.setStyleSheet('''
                    QMenu {
                        border: 1px solid black;
                        border-radius: 5px;
                            }
                    QMenu::item{
                        padding: 0 10px;
                        min-height: 30px;
                        text-align: center;
                                }
                    QMenu::item:selected {
                        background-color: #87CEFA;
                        color: black;
                            }
                    QMenu::item:disabled {
                        color: #d0d0d0;
                            }
                            ''')
        botao_ajustes = QAction('Ajustes', self)
        #botao_ajustes.triggered.connect(self.abrir_tela_ajustes)
        botao_ajuda = QAction('Ajuda', self)
        #botao_ajuda.triggered.connect(self.)
        actions = [
            botao_ajustes,
            botao_ajuda
          ]
        menu4.addActions(actions)
        
        botao4.setMenu(menu4)
        botao4.setPopupMode(QToolButton.InstantPopup)

        self.toolbar.addWidget(spacer_right)
    def cria_telas(self):
        #QStackedWidget para Widgets que ficam alternando entre eles
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        #------------declaração das telas--------------------------#
        self.tela_eventos = TelaEventos()
        #--------------CHAMAR AS TELAS---------------------#
        self.stacked_widget.addWidget(self.tela_eventos)
    #--------------------BOTOES FUNÇÕES PRINCIPAIS-----------------------#
    def abrir_tela_eventos(self):
        self.stacked_widget.setCurrentWidget(self.tela_eventos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Tela_Principal()
    main_window.show()
    sys.exit(app.exec_())