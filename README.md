# Laboratorio 1: Simulación de un Robot Móvil Diferencial en Webots


## Descripción

En este laboratorio se estudia el comportamiento cinemático de un robot móvil diferencial, analizando cómo las velocidades de sus ruedas determinan su movimiento. Se evalúan distintos tipos de trayectorias y el efecto de perturbaciones en los actuadores.

---

## Ejecución

1. Abrir Webots  
2. Cargar el mundo desde la carpeta `worlds/` (archivo `Lab1.wbt`)  
3. Seleccionar el controller correspondiente:
   - `my_controller` → experimentos básicos  
   - `my_controllerdesafio` → desafíos  
   - `my_controllerperturbacion` → perturbaciones  
4. Ejecutar la simulación  

---

## Experimentos

### Movimiento recto

![Recta](images/LineaRecta1.png)
![Recta](images/LineaRecta3.png)
![Recta](images/LineaRecta2.png)
![Recta](images/LineaRecta4.png)

Cuando ambas ruedas tienen la misma velocidad (vr = vl), la velocidad angular es cero (ω = 0), por lo que el robot no rota y se desplaza en línea recta.

---

### Trayectoria curva

![Curva](images/Curva1.png)
![Curva](images/Curva2.png)
![Curva](images/Curva3.png)
![Curva](images/Curva4.png)
![Curva](images/Curva5.png)

Cuando las velocidades son diferentes (vr ≠ vl), se genera una velocidad angular distinta de cero (ω ≠ 0), lo que provoca que el robot siga una trayectoria curva.

---

### Rotación en el lugar

![Rotacion](images/Rotacion1.png)
![Rotacion](images/Rotacion2.png)
![Rotacion](images/Rotacion3.png)

Cuando las ruedas giran en sentidos opuestos (vr = -vl), la velocidad lineal es cero (v = 0) y el robot rota sobre su propio eje sin desplazarse.

---

## Desafíos

### Movimiento circular

![Circulo](images/Circulo1.png)
![Circulo](images/Circulo2.png)
![Circulo](images/Circulo3.png)
![Circulo](images/Circulo4.png)
![Circulo](images/Circulo5.png)
![Circulo](images/Circulo6.png)
![Circulo](images/Circulo7.png)

[![Ver video](images/FotoVideo1.png)](videos/VideoCirculo.mp4)

El movimiento circular se obtiene al mantener velocidades constantes pero diferentes en cada rueda, generando una combinación constante de velocidad lineal y angular.

---

## Extensión: Perturbaciones

### Comparación

**Sin perturbaciones:**
Movimiento estable y predecible.
[![Ver video](images/FotoVideo3.png)](videos/VideoNormal.mp4)

**Con perturbaciones:**
[![Ver video](images/FotoVideo2.png)](videos/VideoPerturbaciones.mp4)

Las perturbaciones introducen variaciones aleatorias en las velocidades de las ruedas, lo que altera tanto la velocidad lineal como angular del robot. Como resultado, la trayectoria deja de ser ideal y presenta desviaciones, evidenciando la sensibilidad del sistema a pequeños cambios en las velocidades.

---

## Análisis

Los resultados observados coinciden con el modelo cinemático del robot diferencial:

Si vr = vl → ω = 0 → movimiento recto
Si vr ≠ vl → ω ≠ 0 → trayectoria curva
Si vr = -vl → v = 0 → rotación en el lugar

Además, se observa que pequeñas variaciones en las velocidades (perturbaciones) generan cambios significativos en la trayectoria, demostrando que el sistema es altamente sensible a las condiciones de entrada.

---

## Preguntas de análisis

1. ¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?

Cuando ambas ruedas tienen la misma velocidad (vr = vl), la velocidad angular es cero (ω = 0), por lo que el robot no rota y se desplaza en línea recta.

---

2. ¿Cómo cambia la trayectoria cuando las velocidades son diferentes?

Cuando las velocidades son diferentes (vr ≠ vl), se genera una velocidad angular distinta de cero (ω ≠ 0), lo que provoca que el robot describa una trayectoria curva.

---

3. ¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?

Cuando las ruedas giran en sentidos opuestos (vr = -vl), la velocidad lineal es cero (v = 0), por lo que el robot rota sobre su propio eje sin desplazarse.

---

4. ¿Qué tipo de movimiento permite dibujar un círculo?

Un movimiento circular se obtiene cuando las velocidades de las ruedas son constantes pero diferentes, generando una combinación de velocidad lineal y angular constante.

---

## Conclusión

Se comprobó experimentalmente el modelo cinemático del robot diferencial, verificando la relación entre las velocidades de las ruedas y el tipo de movimiento generado.
Asimismo, se evidenció que pequeñas perturbaciones producen desviaciones en la trayectoria ideal, lo que destaca la importancia de un control preciso en sistemas robóticos.
