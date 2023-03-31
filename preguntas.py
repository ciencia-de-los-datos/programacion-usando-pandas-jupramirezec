"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
 return len(tbl0)
pregunta_01() 


def pregunta_02():
 return len(tbl0.columns)
pregunta_02()


def pregunta_03():
 return tbl0['_c1'].value_counts().sort_index(ascending=True)
pregunta_03()    


def pregunta_04():
 return tbl0.groupby('_c1').mean()['_c2']
pregunta_04()    


def pregunta_05():
 return tbl0.groupby('_c1').max()['_c2']
pregunta_05()


def pregunta_06():
 lista = sorted(tbl1['_c4'].unique().tolist())
 lista_up = map(lambda x: x.upper(), lista)
 return list(lista_up)
pregunta_06()


def pregunta_07():
 return tbl0.groupby('_c1').sum()['_c2']
pregunta_07()


def pregunta_08():
 copy = tbl0.copy()
 copy['suma'] = copy['_c0'] + copy['_c2'] 
 return copy
pregunta_08()


def pregunta_09():
 copy2 = tbl0.copy()
 copy2['year'] = copy2['_c3'].apply(lambda x: x[0:4])
 return copy2
pregunta_09()


def pregunta_10():
  def aux(x):
    return ":".join(sorted(x.tolist()))
  copia1 = tbl0.copy()
  copia1['_c2'] = copia1['_c2'].apply(str)
  a = copia1.groupby('_c1')._c2.apply(aux)
  b = pd.DataFrame(a)
  return b
pregunta_10()


def pregunta_11():
 def aux(x):
  x = x.tolist()
  x.sort()
  x = list(map(str,x))
  return ",".join(map(str,x))
 a = tbl1.groupby('_c0')['_c4'].apply(aux)
 return a.reset_index()
pregunta_11()


def pregunta_12():
 def aux(x):
  x = x.tolist()
  x.sort()
  x = list(map(str,x))
  return ",".join(map(str,x))
 cop = tbl2.copy()
 cop['_c5b'] = cop['_c5b'].apply(str)
 cop["_c5"] = cop["_c5a"] + ":" + cop["_c5b"] 
 a = cop.groupby('_c0')['_c5'].apply(aux)
 return a.reset_index()
pregunta_12()


def pregunta_13():
 nueva = pd.merge(tbl0,tbl2, on = '_c0')
 return nueva.groupby('_c1').sum()['_c5b']
pregunta_13()
 