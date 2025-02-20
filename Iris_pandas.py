import pandas as pd


def mylog(msg):
    print("*" * 50)
    print(msg)
    print("*" * 50)


mylog("Datei einlesen")
df = pd.read_csv("/Users/student-sbs/Library/CloudStorage/OneDrive-sbs-herzogenaurach.de/2-PG/Karats_Python/iris.csv")
mylog("Erste und letzten 5 Zeilen ausgeben")
print(df.head(5), "\n" + "-" * 50 + "\n", df.tail(5))
mylog("CSV Zusammenfassung")
print(df.info())

mylog("Spaltenfilterung")
filter = df[['sepal.length', 'sepal.width']]
print(filter.head(10))
mylog("rowfilterung")
rowfilter = df[df['species'] == 'Setosa']
print(rowfilter)
mylog("rowfilterung mit nummern")
rowfilter_number = df[df["petal.length"] > 1.5]
print(rowfilter_number)

mylog("add column")
df["sepal.area"] = df["sepal.length"] * df["sepal.width"]
print(df.head(10))

mylog("replace values")
print(df['species'].map({'Setosa': 'S', 'Versicolor': 'Ve', 'Virginica': 'Vi'}))
df["species"] = df["species"].replace(regex='Setosa', value='S')
df["species"] = df["species"].replace(regex='Versicolor', value='Ve')
df["species"] = df["species"].replace(regex='Virginica', value='Vi')
print(df)

mylog("delete rows")
rowfilter_for_delete = df[df["sepal.length"] < 4.5]
print(rowfilter_for_delete)
