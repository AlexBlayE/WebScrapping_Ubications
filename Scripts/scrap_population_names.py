import pandas as pd
import requests as rq

web_path = r"https://www.idescat.cat/indicadors/?id=aec&n=15903"

taula_poblacio = rq.get(web_path)

llista_taules = pd.read_html(taula_poblacio.content, encoding="utf-8", flavor="html5lib", decimal=",", thousands=".")

poblacions = llista_taules[0]

poblacions.drop("Codi", axis=1, inplace=True)
poblacions.drop([947, 948, 949, 950],axis=0, inplace=True)

poblacions["Municipi"].replace([", la", ", '", ", els", ", el", ", les",", l'"], "", regex=True, inplace=True)
poblacions["Població"].replace([".00",],"", regex=True, inplace=True)

poblacions.to_csv(r".\CSV\populations.csv", sep=",", index=False)