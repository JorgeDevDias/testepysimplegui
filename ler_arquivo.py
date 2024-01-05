import PySimpleGUI as sg
import pandas as pd

def Ler_arquivo():
    df = pd.read_excel('efetivo.xlsx')
    # Pegar o cabeçalho
    name_columns = df.columns.tolist()

    linhas = df.values.tolist()

    return name_columns, linhas


def criar_janela(tema):
  sg.theme(tema)
  sg.set_options(font=("Arial Bold", 14))
  temas_disponiveis = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 
                       'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 
                       'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 
                       'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 
                       'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 
                       'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 
                       'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkGreen', 'DarkGreen1', 
                       'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 
                       'DarkGrey', 'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4',
                         'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkPurple', 'DarkPurple1', 
                         'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 
                         'DarkPurple6', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 
                         'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12',
                           'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6',
                             'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1',
                               'DefaultNoMoreNagging', 'Green', 'GreenMono', 'GreenTan', 
                               'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 
                               'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 
                               'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10',
                                 'LightBrown11', 'LightBrown12', 'LightBrown13',
                                   'LightBrown2', 'LightBrown3', 'LightBrown4', 
                                   'LightBrown5', 'LightBrown6', 'LightBrown7',
                                     'LightBrown8', 'LightBrown9', 'LightGray1', 
                                     'LightGreen', 'LightGreen1', 'LightGreen10', 
                                     'LightGreen2', 'LightGreen3', 'LightGreen4', 
                                     'LightGreen5', 'LightGreen6', 'LightGreen7', 
                                     'LightGreen8', 'LightGreen9', 'LightGrey', 
                                     'LightGrey1', 'LightGrey2', 'LightGrey3', 
                                     'LightGrey4', 'LightGrey5', 'LightGrey6', 
                                     'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']


  cabecalho, linhas = Ler_arquivo()

  layout = [
      [sg.Text('Lista de Efetivo'),sg.Combo(temas_disponiveis, default_value='DarkBlue4', key='-COMBO_TEMA-')],
      [sg.Text('Pesquisa:'), sg.InputText(), sg.Button('Atualizar')],
      [sg.Table(values=linhas,
                headings=cabecalho,
                auto_size_columns=True,
                display_row_numbers=False,
                justification='center',
                key='-TABLE-',
                enable_events=True,
                expand_x=True,
                expand_y=True,
                font=("Arial", 12),
                pad=((10,10),(20,10)),
                )],
  ]

  return sg.Window('Efetivo', layout=layout, resizable=True)

tema_atual = 'DarkBlue4'
nova_janela = criar_janela(tema_atual)

while True:
  event, values = nova_janela.read()

  if event == sg.WINDOW_CLOSED:
      break
  elif event == 'Atualizar':
    nova_janela.close()
    nova_janela = criar_janela()

  elif event == '-COMBO_TEMA-':
    tema_selecionado = values['-COMBO_TEMA-']
    nova_janela.close()
    tema_atual = tema_selecionado
    nova_janela = criar_janela(tema_atual)

nova_janela.close()