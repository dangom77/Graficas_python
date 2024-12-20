"""
El siguiente código permite generar hasta 5 diferentes gráficas usando diferentes paquetes
de python a partir de un dataframe creado de un archivo .csv suministrado.

Requiere un archivo csv y los diferentes paquetes de python

Retorna: Gráficas generadas con los datos suministrados

Author:
  Daniel Alfredo Gómez Chavarría
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from fontTools.unicodedata import block

# Leer el archivo .csv y especificar separador
df = pd.read_csv('Fusarium_Genome_Stats.csv', sep=';', header=0)

#### Verifiación del dataframe y typos de datos que contiene
# print("Column names in the dataset:")
# print(df.columns.tolist())
# print("\nFirst few rows of data:")
# print(df.head())
# print(df.dtypes)

#### Generación de las figuras

# Boxplot de la longitud de los ensamblajes
sns.boxplot(x='Assembly_length', data=df)
plt.title('Distribución de tamaños de los ensamblajes')
plt.show(block=True)
plt.savefig("boxplot_Assembly_length.pdf")

# Pie chart de los datos asociaciados a continentes
continents_count = df['Continent'].value_counts()

plt.pie(continents_count, labels=continents_count.index, autopct='%1.1f%%')
plt.title('Distribución de los ensamblajes reportados por continente')
plt.show(block=True)
plt.savefig("PieChart_Continents.pdf")

# Histograma de frecuencias del %GC

plt.hist(df['GC_ratio'], bins=20)
plt.title('Distribución de Contenido GC en los Ensamblajes')
plt.xlabel('Contenido GC (%)')
plt.ylabel('Frecuencia')
plt.show(block=True)
plt.savefig("Hist_GC.pdf")

# Scatter para comparar Longitud de los ensamblajes con el N50

plt.scatter(df['Assembly_length'], df['N50'])
plt.xlabel('Longitud del ensamblaje')
plt.ylabel('N50')
plt.title('Relación entre longitud del ensamblaje y el N50')
plt.show(block=True)
plt.savefig('ScatterPlot_Assembly_length_vs_N50.pdf')

#### Diagrama de violín

# Transformar los datos del formato ancho al formato largo
df_long = pd.melt(df, id_vars='Genus', value_vars=['BUSCO_singlecopy', 'BUSCO_duplicated'],
                  var_name='type_gen', value_name='count')

# Verificar la transformación
# print(df_long)

# Transformación logarítmica de los datos para facilitar su interpretación gráfica.
df_long['count_log'] = np.log1p(df_long['count'])

# Verificar la transformación
# print(df_long['count_log'])

# Generación del diagrama de violin

sns.violinplot(x='type_gen', y='count_log', data=df_long)
plt.yscale('log')
plt.xlabel('Tipo de gen')
plt.ylabel('Logaritmo del % de genes')
plt.title('Comparación de genes de copia única vs duplicados según BUSCO')
plt.show(block=True)
plt.savefig('Violin_CopiaUnica_vs_duplicados.pdf')
