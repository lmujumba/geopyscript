
import geopy
import folium
import pandas as pd
from geopy import Nominatim

nom=Nominatim(user_agent="map.ipynb")

#m = folium.Map(location=[-1.2832533, 36.8172449])
nairobi=nom.geocode("00200,Nairobi")


# %%
def mapScript():
    #get the user input and produce the output
    userInput=input('Enter a zip code,City')
    jojo=nom.geocode(userInput)
    print(jojo)


# %%
mapScript()


# %%
count=0
with open("/home/lewis/Documents/maps.txt","r+") as file:
    with open("/home/lewis/Documents/newmaps.txt","a+") as newfile:
        data=file.readlines()

        #get the geolocation
        #write the golocation to file
        for item in data:
            jojo=nom.geocode(item)
            #print(jojo,"\n")
            count+=1
            newfile.write(str(count)+":" + str(jojo) + '\n')
            df2=pd.DataFrame(jojo)
            


with open("/home/lewis/Documents/newmaps.txt","r+") as newfile:
    data2=newfile.readlines()
    for item in data2:
        print(item)
            

    


# %%
df2=pd.read_csv('/home/lewis/Documents/newmaps.txt')


# %%
df2


# %%



