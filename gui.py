import functions
import PySimpleGUI as sg

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="enter todo")
add_button=sg.Button("Add")

window = sg.Window('my to-do app', layout=[[label], [input_box,add_button]])
window.read()
window.close()
