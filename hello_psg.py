# hello_psg.py

import PySimpleGUI as sg

message = "GERAI"

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button(message)]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == message or event == sg.WIN_CLOSED:
        break

window.close()