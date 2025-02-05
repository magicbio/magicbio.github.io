# Combinational Equivalence Checking (Francais)

## Définition formelle

Le Combinational Equivalence Checking (CEC) est une technique utilisée en conception de circuits intégrés pour vérifier si deux circuits logiques, généralement représentés sous forme de réseaux logiques, produisent les mêmes sorties pour chaque combinaison possible d'entrées. En d'autres termes, CEC confirme que deux représentations différentes d'un même circuit (ou d'une même fonction logique) sont équivalentes, ce qui est crucial lors de la vérification de la validité des modifications apportées à la conception, telles que celles effectuées lors de l'optimisation ou de la mise à niveau des composants.

## Contexte historique et avancées technologiques

Le concept de CEC a émergé dans les années 1970 avec l'avènement de la conception assistée par ordinateur (CAD) pour les circuits intégrés. À cette époque, la complexité croissante des circuits nécessitait des méthodes formelles pour garantir la fiabilité des conceptions. Les premières approches reposaient principalement sur des techniques basées sur la simulation, mais elles étaient limitées par le nombre d'entrées et la profondeur des circuits.

Avec l'essor des technologies de fabrication et la miniaturisation des composants, des méthodes plus avancées, telles que la vérification formelle, ont été développées dans les années 1990. Ces méthodes utilisent des algorithmes sophistiqués pour prouver mathématiquement l'équivalence entre les circuits. Cela a permis de traiter des designs de plus en plus complexes, notamment ceux des circuits intégrés spécifiques à une application (Application Specific Integrated Circuits - ASIC) et des systèmes sur puce (System on Chip - SoC).

## Technologies connexes et fondamentaux d'ingénierie

### Vérification formelle vs simulation

La vérification formelle et la simulation sont deux approches complémentaires dans le domaine de la vérification de circuits :

- **Vérification formelle** : Utilise des méthodes mathématiques pour prouver que deux circuits sont équivalents, indépendamment des entrées. Elle est exhaustive et peut gérer des cas complexes, mais peut être limitée par des problèmes de complexité computationnelle.

- **Simulation** : Implique de tester les circuits sous un ensemble limité de conditions d'entrée. Bien qu'elle soit moins exhaustive, elle est souvent plus rapide et plus simple à mettre en œuvre pour des designs moins complexes.

### Outils de CEC

Plusieurs outils de conception assistée par ordinateur sont disponibles pour réaliser le CEC, dont :

- **ABC** : Un outil open-source pour la vérification et l'optimisation des circuits.
- **Cadence** : Offre des solutions complètes pour le CEC dans le cadre de son environnement de conception.

## Tendances récentes

Les tendances récentes en matière de CEC incluent l'amélioration des algorithmes pour réduire le temps de calcul et la consommation de mémoire, ainsi que l'intégration d'outils d'apprentissage automatique pour faciliter la tâche. La demande croissante pour des systèmes de plus en plus complexes, tels que l'intelligence artificielle (IA) et l'Internet des objets (IoT), pousse les chercheurs à développer des méthodes plus efficaces pour gérer la vérification de circuits à grande échelle.

## Applications majeures

Le Combinational Equivalence Checking trouve des applications dans divers domaines, notamment :

- **Conception de circuits intégrés** : Pour valider les modifications apportées à la conception des ASIC et des FPGA (Field-Programmable Gate Arrays).
- **Systèmes embarqués** : Pour garantir la fiabilité des systèmes critiques dans des domaines tels que l'automobile et l'aéronautique.
- **Sécurité des systèmes** : Pour vérifier l'intégrité des circuits utilisés dans des applications sensibles.

## Tendances de recherche actuelles et directions futures

Actuellement, la recherche en CEC se concentre sur plusieurs domaines clés :

- **Méthodes basées sur l'apprentissage automatique** : Pour améliorer les performances des algorithmes de CEC et réduire le temps de vérification.
- **Vérification de circuits à plusieurs niveaux** : Pour gérer la complexité croissante des systèmes modernes.
- **Intégration de CEC avec d'autres méthodes de vérification** : Pour une approche plus holistique de la validation des conceptions.

## Comparaison : CEC vs Système de Vérification de Propriétés (Property Checking)

### CEC

- **Objectif** : Vérifier l'équivalence de deux circuits.
- **Méthode** : Utilise des techniques formelles pour prouver l'équivalence.
- **Applications** : Validation de modifications dans des circuits.

### Système de Vérification de Propriétés

- **Objectif** : Vérifier si un circuit satisfait certaines propriétés spécifiées.
- **Méthode** : Peut utiliser des méthodes formelles, mais se concentre sur des propriétés spécifiques plutôt que sur l'équivalence.
- **Applications** : Utilisé pour assurer la conformité des circuits à des normes de sécurité ou de fonctionnalité.

## Entreprises concernées

- **Synopsys**
- **Cadence Design Systems**
- **Mentor Graphics**
- **Aldec**

## Conférences pertinentes

- **International Conference on Computer-Aided Design (ICCAD)**
- **Design Automation Conference (DAC)**
- **Formal Methods in Computer-Aided Design (FMCAD)**

## Sociétés académiques pertinentes

- **IEEE (Institute of Electrical and Electronics Engineers)**
- **ACM (Association for Computing Machinery)**
- **IEEE Computer Society**

Cet article fournit une vue d'ensemble complète du Combinational Equivalence Checking, de ses principes fondamentaux aux dernières tendances de recherche, et sert de référence pour les chercheurs, les ingénieurs et les étudiants dans le domaine des technologies des semi-conducteurs et des systèmes VLSI.