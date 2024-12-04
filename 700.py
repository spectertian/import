import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QLabel, QTextEdit
from PySide6.QtCore import Qt
from pathlib import Path
from PDFProcessor import PDFProcessor  # 假设我们把之前的PDFProcessor类放在一个单独的文件中

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF处理器")
        self.setGeometry(100, 100, 600, 400)

        # 创建主窗口部件和布局
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # PDF文件选择
        pdf_layout = QHBoxLayout()
        self.pdf_label = QLabel("PDF文件:")
        self.pdf_path = QLabel("未选择")
        pdf_button = QPushButton("选择PDF")
        pdf_button.clicked.connect(self.select_pdf)
        pdf_layout.addWidget(self.pdf_label)
        pdf_layout.addWidget(self.pdf_path)
        pdf_layout.addWidget(pdf_button)

        # Excel文件选择
        excel_layout = QHBoxLayout()
        self.excel_label = QLabel("Excel文件:")
        self.excel_path = QLabel("未选择")
        excel_button = QPushButton("选择Excel")
        excel_button.clicked.connect(self.select_excel)
        excel_layout.addWidget(self.excel_label)
        excel_layout.addWidget(self.excel_path)
        excel_layout.addWidget(excel_button)

        # 输出文件选择
        output_layout = QHBoxLayout()
        self.output_label = QLabel("输出文件:")
        self.output_path = QLabel("未选择")
        output_button = QPushButton("选择输出")
        output_button.clicked.connect(self.select_output)
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(output_button)

        # 处理按钮
        process_button = QPushButton("处理")
        process_button.clicked.connect(self.process_files)

        # 日志显示区域
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)

        # 将所有部件添加到主布局
        main_layout.addLayout(pdf_layout)
        main_layout.addLayout(excel_layout)
        main_layout.addLayout(output_layout)
        main_layout.addWidget(process_button)
        main_layout.addWidget(self.log_area)

        # 设置主窗口部件和布局
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def select_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择PDF文件", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdf_path.setText(file_path)

    def select_excel(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择Excel文件", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.excel_path.setText(file_path)

    def select_output(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择输出文件", "", "Excel Files (*.xlsx)")
        if file_path:
            self.output_path.setText(file_path)

    def process_files(self):
        pdf_path = self.pdf_path.text()
        excel_path = self.excel_path.text()
        output_path = self.output_path.text()

        if pdf_path == "未选择" or excel_path == "未选择" or output_path == "未选择":
            self.log_area.append("请选择所有必要的文件。")
            return

        self.log_area.append("开始处理...")
        try:
            processor = PDFProcessor(pdf_path, excel_path, output_path)
            processor.process()
            self.log_area.append("处理完成。")
        except Exception as e:
            self.log_area.append(f"处理过程中出错: {str(e)}")

    def log(self, message):
        self.log_area.append(message)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())