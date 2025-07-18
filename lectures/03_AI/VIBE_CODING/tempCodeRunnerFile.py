import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt

class SeatAssigner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('자리 배치 시각화')
        self.setGeometry(100, 100, 900, 600)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.seat_labels = []
        self.create_ui()

    def create_ui(self):
        # 스크린 표시
        screen = QLabel('스크린(앞)')
        screen.setAlignment(Qt.AlignCenter)
        screen.setStyleSheet('background:#B3E5FC; color:#222; font-size:18px; font-weight:bold; min-height:24px; max-height:24px; border:none; border-radius:6px;')
        self.layout.addWidget(screen, 0, 2, 1, 6)

        # 이름 입력창
        self.name_input = QTextEdit()
        self.name_input.setPlaceholderText('이름을 한 줄에 하나씩 입력하세요')
        self.layout.addWidget(self.name_input, 1, 0, 2, 2)
        self.assign_button = QPushButton('무작위 배정')
        self.assign_button.clicked.connect(self.assign_seats)
        self.layout.addWidget(self.assign_button, 3, 0, 1, 2)

        # 자리 배치 (왼쪽/오른쪽)
        left_structure = [3, 3, 3, 3, 2]
        right_structure = [3, 3, 3, 3, 2]
        self.seat_labels = []
        for row, (l, r) in enumerate(zip(left_structure, right_structure)):
            # 왼쪽
            for col in range(l):
                label = QLabel('')
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet('background:#A8E6CF; color:#222; font-size: 18px; min-width: 80px; min-height: 80px; max-width: 80px; max-height: 80px; border: none; border-radius: 10px;')
                self.layout.addWidget(label, row+2, col+2)
                self.seat_labels.append(label)
            # 오른쪽
            for col in range(r):
                label = QLabel('')
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet('background:#A8E6CF; color:#222; font-size: 18px; min-width: 80px; min-height: 80px; max-width: 80px; max-height: 80px; border: none; border-radius: 10px;')
                self.layout.addWidget(label, row+2, col+7)
                self.seat_labels.append(label)

    def assign_seats(self):
        names = [n.strip() for n in self.name_input.toPlainText().split('\n') if n.strip()]
        total_seats = len(self.seat_labels)
        if len(names) > total_seats:
            QMessageBox.warning(self, '오류', f'입력된 이름이 좌석 수({total_seats})보다 많습니다.')
            return
        random.shuffle(names)
        # 좌석에 이름 배정
        for i, label in enumerate(self.seat_labels):
            if i < len(names):
                label.setText(names[i])
            else:
                label.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SeatAssigner()
    window.show()
    sys.exit(app.exec_())
