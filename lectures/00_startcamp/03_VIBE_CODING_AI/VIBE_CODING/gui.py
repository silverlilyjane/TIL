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
        screen.setStyleSheet("background:#B3E5FC; color:#222; font-size:18px; font-weight:bold; min-height:24px; max-height:24px; border:none; border-radius:6px; font-family:'Malgun Gothic';")
        # 좌석 사각형 기준으로 가운데(왼쪽 2~4, 오른쪽 7~9, 총 6칸)로 span
        self.layout.addWidget(screen, 0, 2, 1, 8)

        # 이름 입력창
        self.name_input = QTextEdit()
        self.name_input.setPlaceholderText('이름을 한 줄에 하나씩 입력하세요')
        self.name_input.setStyleSheet("font-family:'Malgun Gothic'; font-size:15px;")
        self.layout.addWidget(self.name_input, 1, 0, 2, 2)
        self.assign_button = QPushButton('무작위 배정')
        self.assign_button.clicked.connect(self.assign_seats)
        self.layout.addWidget(self.assign_button, 3, 0, 1, 2)

        # 저장 버튼 추가
        self.save_img_button = QPushButton('이미지로 저장')
        self.save_img_button.clicked.connect(self.save_as_image)
        self.layout.addWidget(self.save_img_button, 4, 0, 1, 2)
        self.save_csv_button = QPushButton('CSV로 저장')
        self.save_csv_button.clicked.connect(self.save_as_csv)
        self.layout.addWidget(self.save_csv_button, 5, 0, 1, 2)

        # 자리 배치 (왼쪽/오른쪽)
        left_structure = [3, 3, 3, 3, 2]
        right_structure = [3, 3, 3, 3, 2]
        self.seat_labels = []
        for row, (l, r) in enumerate(zip(left_structure, right_structure)):
            # 왼쪽
            for col in range(l):
                label = QLabel('')
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("background:#A8E6CF; color:#222; font-size: 18px; min-width: 80px; min-height: 80px; max-width: 80px; max-height: 80px; border: none; border-radius: 10px; font-family:'Malgun Gothic';")
                self.layout.addWidget(label, row+2, col+2)
                self.seat_labels.append(label)
            # 오른쪽
            for col in range(r):
                label = QLabel('')
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("background:#A8E6CF; color:#222; font-size: 18px; min-width: 80px; min-height: 80px; max-width: 80px; max-height: 80px; border: none; border-radius: 10px; font-family:'Malgun Gothic';")
                self.layout.addWidget(label, row+2, col+7)
                self.seat_labels.append(label)
    def save_as_image(self):
        from PyQt5.QtWidgets import QFileDialog
        from PyQt5.QtGui import QPixmap
        # 좌석 배치 영역만 이미지로 저장
        file_path, _ = QFileDialog.getSaveFileName(self, '이미지로 저장', '', 'PNG Files (*.png)')
        if file_path:
            # 좌석 라벨들과 스크린 라벨의 영역 계산
            if not self.seat_labels:
                QMessageBox.warning(self, '오류', '좌석 배치가 없습니다.')
                return
            # 스크린 라벨 찾기 (항상 첫 번째 위젯)
            screen_label = None
            for i in range(self.layout.count()):
                widget = self.layout.itemAt(i).widget()
                if isinstance(widget, QLabel) and widget.text() == '스크린(앞)':
                    screen_label = widget
                    break
            if not screen_label:
                QMessageBox.warning(self, '오류', '스크린 라벨을 찾을 수 없습니다.')
                return
            # 스크린 라벨의 좌상단, 모든 좌석의 우하단 중 최대값(마지막 열이 잘리지 않게)
            p1 = screen_label.mapTo(self, screen_label.rect().topLeft())
            # 모든 좌석의 우하단 좌표 중 최대값 찾기
            max_x, max_y = 0, 0
            for seat in self.seat_labels:
                p = seat.mapTo(self, seat.rect().bottomRight())
                if p.x() > max_x:
                    max_x = p.x()
                if p.y() > max_y:
                    max_y = p.y()
            x, y = p1.x(), p1.y()
            w, h = max_x - x, max_y - y
            # 여백 추가
            margin = 10
            x = max(0, x - margin)
            y = max(0, y - margin)
            w = w + 2 * margin
            h = h + 2 * margin
            # 전체 윈도우 캡처 후 해당 부분만 crop
            full_pixmap = self.grab()
            seat_pixmap = full_pixmap.copy(x, y, w, h)
            seat_pixmap.save(file_path, 'PNG')
            QMessageBox.information(self, '저장 완료', '이미지로 저장되었습니다.')

    def save_as_csv(self):
        import csv
        from PyQt5.QtWidgets import QFileDialog
        file_path, _ = QFileDialog.getSaveFileName(self, 'CSV/엑셀로 저장', '', 'CSV Files (*.csv);;Excel Files (*.xlsx)')
        if file_path:
            # 자리 구조와 이름을 2차원 배열로 변환
            left_structure = [3, 3, 3, 3, 2]
            right_structure = [3, 3, 3, 3, 2]
            seat_idx = 0
            rows = []
            total_cols = 10
            # 첫 번째 행을 빈 칸 10개로 채움
            empty_row = [''] * total_cols
            rows.append(empty_row)
            for i, (l, r) in enumerate(zip(left_structure, right_structure)):
                row = []
                for _ in range(l):
                    row.append(self.seat_labels[seat_idx].text())
                    seat_idx += 1
                center = 4
                if i == 4:
                    center = 6
                for _ in range(center):
                    row.append('')
                for _ in range(r):
                    row.append(self.seat_labels[seat_idx].text())
                    seat_idx += 1
                while len(row) < total_cols:
                    row.append('')
                rows.append(row)

            import os
            ext = os.path.splitext(file_path)[1].lower()
            total_cols = 10
            # 모든 row의 길이를 10으로 맞춤
            for idx, row in enumerate(rows):
                if len(row) < total_cols:
                    row += [''] * (total_cols - len(row))
                elif len(row) > total_cols:
                    rows[idx] = row[:total_cols]
            if ext == '.xlsx':
                try:
                    from openpyxl import Workbook
                    from openpyxl.styles import Alignment, Font
                except ImportError:
                    QMessageBox.warning(self, '오류', 'openpyxl 패키지가 필요합니다.\n명령 프롬프트에서 "pip install openpyxl"을 실행하세요.')
                    return
                wb = Workbook()
                ws = wb.active
                for row in rows:
                    ws.append(row)
                wb.save(file_path)
                QMessageBox.information(self, '저장 완료', '엑셀(xlsx)로 저장되었습니다.')
            else:
                with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                QMessageBox.information(self, '저장 완료', 'CSV로 저장되었습니다.')

        # (중복 좌석 생성 코드 삭제)

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
