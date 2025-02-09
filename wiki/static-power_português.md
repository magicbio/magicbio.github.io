# Static Power

## 1. Definition: What is **Static Power**?
**Static Power**, no contexto do design de circuitos digitais, refere-se à potência consumida por um circuito eletrônico quando ele está em estado de repouso, ou seja, quando não está realizando nenhuma operação ativa. Este consumo de energia é crucial para a eficiência energética de dispositivos eletrônicos, especialmente em sistemas VLSI (Very Large Scale Integration), onde múltiplos componentes operam simultaneamente. A importância do **Static Power** se torna evidente em aplicações onde a eficiência energética é primordial, como em dispositivos móveis e sistemas embarcados, onde a duração da bateria é uma consideração crítica.

O **Static Power** é predominantemente causado por dois fatores principais: a corrente de fuga (leakage current) e a corrente de polarização (bias current). A corrente de fuga ocorre devido à subtransistores, mesmo quando estes estão em estado "off", e é influenciada por fatores como temperatura e tecnologia de fabricação. A corrente de polarização, por outro lado, pode ser intencionalmente introduzida em circuitos para garantir um desempenho adequado em certas condições operacionais.

Entender o **Static Power** é fundamental para engenheiros e projetistas, pois permite otimizar o desempenho e a eficiência dos circuitos. Isso envolve o uso de técnicas como o dimensionamento adequado de transistores, a escolha de materiais com propriedades de fuga reduzidas, e a implementação de estratégias de desligamento (power gating) para minimizar o consumo de energia em estados ociosos.

## 2. Components and Operating Principles
Os principais componentes que influenciam o **Static Power** incluem transistores, resistores e capacitores, cada um desempenhando um papel vital na determinação da quantidade de energia consumida em estado de repouso. A interação entre esses componentes é complexa e depende de vários fatores, incluindo a tecnologia de fabricação e a arquitetura do circuito.

### 2.1 Transistores
Os transistores, especialmente os MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors), são os principais responsáveis pela corrente de fuga em circuitos digitais. A corrente de fuga pode ser classificada em várias categorias, como a subthreshold leakage, gate-induced drain leakage (GIDL) e junction leakage. Cada uma dessas correntes de fuga tem características distintas e varia de acordo com a tensão aplicada e a temperatura, tornando o controle do **Static Power** um desafio significativo.

### 2.2 Resistores e Capacitores
Os resistores e capacitores também desempenham um papel no consumo de **Static Power**. Em circuitos que utilizam resistores de pull-up ou pull-down, a resistência pode contribuir para a corrente de polarização, resultando em um consumo adicional de energia. Capacitores, embora mais associados ao consumo dinâmico, podem influenciar o comportamento de corrente em estados de transição, afetando indiretamente o **Static Power**.

### 2.3 Métodos de Implementação
Os métodos de implementação para controlar o **Static Power** incluem técnicas como o uso de transistores de canal duplo (dual-channel transistors) e a adoção de tecnologias de fabricação avançadas, que buscam reduzir a corrente de fuga. Além disso, estratégias de projeto como o uso de células de memória de baixa potência e circuitos de desligamento são amplamente utilizadas para minimizar o impacto do **Static Power** em dispositivos.

## 3. Related Technologies and Comparison
Ao comparar o **Static Power** com outras tecnologias, como o **Dynamic Power**, é essencial entender as diferenças fundamentais entre esses conceitos. O **Dynamic Power** refere-se ao consumo de energia que ocorre quando um circuito está ativo e realizando operações, sendo diretamente proporcional à frequência do clock e ao número de transistores que mudam de estado.

### Comparação de Características
- **Static Power**:
  - Consumo constante em repouso.
  - Principalmente causado por corrente de fuga.
  - Influenciado por temperatura e tecnologia de fabricação.

- **Dynamic Power**:
  - Consumo variável baseado na atividade do circuito.
  - Depende da frequência do clock e da capacitância.
  - Pode ser otimizado através de técnicas de redução de capacitância e diminuição da frequência.

### Vantagens e Desvantagens
A principal vantagem do **Static Power** é que ele fornece uma visão clara do consumo de energia em estados ociosos, permitindo que projetistas implementem soluções para mitigar esse consumo. No entanto, a desvantagem é que, à medida que as tecnologias de fabricação avançam e os transistores se tornam menores, a corrente de fuga tende a aumentar, exacerbando o problema do **Static Power**.

### Exemplos do Mundo Real
Em dispositivos móveis, a gestão do **Static Power** é crucial para prolongar a vida útil da bateria. Tecnologias como o **power gating** e o uso de transistores de baixa fuga são amplamente aplicadas para garantir que o consumo de energia em estado de repouso seja minimizado. Em contraste, em circuitos de alto desempenho, como processadores de servidores, o **Dynamic Power** pode ser mais crítico, mas ainda assim, o **Static Power** não deve ser negligenciado, pois contribui significativamente para o consumo total de energia.

## 4. References
- IEEE (Institute of Electrical and Electronics Engineers)
- ACM (Association for Computing Machinery)
- SEMI (Semiconductor Equipment and Materials International)
- ISSCC (International Solid-State Circuits Conference)
- TSMC (Taiwan Semiconductor Manufacturing Company)

## 5. One-line Summary
**Static Power** é a potência consumida por circuitos eletrônicos em estado de repouso, crucial para a eficiência energética em sistemas VLSI e dispositivos móveis.