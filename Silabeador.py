#coding=UTF-8
# División silábica en español (Quilis, Tratado de fonética y fonología, p. 368 y ss.)
# V=vocal C = consonante.
# 1. VCV = V-CV
# 2. VCCV = a) VC-CV b) V-CCV (p, b, f, g, k + r, l / dr, tr)
# 3. VCCC(C)V = a)VCC (ns, bs) - CV b)VC-CCV (C + l, r) cons- truir an-sie-dad
# 4. VV = a) V-V (abiertas, abierta + cerrada tónica, cerrada tónica + abierta) b) VV (cerradas, abierta+cerrada átona, cerrada átona + abierta)
# La consonante no puede ser núcleo ni constituir sílaba por sí misma.
# prefijos = sub

consonantes =  map(lambda word: unicode(word, 'utf-8'), ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
vocales =map(lambda word: unicode(word, 'utf-8'), ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü'])
inseparables = map(lambda word: unicode(word, 'utf-8'), ['ch', 'll', 'rr', 'pr', 'pl', 'br', 'bl', 'fr', 'fl', 'gr', 'gl', 'kr', 'cr', 'kl', 'cl', 'dr', 'tr'])
vcerradas = map(lambda word: unicode(word, 'utf-8'),['i', 'u', 'ü'])
letras = consonantes + vocales

def es_vocal(letra):
  return letra in vocales

def es_consonante(letra):
  return letra in consonantes

def es_inseparable(letra1, letra2):
  if not letra1 or not letra2:
    return False
  return letra1+letra2 in inseparables

def es_diptongo(letra_anterior, letra):
  return letra in vcerradas or letra_anterior in vcerradas

def buscar_letra_anterior(palabra, index):
  return palabra[index-1]

def buscar_letra_siguiente(palabra, index):
  if index == len(palabra)-1:
    return False
  else:
    return palabra[index+1]
    
def pedir_palabra():
  while True:
    palabra = raw_input('Escriba la palabra (exit para salir): ').decode('utf-8')
    if palabra == 'exit':
      print 'Adiós'   
      exit()
    if len(palabra) > 0:
      palabra = palabra.lower()
      palabra = palabra.strip()
      return palabra
      break  
    
while True:
    
  palabra = pedir_palabra()
  silaba = ''
  silabeo = []
  
  for index, letra in enumerate(palabra):
    
    if index==0:
      silaba=letra
      continue
  
    letra_anterior = buscar_letra_anterior(palabra, index)
    letra_siguiente = buscar_letra_siguiente(palabra, index)
    
    if es_vocal(letra) and es_consonante(letra_anterior):           # Estructura CV, la vocal se agrupa siempre con la consonante
      silaba=silaba+letra
      
    elif es_vocal(letra) and es_vocal(letra_anterior):                  # Estructura VV
      
      if es_diptongo(letra_anterior, letra):                                     # Diptongo VV, cuando una de las vocales es cerrada átona (i, u), resto de casos forma hiato V-V
        silaba=silaba+letra
      else:
        silabeo.append(silaba)
        silaba = letra
        
    elif es_consonante(letra):
    
      if es_inseparable(letra, letra_siguiente) or not es_inseparable(letra_anterior, letra) and es_vocal(letra_siguiente):
        silabeo.append(silaba)
        silaba = letra
          
      else:
        silaba=silaba+letra
        
    else:
      print 'Palabra no válida'
      break 
    
  silabeo.append(silaba)
  separador = ' - '
  silabeo = separador.join(silabeo)
  print silabeo

#silabeo= []
#for silaba in silabeo:
#  ' - '
#print 'cc: ' + letra_anterior + ' ' + letra + "\n"

		
