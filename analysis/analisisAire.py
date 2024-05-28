import pandas as pd

from data.generators.generadorAire import generarDatosCalidadAire

def construirAireDataFrame():
    dataAire=generarDatosCalidadAire()

    #generamos el dataframe

construirAireDataFrame=pd.DataFrame(generarDatosCalidadAire,colums=['nombre','comuna','ica','fecha','correo'])


construirAireDataFrame()

