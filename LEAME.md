# Descripción

*Syllabicator* 'silabeador' es una función para la división silábica normativa de unidades discretas (palabras y pseudopalabras). No es aplicable por tanto a la transcripción fonética ni al análisis métrico del verso.

Aunque el proyecto nace para el análisis en lengua española la estructura es flexible y permite su adaptación a otros juegos de reglas y otros idiomas de estructuras silábicas análogas.

# Módulo de español

Se aplican las pautas de división silábica expuestas en Quilis, *Tratado de fonética y fonología*, p. 368 y ss. basada en patrones vocal/consonante (V=vocal C = consonante).

- VCV → V-CV 'a-mo'
- VCCV    
    - → VC-CV 'ar-mo'
    - → V-CCV 'a-bro' [(b, c, f, g, k, p) + (l, r), dr, tr, ch, ll, rr]
- VCCC(C)V   
    - → VCC (ns, bs) - (C)CV 'ins-tante', 'obs- truir'
    - → VC-CCV 'in-tra' (grupo inseparable)

- VV
    - → V-V 've-a', 'le-í-a' (abierta + abierta, abierta + cerrada tónica, cerrada tónica + abierta)
    - → VV 'au-ra' (cerrada + cerrada, abierta + cerrada átona, cerrada átona + abierta)


La consonante se define por no poder ser núcleo silábico ni constituir sílaba por sí misma.

Aunque técnicamente no pertenece al español, sino al euskera, dado el uso frecuente grupo consonántico 'tx' como equivalente a la grafía 'ch', se ha considerado inseparable en los mismos contextos que otros casos como tr, pr, br, etc.

Por convención, la consonante 'x' se agrupa con la vocal siguiente (é-xi-to), si bien fonéticamente representa dos sonidos que pertenecen a sílabas distintas ['ek.si.to]

## Semivocales y semiconsonantes

El grafema 'y' es tratado como vocal en posición interconsonántica y como consonante en posición intervocálica.

Los grafemas 'w' (semiconsonante) y 'h' (muda, aunque no es infrecuente su aspiración en el habla) son tratadas siempre como consonantes, por lo que algunas palabras, especialmente los **extranjerismos**, pueden recibir una segmentación incorrecta, cercana a la división hecha por un hispanohablante que desconociera completamente la fonética del idioma original: 'joc-key'.


## Prefijos

Algunos prefijos ('sub', 'psi' o 'pso') producen errores de segmentación según el contexto ('su-bín-dice*' por 'sub-ín-di-ce', 'pa-rap-si-có-lo-go*' por 'pa-ra-psi-có-lo-go', etc). La causa es que estos elementos no siguen la regla general de agrupamiento cuando se perciben como unidad con significado independiente cuya identidad de sentido queda marcada fonéticamente, si bien existen casos límite donde el prefijo está prácticamente lexicalizado 'su-bra-yar / sub-ra-yar'. Esto no ocurre con otras palabras o pseudopalabras donde, por no apreciarse unidad semántica, el hispanohablante se rige por la norma y agrupa la consonante con la vocal que le sigue: 'rap-so-da', 'pep-si', 'su-bli-me'.

## Carácter convencional de la división silábica

Es importante remarcar que, pese a seguir patrones fonéticos de división, se está trabajando con una abstracción de los sonidos, las llamadas letras o grafemas, y un conjunto aceptado de convenciones sobre cómo se pronuncian estas. Si transcribiéramos los sonidos realmente pronunciados por un hablante concreto el silabeo podría ser muy distinto. Por ejemplo, la palabra "doce" pronunciada por muchos hispanohablantes tendría una única sílaba y diversas representaciones /'dos/, /'doh/ etc., frente a las dos sílabas /do-ce/ que asumimos al verlas por escrito.
