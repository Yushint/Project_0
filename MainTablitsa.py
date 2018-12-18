import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QPushButton


# Наследование от QMainWindow, т.е. от главного окна приложения
class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100,100,100,100)
        self.setWindowTitle("Таблица Умножения") # заголовок окна
        
        self.button_1 = QPushButton(self)
        self.button_1.move(50,50)
        self.button_1.setText("Запустить?")
        self.button_1.clicked.connect(self.run)
        
        self.button_2 = QPushButton(self)
        self.button_2.move(50,20)
        self.button_2.setText("Выход")
        self.button_2.clicked.connect(self.run_2)
        self.show()
    def run(self):
        self.setMinimumSize(QSize(5,5))     #  мин.размеры
        central_widget = QWidget(self)                  # создаем центральный виджет
        self.setCentralWidget(central_widget)           # ставим центральный виджет

        grid_layout = QGridLayout()             # Создаём QGridLayout ( выравнивание виджета по сетке)
        central_widget.setLayout(grid_layout)   # Заливаем его в центральный виджет

        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(10)     # создаем 10 колонок
        table.setRowCount(10)        # и 10 строк

        # "заголовки" первой строки
        table.setHorizontalHeaderLabels([" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 "])

        # заполняем строки
        table.setItem(0, 0, QTableWidgetItem(" 1 "))
        table.setItem(0, 1, QTableWidgetItem(" 2 "))
        table.setItem(0, 2, QTableWidgetItem(" 3 "))
        table.setItem(0, 3, QTableWidgetItem(" 4 "))
        table.setItem(0, 4, QTableWidgetItem(" 5 "))
        table.setItem(0, 5, QTableWidgetItem(" 6 "))
        table.setItem(0, 6, QTableWidgetItem(" 7 "))
        table.setItem(0, 7, QTableWidgetItem(" 8 "))
        table.setItem(0, 8, QTableWidgetItem(" 9 "))
        table.setItem(0, 9, QTableWidgetItem(" 10 "))
        
        table.setItem(1, 0, QTableWidgetItem(" 2 "))
        table.setItem(1, 1, QTableWidgetItem(" 4 "))
        table.setItem(1, 2, QTableWidgetItem(" 6 "))
        table.setItem(1, 3, QTableWidgetItem(" 8 "))
        table.setItem(1, 4, QTableWidgetItem(" 10 "))
        table.setItem(1, 5, QTableWidgetItem(" 12 "))
        table.setItem(1, 6, QTableWidgetItem(" 14 "))
        table.setItem(1, 7, QTableWidgetItem(" 16 "))
        table.setItem(1, 8, QTableWidgetItem(" 18 "))
        table.setItem(1, 9, QTableWidgetItem(" 20 "))
        
        table.setItem(2, 0, QTableWidgetItem(" 3 "))
        table.setItem(2, 1, QTableWidgetItem(" 6 "))
        table.setItem(2, 2, QTableWidgetItem(" 9 "))
        table.setItem(2, 3, QTableWidgetItem(" 12 "))
        table.setItem(2, 4, QTableWidgetItem(" 15 "))
        table.setItem(2, 5, QTableWidgetItem(" 18 "))
        table.setItem(2, 6, QTableWidgetItem(" 21 "))
        table.setItem(2, 7, QTableWidgetItem(" 24 "))
        table.setItem(2, 8, QTableWidgetItem(" 27 "))
        table.setItem(2, 9, QTableWidgetItem(" 30 "))
        
        table.setItem(3, 0, QTableWidgetItem(" 4 "))
        table.setItem(3, 1, QTableWidgetItem(" 8 "))
        table.setItem(3, 2, QTableWidgetItem(" 12 "))
        table.setItem(3, 3, QTableWidgetItem(" 16 "))
        table.setItem(3, 4, QTableWidgetItem(" 20 "))
        table.setItem(3, 5, QTableWidgetItem(" 24 "))
        table.setItem(3, 6, QTableWidgetItem(" 28 "))
        table.setItem(3, 7, QTableWidgetItem(" 32 "))
        table.setItem(3, 8, QTableWidgetItem(" 36 "))
        table.setItem(3, 9, QTableWidgetItem(" 40 "))
        
        table.setItem(4, 0, QTableWidgetItem(" 5 "))
        table.setItem(4, 1, QTableWidgetItem(" 10 "))
        table.setItem(4, 2, QTableWidgetItem(" 15 "))
        table.setItem(4, 3, QTableWidgetItem(" 20 "))
        table.setItem(4, 4, QTableWidgetItem(" 25 "))
        table.setItem(4, 5, QTableWidgetItem(" 30 "))
        table.setItem(4, 6, QTableWidgetItem(" 35 "))
        table.setItem(4, 7, QTableWidgetItem(" 40 "))
        table.setItem(4, 8, QTableWidgetItem(" 45 "))
        table.setItem(4, 9, QTableWidgetItem(" 50 "))
        
        table.setItem(5, 0, QTableWidgetItem(" 6 "))
        table.setItem(5, 1, QTableWidgetItem(" 12 "))
        table.setItem(5, 2, QTableWidgetItem(" 18 "))
        table.setItem(5, 3, QTableWidgetItem(" 24 "))
        table.setItem(5, 4, QTableWidgetItem(" 30 "))
        table.setItem(5, 5, QTableWidgetItem(" 36 "))
        table.setItem(5, 6, QTableWidgetItem(" 42 "))
        table.setItem(5, 7, QTableWidgetItem(" 48 "))
        table.setItem(5, 8, QTableWidgetItem(" 54 "))
        table.setItem(5, 9, QTableWidgetItem(" 60 "))
        
        table.setItem(6, 0, QTableWidgetItem(" 7 "))
        table.setItem(6, 1, QTableWidgetItem(" 14 "))
        table.setItem(6, 2, QTableWidgetItem(" 21 "))
        table.setItem(6, 3, QTableWidgetItem(" 28 "))
        table.setItem(6, 4, QTableWidgetItem(" 35 "))
        table.setItem(6, 5, QTableWidgetItem(" 42 "))
        table.setItem(6, 6, QTableWidgetItem(" 49 "))
        table.setItem(6, 7, QTableWidgetItem(" 56 "))
        table.setItem(6, 8, QTableWidgetItem(" 63 "))
        table.setItem(6, 9, QTableWidgetItem(" 70 "))  
        
        table.setItem(7, 0, QTableWidgetItem(" 8 "))
        table.setItem(7, 1, QTableWidgetItem(" 16 "))
        table.setItem(7, 2, QTableWidgetItem(" 24 "))
        table.setItem(7, 3, QTableWidgetItem(" 32 "))
        table.setItem(7, 4, QTableWidgetItem(" 40 "))
        table.setItem(7, 5, QTableWidgetItem(" 48 "))
        table.setItem(7, 6, QTableWidgetItem(" 56 "))
        table.setItem(7, 7, QTableWidgetItem(" 64 "))
        table.setItem(7, 8, QTableWidgetItem(" 72 "))
        table.setItem(7, 9, QTableWidgetItem(" 80 ")) 
        
        table.setItem(8, 0, QTableWidgetItem(" 9 "))
        table.setItem(8, 1, QTableWidgetItem(" 18 "))
        table.setItem(8, 2, QTableWidgetItem(" 27 "))
        table.setItem(8, 3, QTableWidgetItem(" 36 "))
        table.setItem(8, 4, QTableWidgetItem(" 45 "))
        table.setItem(8, 5, QTableWidgetItem(" 54 "))
        table.setItem(8, 6, QTableWidgetItem(" 63 "))
        table.setItem(8, 7, QTableWidgetItem(" 72 "))
        table.setItem(8, 8, QTableWidgetItem(" 81 "))
        table.setItem(8, 9, QTableWidgetItem(" 90 "))
        
        table.setItem(9, 0, QTableWidgetItem(" 10 "))
        table.setItem(9, 1, QTableWidgetItem(" 20 "))
        table.setItem(9, 2, QTableWidgetItem(" 30 "))
        table.setItem(9, 3, QTableWidgetItem(" 40 "))
        table.setItem(9, 4, QTableWidgetItem(" 50 "))
        table.setItem(9, 5, QTableWidgetItem(" 60 "))
        table.setItem(9, 6, QTableWidgetItem(" 70 "))
        table.setItem(9, 7, QTableWidgetItem(" 80 "))
        table.setItem(9, 8, QTableWidgetItem(" 90 "))
        table.setItem(9, 9, QTableWidgetItem(" 100 "))        

        # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()

        grid_layout.addWidget(table, 0, 0)   # Добавляем таблицу в сетку
    def run_2(self):
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())