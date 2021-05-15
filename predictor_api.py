from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')


data = pd.read_csv("accidents_2005_to_2007.csv", low_memory=False)
dataloc = data.drop(['Road_Type','Speed_limit','Light_Conditions','Weather_Conditions','Day_of_Week','Police_Force', 'Accident_Index', 'Location_Easting_OSGR', 'Location_Northing_OSGR', 'Local_Authority_(District)', 'Local_Authority_(Highway)', '1st_Road_Class', '1st_Road_Number', 'Date', 'LSOA_of_Accident_Location', 'Year', 'Urban_or_Rural_Area', '2nd_Road_Class',
                  '2nd_Road_Number', 'Junction_Detail', 'Junction_Control', 'Did_Police_Officer_Attend_Scene_of_Accident', 'Pedestrian_Crossing-Physical_Facilities', 'Pedestrian_Crossing-Human_Control', 'Number_of_Vehicles', 'Number_of_Casualties', 'Special_Conditions_at_Site', 'Carriageway_Hazards', 'Road_Surface_Conditions'], axis=1)
dataloc = dataloc.dropna(subset=['Longitude', 'Latitude'])
data = data.drop(['Police_Force', 'Accident_Index', 'Location_Easting_OSGR', 'Location_Northing_OSGR', 'Local_Authority_(District)', 'Local_Authority_(Highway)', 'Longitude', 'Latitude', '1st_Road_Class', '1st_Road_Number', 'Date', 'LSOA_of_Accident_Location', 'Year', 'Urban_or_Rural_Area', '2nd_Road_Class',
                  '2nd_Road_Number', 'Junction_Detail', 'Junction_Control', 'Did_Police_Officer_Attend_Scene_of_Accident', 'Pedestrian_Crossing-Physical_Facilities', 'Pedestrian_Crossing-Human_Control', 'Number_of_Vehicles', 'Number_of_Casualties', 'Special_Conditions_at_Site', 'Carriageway_Hazards', 'Road_Surface_Conditions'], axis=1)
data = data.dropna(subset=['Weather_Conditions', 'Time'])
vis = data['Time'].str[:2]
data['Time'] = vis
vis2 = dataloc['Time'].str[:2]
dataloc['Time'] = vis2


def labelEncoder(data):
    encoder = LabelEncoder()
    beta = pd.DataFrame()
    data2 = data.copy()
    length = data2.shape[1]
    col = data2.columns
    for i in range(length):
        a = encoder.fit_transform(data2.iloc[:, i:i+1])
        # b = encoder.fit(data2.iloc[:,i:i+1])
        a = pd.DataFrame(a, columns=[col[i]])
        if i == 0:
            beta = a
        else:
            beta = beta.join(a)
    return beta


model = RandomForestClassifier(n_estimators=4)


def randomForest(data):
    data = labelEncoder(data)
    X = data.drop('Accident_Severity', axis=1)
    y = data['Accident_Severity']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=45)
    model.fit(X_train, y_train)
#     predictions = model.predict(X_test)
#     print(accuracy_score(y_test, predictions))
#     print(confusion_matrix(y_test, predictions))
#     print(classification_report(y_test, predictions))
#     return predictions


def make_prediction(input):
    randomForest(data)
    labelEncoder(data)
    return str(model.predict(input)).strip('[]')


def visualHari(hari):
    df2 = data[(data['Day_of_Week'] == hari)]
    return df2["Accident_Severity"].value_counts().to_json()

def visualCategory(userInput):
    return data[userInput].value_counts().sort_index().to_json()
# test = [[4, 22, 3, 6, 0, 3]]
# make_prediction(test)
def visualOneCategory (category, condition):
    df2 = data[(data[category] == condition)]
    return df2["Accident_Severity"].value_counts().to_json()

def visualTwoCategory (catOne, condOne, catTwo, condTwo):
    df2 = data[(data[catOne] == condOne) & (data[catTwo] == condTwo)]
    return df2["Accident_Severity"].value_counts().to_json()

def mapVisualization (time):
    df2 = dataloc[dataloc['Time']==time]
    return df2.head(30).to_json(orient='records')