# Static Power

## 1. Definition: What is **Static Power**?
**Static Power** se refiere a la potencia consumida por un circuito digital cuando no está realizando ninguna operación activa, es decir, cuando está en un estado de reposo o inactivo. Esta forma de consumo de energía es crucial en el diseño de circuitos digitales, especialmente en sistemas VLSI (Very Large Scale Integration), donde la eficiencia energética se ha convertido en un aspecto fundamental debido a la alta densidad de componentes y la necesidad de prolongar la vida útil de la batería en dispositivos móviles.

El **Static Power** es principalmente resultado de la fuga de corriente en transistores, que ocurre incluso cuando no hay conmutación de señales. Esta fuga puede ser atribuida a varios mecanismos, como la corriente de subumbral, la corriente de puerta, y la corriente de fuga de drenaje. La importancia del **Static Power** radica en su impacto en el rendimiento y la fiabilidad de los circuitos. A medida que la tecnología avanza hacia nodos de proceso más pequeños, la reducción de voltajes y el aumento de la densidad de integración han llevado a un incremento en las corrientes de fuga, lo que a su vez incrementa el consumo de **Static Power**. Por lo tanto, entender y gestionar el **Static Power** es esencial para diseñadores de circuitos y arquitectos de sistemas que buscan optimizar el rendimiento energético y minimizar el costo operativo de los dispositivos electrónicos.

Además, el **Static Power** tiene implicaciones significativas en el diseño térmico y en la gestión de la energía de los sistemas. Un aumento en el consumo de **Static Power** puede llevar a un calentamiento excesivo, lo que afecta la fiabilidad y la vida útil de los componentes. Por lo tanto, la evaluación del **Static Power** no solo es importante desde una perspectiva de diseño, sino también desde un punto de vista de sostenibilidad y eficiencia energética a largo plazo.

## 2. Components and Operating Principles
Los componentes que contribuyen al **Static Power** en un circuito digital son diversos y complejos. A continuación, se describen los principales mecanismos que generan el consumo de **Static Power** y sus principios de funcionamiento.

### 2.1 Subthreshold Leakage
La corriente de subumbral es uno de los principales contribuyentes al **Static Power**. Esta corriente ocurre en transistores MOSFET cuando el voltaje de puerta está por debajo del umbral necesario para encender el transistor. En este estado, aunque el transistor no está completamente activado, permite que una pequeña cantidad de corriente fluya entre el drenaje y la fuente. A medida que los nodos de proceso se reducen, la corriente de subumbral se convierte en un factor crítico en el consumo de energía, lo que requiere técnicas de diseño avanzadas para mitigar su efecto.

### 2.2 Gate Leakage
La corriente de fuga de puerta se produce debido a la tunneling cuántica en la región de la puerta del transistor. Este fenómeno se vuelve más prominente a medida que se disminuye el tamaño de la puerta y se utilizan materiales de alta constante dieléctrica. La gestión de la corriente de fuga de puerta es esencial en el diseño de circuitos, ya que puede contribuir significativamente al **Static Power** en dispositivos en reposo.

### 2.3 Drain-Induced Barrier Lowering (DIBL)
El fenómeno de DIBL también juega un papel importante en el consumo de **Static Power**. A medida que se reduce el voltaje de drenaje, puede disminuir la barrera de potencial en el transistor, permitiendo que más corriente fluya, incluso en estado de reposo. Esto se convierte en un desafío en el diseño de circuitos, ya que puede llevar a un aumento no deseado en el consumo de energía.

### 2.4 Impact of Technology Scaling
La reducción de las dimensiones del transistor, conocida como escalado tecnológico, tiene un efecto directo en el **Static Power**. A medida que los transistores se hacen más pequeños, los mecanismos de fuga se vuelven más pronunciados, lo que lleva a un aumento en el consumo de **Static Power**. Por lo tanto, los diseñadores deben considerar cuidadosamente el impacto del escalado en el diseño de circuitos y buscar soluciones innovadoras, como el uso de transistores de alto rendimiento y técnicas de diseño de bajo consumo.

## 3. Related Technologies and Comparison
El **Static Power** se puede comparar con el **Dynamic Power**, que es la potencia consumida durante la conmutación de estados en un circuito. Mientras que el **Static Power** se produce en estado de reposo, el **Dynamic Power** se genera durante la actividad del circuito, principalmente debido a la carga y descarga de capacitancias. Esta comparación es fundamental para entender cómo los diseñadores pueden optimizar el consumo de energía en sus circuitos.

### 3.1 Features and Advantages
Una de las ventajas del **Static Power** es que proporciona una medida constante de consumo de energía, lo que permite a los diseñadores prever el rendimiento energético de un sistema a lo largo del tiempo. Sin embargo, el **Dynamic Power** puede ser más difícil de predecir, ya que depende de la frecuencia de operación y del patrón de conmutación de las señales. En aplicaciones donde la actividad del circuito es intermitente, el **Static Power** puede ser un factor determinante en el consumo total de energía.

### 3.2 Disadvantages
El principal inconveniente del **Static Power** es que, a medida que los nodos tecnológicos se reducen, su contribución al consumo total de energía aumenta, lo que puede llevar a desafíos de gestión térmica y fiabilidad. En contraste, el **Dynamic Power** puede ser reducido mediante técnicas de diseño que minimizan la frecuencia de operación y optimizan las rutas de señal.

### 3.3 Real-World Examples
En dispositivos móviles, donde la duración de la batería es crítica, la gestión del **Static Power** se ha vuelto esencial. Por ejemplo, los procesadores modernos utilizan técnicas como el "Dynamic Voltage and Frequency Scaling" (DVFS) para ajustar el voltaje y la frecuencia en función de la carga de trabajo, minimizando así el **Static Power** y mejorando la eficiencia energética. Además, en aplicaciones de IoT (Internet of Things), donde los dispositivos a menudo operan en modo de bajo consumo, la reducción del **Static Power** es una prioridad en el diseño de circuitos.

## 4. References
- IEEE (Institute of Electrical and Electronics Engineers)
- ACM (Association for Computing Machinery)
- International Solid-State Circuits Conference (ISSCC)
- Semiconductor Industry Association (SIA)

## 5. One-line Summary
El **Static Power** es la potencia consumida por un circuito digital en reposo, crucial para el diseño eficiente de sistemas VLSI y la gestión de la energía en dispositivos electrónicos.