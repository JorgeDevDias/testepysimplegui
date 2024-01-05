import PySimpleGUI as sg

def criar_janela():
  sg.theme('DarkBlue4')
  linha_inicial = [
    [sg.Checkbox(''),sg.Input('')]
  ]
  layout = [
    [sg.Frame('Tarefas', layout=linha_inicial, key='container')],
    [sg.Button('Nova Tarefa'), sg.Button('Resert')],
  ]

  return sg.Window('Todo List', layout=layout)

nova_janela = criar_janela()

while True:
  event, values = nova_janela.read()
  if event == sg.WINDOW_CLOSED:
    break
  elif event == 'Nova Tarefa':
    nova_janela.extend_layout(nova_janela['container'],[[sg.Checkbox(''),sg.Input('')]])

  elif event == 'Resert':
    nova_janela.close()
    nova_janela = criar_janela()



