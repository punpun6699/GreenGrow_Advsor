import sys,subprocess,joblib
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5 import QtGui
from GreenAdvisor_UI import main_ui


def getdata(): #get the data if all data is float use  usemodel fn
    try:
        UV_index =float(ui.textEdit_UV_index.document().toPlainText())
        Temperature = float(ui.textEdit_Temperature.document().toPlainText())
        Humidity = float(ui.textEdit_Humidity.document().toPlainText())
        Precipitation_Q1 = float(ui.textEdit_Precipitation_Q1.document().toPlainText())
        Precipitation_Q2 = float(ui.textEdit_Precipitation_Q2.document().toPlainText())
        Precipitation_Q3 = float(ui.textEdit_Precipitation_Q3.document().toPlainText())
        Precipitation_Q4 = float(ui.textEdit_Precipitation_Q4.document().toPlainText())
        Nitrogen = float(ui.textEdit_Nitrogen.document().toPlainText())
        Phosphorus = float(ui.textEdit_Phosphorus.document().toPlainText())
        Potassium = float(ui.textEdit_Potassium.document().toPlainText())
        data = [[UV_index, Temperature, Humidity, Precipitation_Q1, Precipitation_Q2, Precipitation_Q3, Precipitation_Q4,Nitrogen, Phosphorus, Potassium]]
        print(data)
        usemodel(data)
    except ValueError:
        cls()
        ui.textEdit_ANS.setText("in put float")

    return

def cls():
    ui.textEdit_UV_index.setText("")
    ui.textEdit_Temperature.setText("")
    ui.textEdit_Humidity.setText("")
    ui.textEdit_Precipitation_Q1.setText("")
    ui.textEdit_Precipitation_Q2.setText("")
    ui.textEdit_Precipitation_Q3.setText("")
    ui.textEdit_Precipitation_Q4.setText("")
    ui.textEdit_Nitrogen.setText("")
    ui.textEdit_Phosphorus.setText("")
    ui.textEdit_Potassium.setText("")
    ui.textEdit_ANS.setText("")


def usemodel(data):    #use plant_recommendation_model.joblib (plant_recommendation model)
    loade_PRM = joblib.load('/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_Model/Model_Training/plant_recommendation_model_V2.joblib')
    prediction = loade_PRM.predict(data)
    ans = str(prediction)
    ui.textEdit_ANS.setText(str(ans[2:len(ans)-2]))
    print("Prediction:", prediction)

def opendata():
    """
    เรียกใช้โปรแกรม data_popUp.py โดยใช้เส้นทางแบบ Absolute Path
    """
    try:
        result = subprocess.run(
            ["python", "/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_app/PopUP_app/data_popup_app/data_popUp.py"],
            capture_output=True,
            text=True
        )
        print("Script Output from opendata:", result.stdout)
        print("Script Errors from opendata:", result.stderr)
    except Exception as e:
        print(f"Error running opendata(): \n{e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = main_ui.Ui_Form()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    win.show()  # Show the main window

    app.setStyle("Fusion")
    palette = app.palette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))  # ขาว
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0))  # ดำ
    app.setPalette(palette)

    # Connect button clicks to functions
    ui.pushButton_cal.clicked.connect(getdata)
    ui.pushButton_cls.clicked.connect(cls)
    ui.pushButton_data.clicked.connect(opendata)

    sys.exit(app.exec_())  # Start the event loop and exit the application when done