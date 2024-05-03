# Tema 1:
## Sistemas Raid
| Raid      | Paralelismo | Fiabilidad | Throughput | Coste |
| --------- | ----------- | ---------- | ---------- | ----- |
| 0    | Bloque   | Baja   | Alto | $ |
| 1    | Bloque   | Copia   | Alto | $$$$ |
| 2    | Bits   | Paridad   | Bajo | $$$ |
| 3 | Bits | Paridad | Bajo | $$ |
| 4 | Bloque | Paridad | Alto | $$ |
| 5 | Bloque | Paridad | Alto | $$ |
| 6 | Bloque | Paridad | Alto | $$ |
## Acceso al almacenamiento 
  ### Algoritmo de gestion de la memoria intermedia
  ```
Bloque memoriaIntermedia[TAM_MEM];
    Bloque ObtenerBloque(int numBloque) {
        int indice = BuscarEnMemoriaIntermedia(numBloque);
        if (indice == NO_ENCONTRADO) {
            indice = ObtenerBloqueLibreEnMemoriaIntermedia();
            LeerDeDiscoAMemoriaIntermedia(indice, numBloque);
        }
        return memoriaIntermedia[indice];
}

int ObtenerBloqueLibreEnMemoriaIntermedia () {
    int candidato = BuscarBloqueLibre();
    if (candidato == NO_ENCONTRADO) {
        candidato = ElegirCandidatoALiberar();
        if(HaSidoModificado(candidato)) {
            EscribrirEnDisco(candidato);
      }
    }
    return candidato;
}
```
  ### Gestion de la memoria intermedia
  ```
SELECT p.nombre_cliente, p.numero_prestamo,
c.calle_cliente, c.ciudad_cliente

FROM prestatario p, cliente c
WHERE p.nombre_cliente = c.nombre_cliente
```
```
for each tupla p de prestatario do
    for each tupla c de cliente do
        if p[nombre_cliente] = c[nombre_cliente] then
        begin
            Sea x una tupla definida como:
                x[nombre_cliente] := p[nombre_cliente]
                x[numero_prestamo] := p[numero_prestamo]
                x[calle_cliente] := c[calle_cliente]
                x[ciudad_cliente] := c[ciudad_cliente]
            Incluir x como resultado final
        end
    end
end
```

## Organización de archivos
### 1. A nivel de bloque:
#### - Registros de tamaño fijo
#### - Registros de tamaño variable
#### - Almacenamiento contiguo
#### - Lista libre
#### - Páginas con ranuras
#### - Registros ordenados
### 2. A nivel de archivo
### 3. Organizacion InMemory
## Estructuras físicas y lógicas en oracle
  ### Tablespaces:
  #### El tablespace es el nivel más alto de la estructura logica de la base de datos Oracle y funciona como contendor lógico de los datafiles, que son la estructura física donde se almacena  los datos
  ### Segmentos:
  #### El segmento es la forma lógica de organizar los datos como tablas, indices, particiones de tabla...etc. Dichos segmentos están compuestos por extensiones.
  ### Extensiones:
  #### Grupos de bloques de datos almacenados de forma contigua.
  ### Bloque de datos:
  #### Los bloques de datos son las unidades más pequeñas de la estructura lógica de almacenamiento y contiene los datos reales.
