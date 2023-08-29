import numpy as np 
import pandas as pd
ventas = np.random.randint(1000,5000,12)
pautas_publicitarias = np.random.randint(1500,3000,12)
df = pd.DataFrame({"ventas": ventas, "pautas publicitarias": pautas_publicitarias})
print(df)
df.plot(kind="scatter", x="ventas", y="pautas publicitarias", title="grafico", figsize=(5,5))
print ("venta mas baja ", df["ventas"].min())
print ("venta mas alta ", df["ventas"].max())
print ("venta promedio ", df["ventas"].mean())
ventasaltas=df["ventas"][df["ventas"]> df["ventas"].mean()]
print ("ventas mayores al promedio", len(ventasaltas))