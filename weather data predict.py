from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
df = pd.read_csv('Weather Data.csv')
df.head()
df.info()
df.Press_kPa = df.Press_kPa.astype(float)
df.isna().sum()
df.duplicated().sum()
df=df.drop(["Date/Time"], axis = 1)
df.Weather.unique()
df.Weather.value_counts()
df.Weather = df.Weather.apply(lambda x: "Cloudy" if "Cloudy" in x else x)
df.Weather = df.Weather.apply(lambda x: "Clear" if "Clear" in x else x)
df.Weather = df.Weather.apply(lambda x: "Snow" if "Snow" in x else x)
df.Weather = df.Weather.apply(lambda x: "Fog" if "Fog" in x else x)
df.Weather = df.Weather.apply(lambda x: "Rain" if "Rain" in x else x)

df.Weather = df.Weather.apply(lambda x : "other" if x in ['Drizzle','Haze','Freezing Drizzle,Haze', 'Thunderstorms','Freezing Drizzle'] else x)
df.Weather.value_counts()
ohe = OneHotEncoder(handle_unknown='ignore')
weather_encoded = ohe.fit_transform(df[['Weather']]).toarray()
X = df.drop('Weather',axis= 1)
y = weather_encoded
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)
# imputation transformer
trf1 = ColumnTransformer([
    ('impute_Temp_C',SimpleImputer(),[0]),
    ('impute_Dew Point Temp_C',SimpleImputer(),[1]),
    ('impute_Rel Hum_%',SimpleImputer(),[2]),
    ('impute_Wind Speed_km/h',SimpleImputer(),[3]),
    ('impute_Visibility_km',SimpleImputer(),[4]),
    ('impute_Press_kPa',SimpleImputer(),[5]),
    
   ]
                         ,remainder='passthrough')
# one hot encoding
trf2 = ColumnTransformer([
    ('ohe_weather',OneHotEncoder( handle_unknown='ignore'),[6])],remainder='passthrough')
# Scaling
trf3 = ColumnTransformer([('scale',MinMaxScaler(),slice(0,10))])
# train the model
trf5 = DecisionTreeClassifier()
# Alternate Syntax
pipe = make_pipeline(trf1,trf3,trf5)
pipe.fit(X_train,y_train)
y_pred = pipe.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

train_acc = []
test_acc = []
depths = [1,2,3,4,5,6,7,8,9,None]  

for d in depths:
    model = DecisionTreeClassifier(max_depth=d, random_state=42)
    model.fit(X_train, y_train)
    
    train_acc.append(model.score(X_train, y_train))
    test_acc.append(model.score(X_test, y_test))


plt.plot(depths, train_acc, label='Train Accuracy', marker='o')
plt.plot(depths, test_acc, label='Test Accuracy', marker='o')
plt.xlabel('Tree Depth')
plt.ylabel('Accuracy')
plt.title('Depth vs Accuracy')
plt.legend()
plt.grid(True)
plt.show()
### Conclusion:
# Jaise jaise decision tree ki depth badhti hai, training accuracy increase hoti hai
# lekin test accuracy ek point ke baad gir jati hai.
# Iska matlab model overfit ho jata hai.
# Depth 4 ya 5 ke aas-paas sabse balanced result mil raha hai (~64%).

