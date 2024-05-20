# TEMA3: Transacciones y Control de Concurrencia

### Conceptos
| Concepto      | Definición |
| --------- | ----------- |
| Transacción | Secuencia de operaciones realizadas como una única unidad de proceso lógico, que debe ser ejecutada en su totalidad o no ejecutarse en absoluto para mantener la integridad de los datos |
|  Accciones conflictivas |  si se refieren al mismo objeto y al menos una de ellas es operacion de escritura en diferentes transacciones  |
| Schedule   | orden cronológico en el que se ejecutan acciones   |
| Schedule Secuencial | Aquel en el que no se solapan las transacciones |

### Propiedades de una transaccion (ACID):
- Atomicidad: garantiza que todas las operaciones de una transaccion se realizan o ninguna realiza.
- Consistencia: sólo permite cambios que llevan a la BD de un estado consistente a otro consistente.
- Aislamiento: protege a las transacciones de las interferencias de otras transacciones concurrentes.
- Durabilidad: si una transaccion se ha confirmado, sus resultados son permanentes.

### Teorema CAP:
- Consistencia: cada nodo en un sistema distribuido muestra la misma informacion al mismo tiempo
- Avialbility: el sistema garantiza que cada recibe un feedback en caso de exito o fallo.
- Partition Tolerance: el sistema continua funcionando en caso de 'particiones' (fallos de comunicación)

## Determinar si una planificación es conflicto-serializable
### Metodos
| Método     | Funcionamiento |
| --------- | ----------- |
| Intercambios de acciones adyacentes no conflictivas| S1, S2 son schedules conflicto-equivalentes si S1 puede ser transformado en S2 mediante una serie de intercambios de acciones adyacentes no conflictivas. |
| Grafo de Presedencia | P(S1) acíclico 'no hay ciclos' <--> S1 conflicto-serializable |
| Protocolo de bloque en 2 fases | Tres reglas:  |