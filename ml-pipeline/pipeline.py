import streamlit as st
import numpy as np
import pickle
from PTL import Image


# prediction Function
## prediction system

def pred(Day_of_week,	Age_band_of_driver,	Sex_of_driver,	Educational_level	,Vehicle_driver_relation,	Driving_experience,	Type_of_vehicle,	Owner_of_vehicle,	Service_year_of_vehicle	,Defect_of_vehicle, Area_accident_occured,Lanes_or_Medians , Road_allignment, Types_of_Junction,Road_surface_type,Road_surface_conditions,Light_conditions,
Weather_conditions,Type_of_collision,Number_of_vehicles_involved,Number_of_casualties,Vehicle_movement,Casualty_class,	Sex_of_casualty,	Age_band_of_casualty,	Casualty_severity,	Work_of_casuality,	Fitness_of_casuality,	Pedestrian_movement	,Cause_of_accident,Hours_of_Day):

   ## your prediction code is here
   features = np.array([[Day_of_week,	Age_band_of_driver,	Sex_of_driver,	Educational_level	,Vehicle_driver_relation,	Driving_experience,	Type_of_vehicle,	Owner_of_vehicle,	Service_year_of_vehicle	,Defect_of_vehicle, Area_accident_occured,Lanes_or_Medians , Road_allignment,Weather_conditions,Type_of_collision,Number_of_vehicles_involved,Number_of_casualties,Vehicle_movement,Casualty_class,	Sex_of_casualty,	Age_band_of_casualty,	Casualty_severity,	Work_of_casuality,	Fitness_of_casuality,	Pedestrian_movement	,Cause_of_accident,Hours_of_Day,Types_of_Junction,Road_surface_type,Road_surface_conditions,Light_conditions]])


   result = pipe.predict(features)
   return result



## Create streamlit app
# load pipe and image
pipe = pickle.load(open('10 pipe.pkl','rb'))
img = Image.open('10 pipe img.png')


# Create app
## in terminal type --> streamlit run pipeline.py
st.title("Accident Prediction with pipeline ")
## display image
st.image(img, use_colmn_width= True)

## Sidebar for user input
with st.sidebar:
   st.write('### User Input here....')
   Day_of_week = st.selectbox('Day of week',['Sun','Mon','Tue','Wed','Thur','Fri','Sat'])
   age_band_of_driver = st.selectbox('Age band of Driver',['17-20','21-25','26-30','31-35','36-40','41-45','46-50','51-55','56-60','61-65','66-70','71-75','Over 75'])
   sex_of_driver = st.selectbox('Sex of Driver',['Male','Female','Other'])
   educational_level = st.selectbox('Educational Level',['Above high School','Junior high school','Elementry school','college','univeresty'])
   Number_of_casualties = st.number_input('Number of Casualities',min_value=1,max_value=10,step=1,value=1)


   if st.sidebar.button("predict"):
      prdicted_class = pred(Day_of_week=Day_of_week ,
                            Age_band_of_driver=age_band_of_driver,
                            Sex_of_driver=sex_of_driver,
                            Educational_level=educational_level,
                            Number_of_casualties=Number_of_casualties
                            pipe =pipe )

## predection result
if prdicted_class[0] == 2:
   print("Slight Injury....")
elif prdicted_class[0] == 1:
   print('Serious Injury...')
else:
   print("Fatal Injury....")
