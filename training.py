import pandas as pd
'''
df=pd.DataFrame([["jack",24],["rose",18]],columns=["name","age"])
df.to_csv("person.csv")
'''
url="https://github.com/venky14/Machine-Learning-with-Iris-Dataset/blob/master/Iris.csv"
columns=["Id","SepalLengthCm"]
df=pd.read_csv(url,delimiter="\n",names=columns)#index_col=["Id"])
print(df.head(2))
