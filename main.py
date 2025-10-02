import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout

class Calculator(QWidget):
    """
    계산기의 메인 윈도우를 담당하는 클래스입니다.
    QWidget을 상속받아 커스텀 위젯을 생성합니다.
    """
    def __init__(self):
        """
        생성자 메서드입니다.
        super().__init__()를 호출하여 부모 클래스의 생성자를 실행하고,
        UI 초기화 메서드를 호출합니다.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        UI의 기본 설정을 초기화하는 메서드입니다.
        """
        # 창의 제목을 '계산기'로 설정합니다.
        self.setWindowTitle('계산기')
        
        # 창의 위치와 크기를 설정합니다. (x, y, 너비, 높이)
        # 화면의 (300, 300) 위치에 400x500 크기의 창이 생성됩니다.
        self.setGeometry(300, 300, 400, 500)

        # 텍스트 에디터 생성
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True) # 편집 불가하도록 설정

        # 메시지 버튼 생성
        btn = QPushButton('메시지', self)
        btn.move(50, 50)
        btn.clicked.connect(self.showMessageBox)
        self.msg_button = QPushButton('메시지', self)
        self.msg_button.clicked.connect(self.appendMessage)

    def showMessageBox(self):
        # Clear 버튼 생성
        self.clear_button = QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.clearText)

        # 수직 레이아웃 생성 및 위젯 추가
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit) # 텍스트 에디터를 레이아웃에 추가
        vbox.addWidget(self.msg_button) # 메시지 버튼을 레이아웃에 추가
        vbox.addWidget(self.clear_button) # Clear 버튼을 레이아웃에 추가

        self.setLayout(vbox)

    def appendMessage(self):
        """
        버튼 클릭 시 메시지 박스를 표시하는 슬롯 메서드입니다.
        버튼 클릭 시 텍스트 에디터에 메시지를 추가하는 슬롯 메서드입니다.
        """
        QMessageBox.information(self, '메시지', 'Button Clicked')
        self.text_edit.append('Button Clicked')

    def clearText(self):
        """
        Clear 버튼 클릭 시 텍스트 에디터의 내용을 지우는 슬롯 메서드입니다.
        """
        self.text_edit.clear()


if __name__ == '__main__':
    # QApplication: 프로그램을 실행하고 이벤트 루프를 관리하는 클래스입니다.
    app = QApplication(sys.argv)
    
    # 우리가 만든 Calculator 클래스의 인스턴스를 생성합니다.
    calc_window = Calculator()
    
    # 위젯을 화면에 보여줍니다.
    calc_window.show()
    
    # 프로그램을 실행하고, 창을 닫으면(exit) 프로세스가 종료되도록 합니다.
    sys.exit(app.exec())
