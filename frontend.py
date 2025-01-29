import streamlit as st
import pickle
import re
from PIL import Image
from streamlit_js_eval import streamlit_js_eval


st.set_page_config(page_title='Airline Passenger',layout='wide',initial_sidebar_state="collapsed")

    
with st.container():

    col1,col2,col3 = st.columns([1,3,1])
    with col2:
        st.title('Airline Passenger Satisfaction Prediction')

    col4, col5, col6 = st.columns([1,10,1])
    with col5:
        image = Image.open('Images/homepage.jpg')
        st.image(image)
    st.write('----')




with st.container():

    col7, col8 ,col8_1= st.columns(3,gap='large')
    with col7:
        gender = st.radio('Select your gender :', ('Male', 'Female'),horizontal=True,index=None)
    
        if gender == 'Male':
            gender = 1
        elif gender == 'Female':
            gender = 0   
        
   
    with col8:
        customer = st.radio('Customer Type :',('Loyal Customer','disloyal Customer'),horizontal=True,index=None)

        if customer == 'Loyal Customer':
            customer = 0
        elif customer == 'disloyal Customer':
            customer = 1    
   

    with col8_1:
        age = st.text_input('Age :',placeholder='Type your age here..')
         

    col10_1,col10_2 = st.columns(2,gap='large')
    with col10_1:
        type_of_travel = st.radio('Type of Travel :',('Business travel','Personal Travel'),horizontal=True,index=None)

        if type_of_travel == 'Business travel':
            type_of_travel = 0
        elif type_of_travel == 'Personal Travel':
            type_of_travel = 1   

    with col10_2:
        class_type = st.radio('Class :',('Business','Eco','Eco Plus'),horizontal=True,index=None)

        if class_type == 'Business':
            class_type = 0
        elif class_type == 'Eco':
            class_type = 1
        elif class_type == 'Eco Plus':
            class_type = 2  


    col10, col11 = st.columns(2,gap='large')
    with col10:
        flight_distance = st.radio('Flight Distance :',('Short (upto 500km)','Medium (501-2000km)','Long (Above 2000kms)'),horizontal=True,index=None)

        if flight_distance == 'Short (upto 500km)':
            flight_distance = 2
        elif flight_distance == 'Medium (501-2000km)':
            flight_distance = 1
        elif flight_distance == 'Long (Above 2000kms)':
            flight_distance = 0
        # flight_distance = st.text_input('Flight Distance :',placeholder='Type the distance in Km here..')
    with col11:
        # depature_delay = st.text_input('Departure Delay in Minutes :',placeholder='Type delay time here..')
        depature_delay = st.radio('Departure Delay :',('No','Minor (1-15 mins)','Moderate (16-60 mins)','Significant (1-2 hrs)','Major (Above 2 hrs)'),horizontal=True,index=None)
        
        if depature_delay == 'No':
            depature_delay = 3
        elif depature_delay == 'Minor (1-15 mins)':
            depature_delay = 1
        elif depature_delay == 'Moderate (16-60 mins)':
            depature_delay = 2 
        elif depature_delay == 'Significant (1-2 hrs)':
            depature_delay = 4
        elif depature_delay == 'Major (Above 2 hrs)':    
            depature_delay = 0
    st.write(" ")


    col12, col13 = st.columns(2,gap='large')
    with col12:
        wifi = st.select_slider('Infligt WiFi Service :',(0,1,2,3,4,5))
        online_booking = st.select_slider('Ease of Online booking :',(0,1,2,3,4,5))
        food_drink = st.select_slider('Food and drink :',(0,1,2,3,4,5))
        seat_comfort = st.select_slider('Seat comfort :',(0,1,2,3,4,5))
        service = st.select_slider('On-board service :',(0,1,2,3,4,5))
        baggage = st.select_slider('Baggage handling :',(1,2,3,4,5))
        inflight_service = st.select_slider('Inflight service :',(0,1,2,3,4,5))

    with col13:
        D_A_time = st.select_slider('Departure/Arrival time convenient :',(0,1,2,3,4,5))
        gate_location = st.select_slider('Gate location :',(0,1,2,3,4,5))
        boarding = st.select_slider('Online boarding :',(0,1,2,3,4,5))
        entertainment = st.select_slider('Inflight entertainment :',(0,1,2,3,4,5))
        leg_room = st.select_slider('Leg room service :',(0,1,2,3,4,5))
        check_in = st.select_slider('Checkin service :',(0,1,2,3,4,5))
        cleanliness = st.select_slider('Cleanliness :',(0,1,2,3,4,5))
    
    st.write(" ")
    button_col1, button_col2, button_col3 = st.columns([3,3,3])
    with button_col2:
        pred = st.button('Predict',use_container_width=True,type='primary')
    
    
    
    features = [gender,customer,age,type_of_travel,class_type,flight_distance,wifi,D_A_time,online_booking,
                gate_location,food_drink,boarding,seat_comfort,entertainment,service,leg_room,baggage,check_in,
                inflight_service,cleanliness,depature_delay]
    
    Model = pickle.load(open('Best_Model_Scaler/best_model.sav','rb'))
    Scaler = pickle.load(open('Best_Model_Scaler/MinMax_scaler.sav','rb'))

    rule1 = "(?:1[0-9]|[2-9][0-9]|10[0-5])$"

    match1 = re.fullmatch(rule1,age)

    if pred:
        if gender == None:
            st.error("Please select your gender.")

        elif type_of_travel == None:
            st.error("Please select your type of travel.")

        elif customer == None:
            st.error("Please select your customer type.")

        elif class_type == None:
            st.error("Please select your class.")

        elif age == '':
            st.error('Please enter your age.')  
        elif  not match1:
            st.error('Incorrect age. (Age must be in range 10 to 105) ')

        elif flight_distance == None:
            st.error("Please select your flight distance.")   

        elif depature_delay == None:
            st.error("Please select your depature delay.")   
              
        else:      
            prediction = Model.predict(Scaler.transform([features]))

            st.write(' ')
            st.write('---')
            st.write(' ')
            
            
            if prediction == 0:
                # st.switch_page('pages/result_sat.py')
                st.error('The passenger may be neutral or dissatisfied.')
                res_col1, res_col2, res_col3 = st.columns([2,3,2])
                with res_col2:  
                    img = Image.open('Images/dissatisfied2.png') 
                    st.image(img)
                

            elif prediction == 1:
                # st.switch_page('pages/result_dis.py')
                st.success('The passenger is satisfied.')
                res_col1, res_col2, res_col3 = st.columns([2,3,2])
                with res_col2:
                    img = Image.open('Images/satisfied1.png')
                    st.image(img)

    if st.button("Reload page"):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")               

