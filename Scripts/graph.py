import pandas as pd
import matplotlib.pyplot as plt

mapa = pd.read_csv(r"CSV\populations_with_ubications.csv", sep=",", decimal=".")

mapa.dropna()

plt.scatter(x=mapa["Latitud"], y=mapa["Longitud"], alpha=0.4, s=mapa["Superfície (km²)"],
            label="Superficie", c=mapa["Població"], cmap=plt.get_cmap("jet"), )
plt.colorbar(label="Població")
plt.legend()
plt.show()