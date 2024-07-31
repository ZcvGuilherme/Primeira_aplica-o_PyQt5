import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QToolButton, QWidget, QVBoxLayout, QSizePolicy, QMenu, QAction, QLabel, QStackedLayout, QStackedWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QRect
#CLASSE PARA TELA DOS EVENTOS
class TelaEventos(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.Tela_Widget_Evento()
        self.botoes()
    def Tela_Widget_Evento(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel())
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
                ''')
        self.WidEvento.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.evento_layout = QVBoxLayout()

        self.WidEvento.setLayout(self.evento_layout)

        layout.addWidget(self.WidEvento)

        self.setLayout(layout)
    def botoes(self):
        #---------------BOTAO-------------------#
        botao_1 = QPushButton('botao 1')
        botao_1.setStyleSheet('''
                QPushButton{
                    border: 1px solid black;
                    border-radius: 5px;
                    font-size: 16px;
                              }
                QPushButton:hover {
                    background-color: #FFE4B5;
                              }
                QPushButton:pressed{
                    background-color: #FFDAB9;
                              }
                            ''')
        botao_1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        botao_1.setMinimumSize(QSize(200, 70))
        botao_1.clicked.connect(self.click_button)

        #------------------------------------------#
        self.evento_layout.addWidget(botao_1, alignment=Qt.AlignRight)
    def click_button(self):
        print('Clicou!!!')
#CLASSE PARA TELA DOS DADOS 
class TelaDados(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Tela de Dados'))
        self.setLayout(layout)
#CLASSE PARA TELA CLIENTES
class TelaClientes(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Tela de Clientes'))
        self.setLayout(layout)
#CLASSE PARA TELA CONFIGURAÇÕES
class TelaConfig(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Tela de Ajustes'))
        self.setLayout(layout)


class Tela_pricipal(QMainWindow):
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
        self.toolbar.addWidget(botao1)
        #-----------------------------------#MENU 1#-------------------------------------#
        menu = QMenu()
        menu.setStyleSheet('''
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
        actions = [
            QAction('Adicionar', self),
            QAction('Deletar', self),
            QAction('Modificar', self),
            QAction('Gerenciar', self)
        ]
        menu.addActions(actions)

        botao1.setMenu(menu)
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
        botao3.clicked.connect(self.mostrar_tela_clientes)
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
        botao_ajustes.triggered.connect(self.abrir_tela_ajustes)
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
        self.tela_dados = TelaDados()
        self.tela_clientes = TelaClientes()
        self.tela_configurações = TelaConfig()
        #--------------CHAMAR AS TELAS---------------------#
        self.stacked_widget.addWidget(self.tela_eventos)
        self.stacked_widget.addWidget(self.tela_dados)
        self.stacked_widget.addWidget(self.tela_clientes)
        self.stacked_widget.addWidget(self.tela_configurações)
    #--------------------BOTOES FUNÇÕES PRINCIPAIS-----------------------#
    def abrir_tela_ajustes(self):
        self.stacked_widget.setCurrentWidget(self.tela_eventos)
    def mostrar_tela_dados(self):
        self.stacked_widget.setCurrentWidget(self.tela_dados)
    def mostrar_tela_clientes(self):
        self.stacked_widget.setCurrentWidget(self.tela_clientes)
        print('botao apertado')
    def mostrar_tela_config(self):
        self.stacked_widget.setCurrentWidget(self.tela_configurações)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Tela_pricipal()
    main_window.show()
    sys.exit(app.exec_())