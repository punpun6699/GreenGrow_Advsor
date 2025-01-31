from PyQt5 import QtCore, QtWidgets,QtGui



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("GreenGrow Advisor")
        Form.resize(520, 600)

        #Form.setStyleSheet("background-color: #e8f5e9;")  # เขียวอ่อน
        Form.setObjectName("GreenGrow Advisor")
        Form.resize(520, 600)

        # ตั้งค่าพื้นหลังให้ขยายตามขนาดของหน้าต่าง
        Form.setStyleSheet("""
                    QWidget {
                        background-image: url('/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_UI/image/Green Saver.png');
                        background-position: center;
                        background-repeat: no-repeat;
                        background-size: cover;
                    }
                """)
        # สร้างฟอนต์
        font_label = "font-size: 14px; font-weight: bold; color: #2e7d32;"
        font_input = "background-color: white; border: 1px solid #388e3c; border-radius: 5px; color: #2e7d32;"
        font_button = """
    QPushButton {
        background: transparent;
        border: none;
    }
    QPushButton:hover {
        background-color: rgba(255, 255, 255, 50); /* สีขาวโปร่งแสง */
    }
"""
        font_button_hover = "QPushButton:hover {background-color: #388e3c;}"


        # สร้าง label และ textedit แบบไม่ใช้ for
        # self.label_UV_index = QtWidgets.QLabel(Form)
        # self.label_UV_index.setGeometry(QtCore.QRect(40, 40, 140, 30))
        # self.label_UV_index.setText("UV Index:")
      #  self.label_UV_index.setStyleSheet(font_label)

        self.textEdit_UV_index = QtWidgets.QTextEdit(Form)
        self.textEdit_UV_index.setGeometry(QtCore.QRect(190, 40, 150, 30))
        self.textEdit_UV_index.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

       # self.textEdit_UV_index.setStyleSheet(font_input)

        # self.label_Temperature = QtWidgets.QLabel(Form)
        # self.label_Temperature.setGeometry(QtCore.QRect(40, 80, 140, 30))
        # self.label_Temperature.setText("Temperature:")
      #  self.label_Temperature.setStyleSheet(font_label)

        self.textEdit_Temperature = QtWidgets.QTextEdit(Form)
        self.textEdit_Temperature.setGeometry(QtCore.QRect(190, 80, 150, 30))
        self.textEdit_Temperature.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

       # self.textEdit_Temperature.setStyleSheet(font_input)

        # self.label_Humidity = QtWidgets.QLabel(Form)
        # self.label_Humidity.setGeometry(QtCore.QRect(40, 120, 140, 30))
        # self.label_Humidity.setText("Humidity:")
      #  self.label_Humidity.setStyleSheet(font_label)

        self.textEdit_Humidity = QtWidgets.QTextEdit(Form)
        self.textEdit_Humidity.setGeometry(QtCore.QRect(190, 120, 150, 30))
        self.textEdit_Humidity.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

       # self.textEdit_Humidity.setStyleSheet(font_input)

        # self.label_Precipitation_Q1 = QtWidgets.QLabel(Form)
        # self.label_Precipitation_Q1.setGeometry(QtCore.QRect(40, 160, 140, 30))
        # self.label_Precipitation_Q1.setText("Precipitation Q1:")
      #  self.label_Precipitation_Q1.setStyleSheet(font_label)

        self.textEdit_Precipitation_Q1 = QtWidgets.QTextEdit(Form)
        self.textEdit_Precipitation_Q1.setGeometry(QtCore.QRect(190, 160, 150, 30))
        self.textEdit_Precipitation_Q1.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

      #  self.textEdit_Precipitation_Q1.setStyleSheet(font_input)

        # self.label_Precipitation_Q2 = QtWidgets.QLabel(Form)
        # self.label_Precipitation_Q2.setGeometry(QtCore.QRect(40, 200, 140, 30))
        # self.label_Precipitation_Q2.setText("Precipitation Q2:")
      #  self.label_Precipitation_Q2.setStyleSheet(font_label)

        self.textEdit_Precipitation_Q2 = QtWidgets.QTextEdit(Form)
        self.textEdit_Precipitation_Q2.setGeometry(QtCore.QRect(190, 200, 150, 30))
        self.textEdit_Precipitation_Q2.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

       # self.textEdit_Precipitation_Q2.setStyleSheet(font_input)

        # self.label_Precipitation_Q3 = QtWidgets.QLabel(Form)
        # self.label_Precipitation_Q3.setGeometry(QtCore.QRect(40, 240, 140, 30))
        # self.label_Precipitation_Q3.setText("Precipitation Q3:")
        #self.label_Precipitation_Q3.setStyleSheet(font_label)

        self.textEdit_Precipitation_Q3 = QtWidgets.QTextEdit(Form)
        self.textEdit_Precipitation_Q3.setGeometry(QtCore.QRect(190, 240, 150, 30))
        self.textEdit_Precipitation_Q3.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

        #self.textEdit_Precipitation_Q3.setStyleSheet(font_input)

       #  self.label_Precipitation_Q4 = QtWidgets.QLabel(Form)
       #  self.label_Precipitation_Q4.setGeometry(QtCore.QRect(40, 280, 140, 30))
       #  self.label_Precipitation_Q4.setText("Precipitation Q4:")
       # # self.label_Precipitation_Q4.setStyleSheet(font_label)

        self.textEdit_Precipitation_Q4 = QtWidgets.QTextEdit(Form)
        self.textEdit_Precipitation_Q4.setGeometry(QtCore.QRect(190, 280, 150, 30))
        self.textEdit_Precipitation_Q4.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

        #self.textEdit_Precipitation_Q4.setStyleSheet(font_input)

        # self.label_Nitrogen = QtWidgets.QLabel(Form)
        # self.label_Nitrogen.setGeometry(QtCore.QRect(40, 320, 140, 30))
        # self.label_Nitrogen.setText("Nitrogen:")
        #self.label_Nitrogen.setStyleSheet(font_label)

        self.textEdit_Nitrogen = QtWidgets.QTextEdit(Form)
        self.textEdit_Nitrogen.setGeometry(QtCore.QRect(190, 320, 150, 30))
        self.textEdit_Nitrogen.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

      #  self.textEdit_Nitrogen.setStyleSheet(font_input)

        # self.label_Phosphorus = QtWidgets.QLabel(Form)
        # self.label_Phosphorus.setGeometry(QtCore.QRect(40, 360, 140, 30))
        # self.label_Phosphorus.setText("Phosphorus:")
      #  self.label_Phosphorus.setStyleSheet(font_label)

        self.textEdit_Phosphorus = QtWidgets.QTextEdit(Form)
        self.textEdit_Phosphorus.setGeometry(QtCore.QRect(190, 360, 150, 30))
        self.textEdit_Phosphorus.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

      #   self.label_Potassium.setStyleSheet(font_label)

        self.textEdit_Potassium = QtWidgets.QTextEdit(Form)
        self.textEdit_Potassium.setGeometry(QtCore.QRect(190, 400, 150, 30))
        self.textEdit_Potassium.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

      #  self.textEdit_Potassium.setStyleSheet(font_input)

        # สร้าง label และ textedit สำหรับ Result
        # self.label_ANS = QtWidgets.QLabel(Form)
        # self.label_ANS.setGeometry(QtCore.QRect(40, 440, 140, 30))
        # self.label_ANS.setText("Result:")
      #  self.label_ANS.setStyleSheet(font_label)

        self.textEdit_ANS = QtWidgets.QTextEdit(Form)
        self.textEdit_ANS.setGeometry(QtCore.QRect(190, 440, 150, 30))
        self.textEdit_ANS.setReadOnly(True)
        self.textEdit_ANS.setStyleSheet("background: transparent; border: none; color: #2e7d32;")

      #  self.textEdit_ANS.setStyleSheet(font_input)

        # สร้างปุ่ม
        self.pushButton_cal = QtWidgets.QPushButton(Form)
        self.pushButton_cal.setGeometry(QtCore.QRect(370, 40, 120, 50))
        self.pushButton_cal.setText("")
        self.pushButton_cal.setStyleSheet(font_button)

       # self.pushButton_cal.setStyleSheet(font_button + font_button_hover)

        self.pushButton_cls = QtWidgets.QPushButton(Form)
        self.pushButton_cls.setGeometry(QtCore.QRect(370, 100, 120, 50))
        self.pushButton_cls.setText("")
        self.pushButton_cls.setStyleSheet(font_button)

       # self.pushButton_cls.setStyleSheet(font_button + font_button_hover)

        self.pushButton_data = QtWidgets.QPushButton(Form)
        self.pushButton_data.setGeometry(QtCore.QRect(370, 160, 120, 50))
        self.pushButton_data.setText("")
        self.pushButton_data.setStyleSheet(font_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle("GreenGrow Advisor")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # ตั้งให้แอปไม่ใช้ Dark Mode โดยการตั้ง Palette
    app.setStyle("Fusion")
    palette = app.palette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))  # ขาว
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0))  # ดำ
    app.setPalette(palette)


    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
