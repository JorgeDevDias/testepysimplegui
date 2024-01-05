import PySimpleGUI as psg
import pandas as pd
psg.set_options(font=("Arial Bold", 14))

#Ler o arquivo
df = pd.read_excel('efetivo.xlsx')
#Pegar o cabeçalho
name_columns = []
for col in df.columns:
    name_columns.append(col)
print(name_columns)

linhas = []
for i in df.index:
    valores_linha = [df.loc[i, coluna] for coluna in df.columns]
    linhas.append(valores_linha)

tbl1 = psg.Table(values=linhas, headings=name_columns,
   auto_size_columns=True,
   display_row_numbers=False,
   justification='center', key='-TABLE-',
   #selected_row_colors='red on yellow',
   enable_events=True,
   expand_x=True,
   expand_y=True,)
  #enable_click_events=True)

layout = [[psg.Text('Some text on Row 1')],
            [psg.Text('Enter something on Row 2'), psg.InputText()]]

layout.append([[tbl1]])

window = psg.Window("Table Demo", layout, size=(715, 500), resizable=True)
while True:
   event, values = window.read()
   if event == psg.WIN_CLOSED:
      break
   if '+CLICKED+' in event:
      psg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))

window.close()