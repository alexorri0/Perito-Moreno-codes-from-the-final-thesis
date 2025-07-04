# -*- coding: utf-8 -*-
"""perfils_velocitat.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15IWaW-vhZwhvJwN9JgBg8h6bURsDh9YY
"""

from IPython import get_ipython
from IPython.display import display
# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Importem seaborn per millorar l'estil

sns.set_theme(style="whitegrid")

# Configurem la font

plt.rcParams['font.family'] = 'serif'

# Llista de fonts serif a provar (Matplotlib utilitzarà la primera que trobi)

plt.rcParams['font.serif'] = ['Times New Roman', 'Georgia', 'Palatino Linotype', 'DejaVu Serif', 'serif']

# Llista dels fitxers CSV a carregar

fitxers_i_columnes = [
    ('Gener2017.csv', 1), # Fitxer 'Gener2017.csv', utilitzar la columna amb índex 1
    ('Gener2018.csv', 0), # Fitxer 'Gener2018.csv', utilitzar la columna amb índex 0
    ('Agost2018.csv',0),
    ('Gener2021.csv',0),
    ('Agost2021.csv',0),
    ('Gener2025.csv',0)
]

# Paleta de colors per les línies

colors = sns.color_palette("tab10", len(fitxers_i_columnes))

# Creació de la figura i els eixos per al gràfic
# Augmentem significativament la mida horitzontal per "descomprimir-lo"

plt.figure(figsize=(18, 6))

# Bucle per carregar les dades de cada fitxer i traçar la línia corresponent

for i, (fitxer, index_columna) in enumerate(fitxers_i_columnes):
    try:
        # Carregar les dades del fitxer CSV
        df = pd.read_csv(fitxer)

        # Verificar que l'índex de columna és vàlid
        if index_columna < df.shape[1]:
            # Seleccionar les dades de la columna especificada
            y = df.iloc[:, index_columna]
            # Calcular la distància en km basant-se en l'índex i la longitud total (20 km)
            x = (df.index / (len(df) - 1)) * 20 if len(df) > 1 else df.index


            # Modificar el nom del fitxer per la llegenda (eliminar '.csv')
            nom_llegenda = fitxer.replace('.csv', '')

            # Traçar la línia per al fitxer actual
            plt.plot(x, y, color=colors[i], linewidth=2, label=nom_llegenda)

        else:
            print(f"Advertència: La columna amb índex {index_columna} no existeix en el fitxer {fitxer}. S'ignora aquest fitxer.")

    except FileNotFoundError:
        print(f"Error: El fitxer {fitxer} no s'ha trobat. Assegura't que el fitxer és al directori correcte.")
    except Exception as e:
        print(f"Error processant el fitxer {fitxer}: {e}")

# Configuració de l'estètica del gràfic

plt.ylabel('Velocitat [m/d]', fontsize=12)
plt.title('Comparativa de velocitats al llarg de la glacera', fontsize=14)

# Afegim l'eix X

plt.xticks(range(0, 21, 5)) # Posem marques cada 5 unitats fins a 20
plt.xlabel("Distància del transsecte A-A' [km]", fontsize=12) # Afegim l'etiqueta de l'eix X
plt.gca().spines['bottom'].set_visible(True) # Fem visible la línia de l'eix X
plt.gca().xaxis.set_visible(True) # Fem visibles les marques i etiquetes de l'eix X

# Ajustar els límits de l'eix X
plt.xlim(0, 20)


plt.grid(True, linestyle='--', alpha=0.6) # Afegim una graella

plt.legend(title='Dades', loc='upper left', fontsize=10) # Posició de la llegenda dins del gràfic

plt.tight_layout() # Ajustar el layout automàticament

# Mostrar el gràfic
plt.show()