import PySimpleGUI as sg

sg.theme("DarkGreen")

layout=[
    [sg.Text("Hello,world!")]
]
win=sg.Window("Hello,world!",layout)
while True:
    event,values=win.read()
    if event is None:
        break

win.close()