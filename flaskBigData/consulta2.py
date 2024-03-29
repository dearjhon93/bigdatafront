import pandas as pd
import os
import time

start = time.time()
df = pd.DataFrame()
# nameFinalFile="consulta2_hasta2008.csv"
archivos=os.listdir("./csvs")
#decomentar las siguientes 2 lineas para generar los datos solo hasta 2007
archivos.pop()#para no tomar en cuenta el ultimo csv en este caso el 2008
nameFinalFile="consulta2_hasta2007.csv"
for filename in archivos:
    print(filename)
    speedlayerview = pd.read_csv("./csvs/" + filename, encoding="windows-1251")[
        ["ArrDelay", "DepDelay", "Origin", "Dest", "CarrierDelay", "WeatherDelay", "UniqueCarrier"]]
    # consulta dos por aerolinea
    vistaatrasosRdes = speedlayerview.groupby(['UniqueCarrier']).agg(
        {"ArrDelay": tuple}).reset_index()  # retrasos llegada
    vistaatrasosRdes["retrasosLlegada"] = vistaatrasosRdes['ArrDelay'].apply(lambda x: len([i for i in x if i > 0]))
    vistaatrasosRorg = speedlayerview.groupby(['UniqueCarrier']).agg(
        {"DepDelay": tuple}).reset_index()  # retrasos salida
    vistaatrasosRorg["rorg"] = vistaatrasosRorg['DepDelay'].apply(lambda x: len([i for i in x if i > 0]))
    consulta2 = vistaatrasosRorg.assign(rdes=vistaatrasosRdes["retrasosLlegada"])[["UniqueCarrier", "rorg", "rdes"]]
    print(consulta2)
    df = pd.concat([df, consulta2])

originretarases=df.groupby(['UniqueCarrier']).agg({"rorg": tuple}).reset_index()#retrasos llegada
originretarases["rorg"]= originretarases['rorg'].apply(lambda x: sum(x))
destinretarases=df.groupby(['UniqueCarrier']).agg({"rdes": tuple}).reset_index()#retrasos llegada
destinretarases["rdes"]= destinretarases['rdes'].apply(lambda x: sum(x))
dfFinal=originretarases.assign(rdes=destinretarases["rdes"])
dfFinal.to_csv(nameFinalFile, index=False)
print(dfFinal)
end = time.time()
print("time",end - start)