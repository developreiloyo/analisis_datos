# Análisis de Rentabilidad y Comportamiento de Clientes

Este proyecto tiene como objetivo analizar los datos de ventas de una tienda online para obtener insights sobre la rentabilidad por categoría de producto, comportamiento de clientes (análisis RFM), productos con baja rentabilidad y patrones estacionales en las compras.

---

## 🎯 Objetivos del Análisis

1. **Análisis de Rentabilidad por Categoría de Producto**
   - Ganancia neta por categoría = ingresos - costos - descuentos - envíos
   - Identificar qué categorías generan mayor y menor margen de ganancia.

2. **Análisis RFM (Recency, Frequency, Monetary) de Clientes**
   - Clasificación de clientes según su recencia, frecuencia y valor monetario.
   - Identificación de los clientes más valiosos.

3. **Detección de Productos con Baja Rentabilidad o Alta Tasa de Devolución**
   - Descubrir productos o categorías con altas devoluciones o pérdidas económicas.

4. **Análisis de Frecuencia de Compra y Ciclos Estacionales**
   - Determinar con qué frecuencia compran los clientes.
   - Detectar picos de venta en ciertos meses.

5. **Sugerencia de Segmentación para Campañas de Marketing**
   - Recomendaciones basadas en RFM, tipo de producto comprado, país y método de pago.

---

## 📁 Archivos necesarios

### 1. `orders.csv`
- Contiene todos los pedidos realizados.
  - `order_id`: ID del pedido
  - `customer_id`: ID del cliente
  - `order_date`: Fecha del pedido
  - `order_status`: Estado del pedido (Completed, Cancelled, Returned)
  - `shipping_cost`: Costo de envío
  - `payment_method`: Método de pago
  - `total_amount`: Monto total del pedido

### 2. `order_items.csv`
- Detalles por producto de cada pedido.
  - `order_id`: ID del pedido
  - `product_id`: ID del producto
  - `category`: Categoría del producto
  - `product_name`: Nombre del producto
  - `quantity`: Cantidad vendida
  - `unit_price`: Precio unitario
  - `discount`: Porcentaje de descuento aplicado

### 3. `customers.csv`
- Información de los clientes.
  - `customer_id`: ID del cliente
  - `name`: Nombre del cliente
  - `email`: Email del cliente
  - `signup_date`: Fecha de registro
  - `country`: País del cliente

### 4. `products.csv`
- Información general de los productos.
  - `product_id`: ID del producto
  - `category`: Categoría del producto
  - `product_name`: Nombre del producto

---

## 🔧 Herramientas y Librerías Utilizadas

- **Python**
- **Pandas**: Para manipulación y análisis de datos.
- **NumPy**: Para operaciones numéricas.
- **Matplotlib / Seaborn**: Para visualización de resultados.
- **Jupyter Notebook**: Entorno de desarrollo interactivo.
- **IPython.display**: Para mostrar tablas formateadas.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display as dp
```

### 1. Carga de Datos
```python
carp = 'documents'
customer_rut = os.path.join(carp, 'customers.csv')
order_item_rut = os.path.join(carp, 'order_items.csv')
orders_rut = os.path.join(carp, 'orders.csv')
products_rut = os.path.join(carp, 'products.csv')
```
### 2. Extraccion de Documentos
```python
customer = pd.read_csv(customer_rut)
order_item = pd.read_csv(order_item_rut)
orders = pd.read_csv(orders_rut)
products = pd.read_csv(products_rut)
```

### 3. Filtrado de Pedidos Completados
```python
complete_orders = orders[orders['order_status'] == 'Completed']
```
### 4. Fusión de Tablas
```python
merge_item = pd.merge(order_item, complete_orders, on='order_id')
```
### 5. Cálculo de Ingresos y Costos
```python
merge_item['ingreso_bruto'] = merge_item['unit_price'] * merge_item['quantity']
merge_item['descuento'] = merge_item['unit_price'] * merge_item['discount'] / 100 * merge_item['quantity']
merge_item['costo'] = merge_item['cost_price'] * merge_item['quantity']
```
### 6. Resumen por Categoría
```python
resumen_categoria = merged.groupby('category').agg({
    'ingreso_bruto': 'sum',
    'costo': 'sum',
    'descuento': 'sum',
    'shipping_cost': 'sum'
})
resumen_categoria['ganancia_neta'] = resumen_categoria['ingreso_bruto'] - resumen_categoria['costo'] - resumen_categoria['descuento'] - resumen_categoria['shipping_cost']
```
### 7. Análisis RFM
```python
rfm = (
    merge_item.groupby('customer_id')
    .agg(
        Recency=('order_date', lambda x: (pd.to_datetime('today') - pd.to_datetime(x).max()).days),
        Frequency=('order_id', 'nunique'),
        Monetary=('ingreso_bruto', 'sum')
    )
)
```
### 📊 Resultados Principales
    Categorías más rentables:  [Ejemplo: "Electrónica" con ganancia neta alta].
    Categorías menos rentables:  [Ejemplo: "Decoración" con pérdidas].
    Clientes más valiosos:  Clasificados por RFM en cuartiles.
    Productos con devoluciones altas:  [Listado con razón de devolución].
    Patrones estacionales:  Mayor volumen de ventas en noviembre y diciembre.
    Recomendaciones de marketing:  Enfocarse en clientes con alto RFM y promocionar categorías con márgenes altos.
     
## 📌 Conclusión

Este análisis permitió obtener una visión integral del desempeño comercial de la empresa, identificando áreas de mejora, oportunidades de crecimiento y posibles riesgos. Los hallazgos pueden ser utilizados para tomar decisiones informadas en estrategias de precios, logística, atención al cliente y campañas de marketing.

## 👥 Autores

Este ejercicio es una adaptación basada en el contenido original del canal de YouTube **@automatiza-con-max**, creado por **Max**.

🔗 [Visita su canal](https://www.youtube.com/@automatiza-con-max) 

> Este trabajo se inspira en los tutoriales realizados por Max, enfocado en la automatización con Python y análisis de datos.
