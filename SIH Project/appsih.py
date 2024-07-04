

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
science_11 = 0


app = Flask(__name__)

# Load the trained Random Forest model
# with open('final_deploy.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

model = pickle.load(open('final_deploy.pkl' , 'rb'))

@app.route('/')
def home():
    return render_template('animation.html')

@app.route('/predict', methods=['post'])
def predict():
    try:




        # Get input data from the form
        #q1
        data_1 = request.form["intrest_1"]
        if(data_1 == 'i11'):
            
            arts_11 = 2
            commrece_11 = 3
            science_11 = 4
            print(science_11)
        
        elif(data_1 == 'i12'):
            
            arts_11 = 5
            commrece_11 = 3
            science_11 = 2

        elif(data_1 == 'i13'):
            
            arts_11 = 3
            commrece_11 = 2
            science_11 = 5

        elif(data_1 == 'i14'):
            
            arts_11 = 4
            commrece_11 = 4
            science_11 = 4

        elif(data_1 == 'i15'):
            
            arts_11 = 1
            commrece_11 = 1
            science_11 = 1         

#q2
        data_2 = request.form["intrest_2"]
        if(data_2 == 'i21'):
            
            arts_12 = 2
            commrece_12 = 2
            science_12 = 5
            
        
        elif(data_2 == 'i22'):
            
            arts_12 = 5
            commrece_12 = 4
            science_12 = 3

        elif(data_2 == 'i23'):
            
            arts_12 = 5
            commrece_12 = 3
            science_12= 2

        elif(data_1 == 'i24'):
            
            arts_12 = 4
            commrece_12 = 5
            science_12 = 4

        elif(data_2 == 'i25'):
            
            arts_12 = 1
            commrece_12 = 1
            science_12 = 1     
#q3
        data_3 = request.form["intrest_3"]
        if(data_3 == 'i31'):
            
            arts_13 = 4
            commrece_13 = 4
            science_13 = 5
            #print(science_11)
        
        elif(data_3 == 'i32'):
            
            arts_13 = 3
            commrece_13 = 3
            science_13 = 4

        elif(data_3 == 'i33'):
            
            arts_13 = 2
            commrece_13 = 2
            science_13= 3

        elif(data_3 == 'i34'):
            
            arts_13 = 1
            commrece_13 = 1
            science_13 = 2

        elif(data_3 == 'i35'):
            
            arts_13 = 2
            commrece_13 = 2
            science_13 = 3    
#q4 
        data_4 = request.form["intrest_4"]
        if(data_4 == 'i41'):
            
            arts_14 = 4
            commrece_14 = 4
            science_14 = 5
            #print(science_11)
        
        elif(data_4 == 'i42'):
            
            arts_14 = 3
            commrece_14 = 3
            science_14 = 4

        elif(data_4 == 'i43'):
            
            arts_14 = 2
            commrece_14 = 2
            science_14 = 3

        elif(data_4 == 'i44'):
            
            arts_14 = 2
            commrece_14 = 2
            science_14 = 3

        elif(data_4 == 'i45'):
            
            arts_14 = 2
            commrece_14 = 2
            science_14 = 3    
#q5
        data_5 = request.form["intrest_5"]
        if(data_5 == 'i51'):
            
            arts_15 = 4
            commrece_15 = 3
            science_15 = 4
            #print(science_11)
        
        elif(data_5 == 'i52'):
            
            arts_15 = 3
            commrece_15 = 4
            science_15 = 5

        elif(data_5 == 'i53'):
            
            arts_15 = 5
            commrece_15 = 3
            science_15 = 2

        elif(data_5 == 'i54'):
            
            arts_15 = 4
            commrece_15 = 4
            science_15 = 4

        elif(data_5 == 'i55'):
            
            arts_15 = 2
            commrece_15 = 2
            science_15 = 3     

        arts1=arts_11+arts_12+arts_13+arts_14+arts_15
        commrece1=commrece_11+commrece_12+commrece_13+commrece_14+commrece_15
        science1=science_11+science_12+science_13+science_14+science_15
        print(science1)

#q6
        data_6 = request.form["acad_1"]
        if(data_6 == 'a11'):
            
            arts_21 = 2
            commrece_21 = 2
            science_21 = 5
            #print(science_11)
        
        elif(data_6 == 'a12'):
            
            arts_21 = 5
            commrece_21 = 4
            science_21 = 4

        elif(data_6 == 'a13'):
            
            arts_21 = 5
            commrece_21 = 4
            science_21 = 3

        elif(data_6 == 'a14'):
            
            arts_21 = 4
            commrece_21 = 5
            science_21 = 4

        elif(data_6 == 'a15'):
            
            arts_21 = 1
            commrece_21 = 1
            science_21 = 1     

#q7
        data_7 = request.form["acad_2"]
        if(data_7 == 'a21'):
            
            arts_22 = 4
            commrece_22 = 4
            science_22 = 5
            #print(science_11)
        
        elif(data_7 == 'a22'):
            
            arts_22 = 3
            commrece_22 = 3
            science_22 = 4

        elif(data_7 == 'a23'):
            
            arts_22 = 2
            commrece_22 = 2
            science_22 = 3

        elif(data_7 == 'a24'):
            
            arts_22 = 2
            commrece_22 = 2
            science_22 = 3

        elif(data_7 == 'a25'):
            
            arts_22 = 2
            commrece_22 = 2
            science_22 = 3     

#q8

        data_8 = request.form["acad_3"]
        if(data_8 == 'a31'):
            
            arts_23 = 4
            commrece_23 = 4
            science_23 = 5
            #print(science_11)
        
        elif(data_8 == 'a32'):
            
            arts_23 = 3
            commrece_23 = 3
            science_23 = 4

        elif(data_8 == 'a33'):
            
            arts_23 = 2
            commrece_23 = 2
            science_23 = 3

        elif(data_8 == 'a34'):
            
            arts_23 = 3
            commrece_23 = 3
            science_23 = 4

        elif(data_8 == 'a35'):
            
            arts_23 = 2
            commrece_23 = 2
            science_23 = 3     
#q9
        data_9 = request.form["acad_4"]
        if(data_9 == 'a41'):
            
            arts_24 = 3
            commrece_24 = 3
            science_24 = 4
            #print(science_11)
        
        elif(data_9 == 'a42'):
            
            arts_24 = 2
            commrece_24 = 2
            science_24 = 3

        elif(data_9 == 'a43'):
            
            arts_24 = 4
            commrece_24 = 4
            science_24 = 5

        elif(data_9 == 'a44'):
            
            arts_24 = 3
            commrece_24 = 3
            science_24 = 4

        elif(data_9 == 'a45'):
            
            arts_24 = 2
            commrece_24 = 2
            science_24 = 3     
#q10
        data_10 = request.form["acad_5"]
        if(data_10 == 'a51'):
            
            arts_25 = 4
            commrece_25 = 4
            science_25 = 5
            #print(science_11)
        
        elif(data_10 == 'a52'):
            
            arts_25 = 3
            commrece_25 = 3
            science_25 = 4

        elif(data_10 == 'a53'):
            
            arts_25 = 2
            commrece_25 = 2
            science_25 = 3

        elif(data_10 == 'a54'):
            
            arts_25 = 2
            commrece_25 = 2
            science_25 = 3

        elif(data_10 == 'a55'):
            
            arts_25 = 2
            commrece_25 = 2
            science_25 = 3     



        arts2=arts_21+arts_22+arts_23+arts_24+arts_25
        commrece2=commrece_21+commrece_22+commrece_23+commrece_24+commrece_25
        science2=science_21+science_22+science_23+science_24+science_25
        print(science2)

#q11
        data_11 = request.form["pers_1"]
        if(data_11 == 'p11'):
            
            arts_31 = 4
            commrece_31 = 4
            science_31 = 3
            #print(science_11)
        
        elif(data_11 == 'p12'):
            
            arts_31 = 3
            commrece_31 = 3
            science_31 = 4

        elif(data_11 == 'p13'):
            
            arts_31 = 3
            commrece_31 = 3
            science_31 = 4

        elif(data_11 == 'p14'):
            
            arts_31 = 4
            commrece_31 = 4
            science_31 = 3

        elif(data_11 == 'p15'):
            
            arts_31 = 2
            commrece_31 = 2
            science_31 = 3        

#q12
        data_12 = request.form["pers_2"]
        if(data_12 == 'p21'):
            
            arts_32 = 4
            commrece_32 = 4
            science_32 = 3
            #print(science_11)
        
        elif(data_12 == 'p22'):
            
            arts_32 = 3
            commrece_32 = 3
            science_32 = 4

        elif(data_12 == 'p23'):
            
            arts_32 = 4
            commrece_32 = 4
            science_32 = 3

        elif(data_12 == 'p24'):
            
            arts_32 = 3
            commrece_32 = 3
            science_32 = 4

        elif(data_12 == 'p25'):
            
            arts_32 = 2
            commrece_32 = 2
            science_32 = 3     
#q13
        data_13 = request.form["pers_3"]
        if(data_13 == 'p31'):
            
            arts_33 = 3
            commrece_33 = 3
            science_33 = 4
            #print(science_11)
        
        elif(data_13 == 'p32'):
            
            arts_33 = 5
            commrece_33 = 4
            science_33 = 3

        elif(data_13 == 'p33'):
            
            arts_33 = 4
            commrece_33 = 3
            science_33 = 5

        elif(data_13 == 'p34'):
            
            arts_33 = 4
            commrece_33 = 4
            science_33 = 4

        elif(data_13 == 'p35'):
            
            arts_33 = 2
            commrece_33 = 2
            science_33 = 3     
#q14
        data_14 = request.form["pers_4"]
        if(data_14 == 'p41'):
            
            arts_34 = 4
            commrece_34 = 4
            science_34 = 3
            #print(science_11)
        
        elif(data_14 == 'p42'):
            
            arts_34 = 3
            commrece_34 = 3
            science_34 = 4

        elif(data_14 == 'p43'):
            
            arts_34 = 2
            commrece_34 = 2
            science_34 = 3

        elif(data_14 == 'p44'):
            
            arts_34 = 3
            commrece_34 = 3
            science_34 = 4

        elif(data_14 == 'p45'):
            
            arts_34 = 2
            commrece_34 = 2
            science_34 = 3     
#q15
        data_15 = request.form["pers_5"]
        if(data_15 == 'p51'):
            
            arts_35 = 4
            commrece_35 = 4
            science_35 = 3
            #print(science_11)
        
        elif(data_15 == 'p52'):
            
            arts_35 = 3
            commrece_35 = 3
            science_35 = 4

        elif(data_15 == 'p53'):
            
            arts_35 = 4
            commrece_35 = 4
            science_35 = 3

        elif(data_15 == 'p54'):
            
            arts_35 = 2
            commrece_35 = 2
            science_35 = 3

        elif(data_15 == 'p55'):
            
            arts_35 = 2
            commrece_35 = 2
            science_35 = 3


        arts3=arts_31+arts_32+arts_33+arts_34+arts_35
        commrece3=commrece_31+commrece_32+commrece_33+commrece_34+commrece_35
        science3=science_31+science_32+science_33+science_34+science_35
        print(science3)
         
#q16
        data_16 = request.form["car_1"]
        if(data_16 == 'c11'):
            
            arts_41 = 5
            commrece_41 = 2
            science_41 = 1
            #print(science_11)
        
        elif(data_16 == 'c12'):
            
            arts_41 = 2
            commrece_41 = 5
            science_41 = 3

        elif(data_16 == 'c13'):
            
            arts_41 = 1
            commrece_41 = 3
            science_41 = 5

        elif(data_16 == 'c14'):
            
            arts_41 = 4
            commrece_41 = 4
            science_41 = 3

        elif(data_16 == 'c15'):
            
            arts_41 = 2
            commrece_41 = 3
            science_41 = 5     

#q17
        data_17 = request.form["car_2"]
        if(data_17 == 'c21'):
            
            arts_42 = 5
            commrece_42 = 3
            science_42 = 2
            #print(science_11)
        
        elif(data_17 == 'c22'):
            
            arts_42 = 4
            commrece_42 = 3
            science_42 = 3

        elif(data_17 == 'c23'):
            
            arts_42 = 3
            commrece_42 = 3
            science_42 = 3

        elif(data_17 == 'c24'):
            
            arts_42 = 2
            commrece_42 = 2
            science_42 = 3

        elif(data_17 == 'c25'):
            
            arts_42 = 1
            commrece_42 = 1
            science_42 = 2     
  

#q18

        data_18 = request.form["car_3"]
        if(data_18 == 'c31'):
            
            arts_43 = 2
            commrece_43 = 4
            science_43 = 5
            #print(science_11)
        
        elif(data_18 == 'c32'):
            
            arts_43 = 3
            commrece_43 = 3
            science_43 = 4

        elif(data_18 == 'c33'):
            
            arts_43 = 3
            commrece_43 = 3
            science_43 = 3

        elif(data_18 == 'c34'):
            
            arts_43 = 4
            commrece_43 = 2
            science_43 = 2

        elif(data_18 == 'c35'):
            
            arts_43 = 5
            commrece_43 = 1
            science_43 = 1         
#q19
        data_19 = request.form["car_4"]
        if(data_19 == 'c41'):
            
            arts_44 = 2
            commrece_44 = 3
            science_44 = 5
            #print(science_11)
        
        elif(data_19 == 'c42'):
            
            arts_44 = 3
            commrece_44 = 4
            science_44 = 4

        elif(data_19 == 'c43'):
            
            arts_44 = 5
            commrece_44 = 4
            science_44 = 2

        elif(data_19 == 'c44'):
            
            arts_44 = 3
            commrece_44 = 3
            science_44 = 3

        elif(data_19 == 'c45'):
            
            arts_44 = 3
            commrece_44 = 3
            science_44 = 3        
#q20
        data_20 = request.form["car_5"]
        if(data_20 == 'c51'):
            
            arts_45 = 2
            commrece_45 = 5
            science_45 = 3
            #print(science_11)
        
        elif(data_20 == 'c52'):
            
            arts_45 = 3
            commrece_45 = 4
            science_45 = 4

        elif(data_20 == 'c53'):
            
            arts_45 = 3
            commrece_45 = 3
            science_45 = 3

        elif(data_20 == 'c54'):
            
            arts_45 = 4
            commrece_45 = 3
            science_45 = 2

        elif(data_20 == 'c55'):
            
            arts_45 = 5
            commrece_45 = 2
            science_45 = 1   


        arts4=arts_41+arts_42+arts_44+arts_44+arts_45
        commrece4=commrece_41+commrece_42+commrece_44+commrece_44+commrece_45
        science4=science_41+science_42+science_44+science_44+science_45
        print(science4)
         

#q21
        #q21
        data_21 = request.form["ss_1"]
        print(data_21)
        if(data_21 == 'ss11'):
            
            arts_51 = 5
            commrece_51 = 4
            science_51 = 4
            print("hack")
        
        elif(data_21 == 'ss12'):
            
            arts_51 = 4
            commrece_51 =4
            science_51 = 3
            print("hack")

        elif(data_21 == 'ss13'):
            
            arts_51 = 3
            commrece_51 = 3
            science_51 = 3
            print("hack")

        elif(data_21 == 'ss14'):
            
            arts_51 = 2
            commrece_51 = 2
            science_51 = 2
            print("hack")

        elif(data_21 == 'ss15'):
            
            arts_51 = 1
            commrece_51 = 1
            science_51 = 1   
            print("hack")      

#q22
        data_22 = request.form["ss_2"]
        print(data_22)
        if(data_22 == 'ss21'):
            
            arts_52 = 3
            commrece_52 = 4
            science_52 = 4
            print("hack")
            #ssrint(science_21)
        
        elif(data_22 == 'ss22'):
            
            arts_52 = 4
            commrece_52 = 4
            science_52 = 3
            print("hack")

        elif(data_22 == 'ss23'):
            
            arts_52 = 3
            commrece_52 = 3
            science_52 = 3
            print("hack")

        elif(data_22 == 'ss24'):
            
            arts_52 = 2
            commrece_52 = 2
            science_52 = 2
            print("hack")

        elif(data_22 == 'ss25'):
            
            arts_52 = 1
            commrece_52 = 1
            science_52 = 1 
            print("hack")    
#q23
        data_23 = request.form["ss_3"]
        print(data_23)
        if(data_23 == 'ss31'):
            
            arts_53 = 4
            commrece_53 = 4
            science_53 = 2
            print("hack")
            #ssrint(science_21)
        
        elif(data_23 == 'ss32'):
            
            arts_53 = 3
            commrece_53 = 3
            science_53 = 3
            print("hack")

        elif(data_23 == 'ss33'):
            
            arts_53 = 4
            commrece_53 = 4
            science_53 = 3
            print("hack")

        elif(data_23 == 'ss34'):
            
            arts_53 = 3
            commrece_53 = 3
            science_53 = 3
            print("hack")

        elif(data_23 == 'ss35'):
            
            arts_53 = 2
            commrece_53 = 2
            science_53 = 2 
            print("hack")   
#q24
        data_24 = request.form["ss_4"]
        print(data_24)
        if(data_24 == 'ss41'):
            
            arts_54 = 2
            commrece_54 = 4
            science_54 = 4
            print("hack")
            #ssrint(science_21)
        
        elif(data_24 == 'ss42'):
            
            arts_54 = 3
            commrece_54 = 4
            science_54 = 3
            print("hack")

        elif(data_24 == 'ss43'):
            
            arts_54 = 3
            commrece_54 = 3
            science_54 = 3
            print("hack")

        elif(data_24 == 'ss44'):
            
            arts_54 = 4
            commrece_54 = 2
            science_54 = 2
            print("hack")

        elif(data_24 == 'ss45'):
            
            arts_54 = 5
            commrece_54 = 1
            science_54 = 1
            print("hack")    
#q25
        data_25 = request.form["ss_5"]
        print(data_25)
        if(data_25 == 'ss51'):
            
            arts_55 = 5
            commrece_55 = 4
            science_55 = 3
            print("hack")
            #ssrint(science_21)
        
        elif(data_25 == 'ss52'):
            
            arts_55 = 4
            commrece_55 = 4
            science_55 = 3
            print("hack")

        elif(data_25 == 'ss53'):
            
            arts_55 = 3
            commrece_55 = 3
            science_55 = 3
            print("hack")

        elif(data_25 == 'ss54'):
            
            arts_55 = 2
            commrece_55 = 2
            science_55 = 2
            print("hack")

        elif(data_25 == 'ss55'):
            
            arts_55 = 1
            commrece_55 = 1
            science_55 = 1
            print("hack")

        arts5 = arts_51+arts_52+arts_53+arts_54+arts_55
        commrece5= commrece_51 + commrece_52 + commrece_53 + commrece_54 + commrece_55
        science5 = science_51 + science_52 + science_53 + science_54 + science_55
        print(arts5)
        print(science5)

#q26
        data_26 = request.form["ip_1"]
        if(data_26 == 'ip11'):
            
            arts_61 = 5
            commrece_61 = 4
            science_61 = 3
            #print(science_11)
        
        elif(data_26 == 'ip12'):
            
            arts_61 = 2
            commrece_61 = 5
            science_61 = 3

        elif(data_26 == 'ip13'):
            
            arts_61 = 3
            commrece_61 = 3
            science_61 = 5

        elif(data_26 == 'ip14'):
            
            arts_61 = 4
            commrece_61 = 4
            science_61 = 4

        elif(data_26 == 'ip15'):
            
            arts_61 = 5
            commrece_61 = 3
            science_61 = 2     

#q27
        data_27 = request.form["ip_2"]
        if(data_27 == 'ip21'):
            
            arts_62 = 5
            commrece_62 = 3
            science_62 = 2
            #print(science_11)
        
        elif(data_27 == 'ip22'):
            
            arts_62 = 3
            commrece_62 = 5
            science_62 = 3

        elif(data_27 == 'ip23'):
            
            arts_62 = 2
            commrece_62 = 2
            science_62 = 5

        elif(data_27 == 'ip24'):
            
            arts_62 = 4
            commrece_62 = 4
            science_62 = 3

        elif(data_27 == 'ip25'):
            
            arts_62 = 2
            commrece_62 = 3
            science_62 = 5    
  

#q28

        data_28 = request.form["ip_3"]
        if(data_28 == 'ip31'):
            
            arts_63 = 4
            commrece_63 = 4
            science_63 = 5
            #print(science_11)
        
        elif(data_28 == 'ip32'):
            
            arts_63 = 3
            commrece_63 = 3
            science_63 = 4

        elif(data_28 == 'ip33'):
            
            arts_63 = 2
            commrece_63 = 2
            science_63 = 3

        elif(data_28 == 'ip34'):
            
            arts_63 = 1
            commrece_63 = 1
            science_63 = 2

        elif(data_28 == 'ip35'):
            
            arts_63 = 2
            commrece_63 = 2
            science_63 = 3       
#q29
        data_29 = request.form["ip_4"]
        if(data_29 == 'ip41'):
            
            arts_64 = 4
            commrece_64 = 4
            science_64 = 5
            #print(science_11)
        
        elif(data_29 == 'ip42'):
            
            arts_64 = 3
            commrece_64 = 3
            science_64 = 4

        elif(data_29 == 'ip43'):
            
            arts_64 = 2
            commrece_64 = 2
            science_64 = 3

        elif(data_29 == 'ip44'):
            
            arts_64 = 2
            commrece_64 = 2
            science_64 = 3

        elif(data_29 == 'ip45'):
            
            arts_64 = 2
            commrece_64 = 2
            science_64 = 3         
#q30
        data_30 = request.form["ip_5"]
        if(data_30 == 'ip51'):
            
            arts_65 = 5
            commrece_65 = 3
            science_65 = 2
            #print(science_11)
        
        elif(data_30 == 'ip52'):
            
            arts_65 = 2
            commrece_65 = 5
            science_65 = 3

        elif(data_30 == 'ip53'):
            
            arts_65 = 2
            commrece_65 = 3
            science_65 = 5

        elif(data_30 == 'ip54'):
            
            arts_65 = 4
            commrece_65 = 4
            science_65 = 4

        elif(data_30 == 'ip55'):
            
            arts_65 = 3
            commrece_65 = 3
            science_65 = 3  


        arts6=arts_61+arts_62+arts_63+arts_64+arts_65
        commrece6=commrece_61+commrece_62+commrece_63+commrece_64+commrece_65
        science6=science_61+science_62+science_63+science_64+science_65
        print(science6)







        # Add more features as needed

        # Make predictions using the model
        #arr = np.array([1,2,3,4,5,6,7,9,0,1,1,2,4,5,7,8,89,1])


        user_choices = pd.DataFrame({
            'Choice1Weight': [arts1],
            'Choice2Weight': [commrece1],
            'Choice3Weight': [science1],
            'Choice4Weight': [arts2],
            'Choice5Weight': [commrece2],
            'Choice6Weight': [science2],
            'Choice7Weight': [arts3],
            'Choice8Weight': [commrece3],
            'Choice9Weight': [science3],
            'Choice10Weight': [arts4],
            'Choice11Weight': [commrece4],
            'Choice12Weight': [science4],
            'Choice13Weight': [arts5],
            'Choice14Weight': [commrece5],
            'Choice15Weight': [science5],
            'Choice16Weight': [arts6],
            'Choice17Weight': [commrece6],
            'Choice18Weight': [science6],

        })
        print("data to be entered")
    
        predicted_career = model.predict(user_choices)
        #label_encoder = LabelEncoder()
        #predicted_career = label_encoder.inverse_transform([predicted_career])
        print("data entered into model")
        print("Shape of arr:", user_choices.shape)
        #print("Data type of arr:", user_choices.dtype)  
        print((predicted_career))

        if(int(predicted_career) == 1):
            return render_template('arts.html', data=predicted_career)
        elif(int(predicted_career) == 9):
            return render_template('commrece.html', data=predicted_career)
        else:
            return render_template('science.html', data=predicted_career)




        #prediction = int(model.predict(arr))
        #label_encoder = LabelEncoder()
        #predicted_career = label_encoder.inverse_transform([prediction])
        #prediction_str = str(prediction)
        
        #print("hello" )

        # Return the prediction to the webpage
        #return render_template('output.html', data=predicted_career)
    except Exception as e:
        print("hello")
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)



