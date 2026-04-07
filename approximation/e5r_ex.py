from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem
import math
def euler():
    s0=1
    s=2
    while abs((1/(s0*s0))-(1/(s*s)))>=0.0001:
        s0=s0+1
        s=s+1
    return (1/(s0*s0))-(1/(s*s))
def wallis(eps):
    b=2
    m1=1
    m2=3
    p=(b/m1)*(b/m2)
    p0=0
    while (abs(abs((2*p)-(2*p0))))>=eps:
        p0=p
        b+=2
        m1+=2
        m2+=2
        p*=(b/m1)*(b/m2)
    return p*2
    
    
def calcul_e():
    p1=2
    s0=1
    s1=1/p1
    while (abs(s0-s1)>=0.0001):
        p1+=1
        s0=s1
        s1=1/fact(p1)
        
    return abs(s0-s1)

def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p


def play():
    inp=f.input.text()
    ch=0
    if not ((inp).isdecimal):
        QmessageBox.critical(f,"erreur","input invalid")
    else:
        if f.r1.isChecked():
            ch=str(wallis(int(inp)))
        elif f.r2.isChecked():
            ch=str(euler())
        elif f.r3.isChecked():
            ch=str(calcul_e())
    f.output.setText(ch)
        
        

app = QApplication([])
f = loadUi ("play.ui")
f.show()
f.c.clicked.connect (play)
app.exec_()
