from django.shortcuts import render
from healthprediction.serializers import DiseasePredictSerializer
import json


from healthprediction.seed import get_predicted_value,helper

import pickle
svc = pickle.load(open('model/svc.pkl','rb'))



# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate # import here authenticate
from account.renderers import UserRenderer   # import custome errors

from rest_framework.permissions import IsAuthenticated



class DiseasePredict(APIView):
    renderer_classes = [UserRenderer]   # ab all 'error' word show before error text
    def post(self, request,format=None):
        
        
        serializer = DiseasePredictSerializer(data=request.data)
        
        
        
        model = svc.predict([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        # svc.predict(X_test.iloc[100].values.reshape(1,-1))
        print('\n\n')
        print('testing 1')
        print('prediction :- ',model[0])
        print('\n\n')
        
        
        # print('\n\n')
        # symptoms = 'itching,skin_rash,nodal_skin_eruptions'
        # user_symptoms = [s.strip() for s in symptoms.split(',')]
        # user_symptoms = [symptom.strip("[]' ") for symptom in user_symptoms]
        # predicted_disease = get_predicted_value(user_symptoms)
        # print('\n','predicted_disease :- ',predicted_disease,'\n')
        
        
        
        # desc, pre, med, die, wrkout = helper(predicted_disease)
        
        
        
        # print("=================predicted disease============")
        # print(predicted_disease)
        # print("=================description==================")
        # print(desc)
        # print("=================precautions==================")
        # i = 1
        # for p_i in pre[0]:
        #     print(i, ": ", p_i)
        #     i += 1

        # print("=================medications==================")
        # for m_i in med:
        #     print(i, ": ", m_i)
        #     i += 1

        # print("=================workout==================")
        # for w_i in wrkout:
        #     print(i, ": ", w_i)
        #     i += 1

        # print("=================diets==================")
        # for d_i in die:
        #     print(i, ": ", d_i)
        #     i += 1


        if serializer.is_valid(raise_exception=True):
            print('testing 2 :- ',serializer.data)
            symtoms_name = serializer.data.get('symtoms_name')
            print('symtoms_name is :- ',symtoms_name)
            # print('symtoms_name type is :- ',type(symtoms_name))
            
            # symptoms = 'itching,skin_rash,nodal_skin_eruptions'
            # symptoms = ' skin_rash, high_fever, blister, red_sore_around_nose'
            # symptoms = ' skin_rash,  joint_pain,  skin_peeling,  silver_like_dusting'

            symptoms = f"{symtoms_name}"
            user_symptoms = [s.strip() for s in symptoms.split(',')]
            user_symptoms = [symptom.strip("[]' ") for symptom in user_symptoms]
            predicted_disease = get_predicted_value(user_symptoms)
            print('\n','predicted_disease testing :- ',predicted_disease,'\n')
            desc, pre, med, die, wrkout = helper(predicted_disease)

         
            data = {
                "symtoms_name":symtoms_name,
                "predicted_disease":predicted_disease,
                "predicted_descriptions":desc,
                "predicted_precations":f"{pre[0]}",   
                "predicted_medications":f"{med[0]}",
                "predicted_diets":f"{die[0]}",
                "predicted_workout":f"{wrkout.values}",
                "msg":"Successfully Model Predictions!!"
            }
            
             
            return Response({'Predictions':data},status=status.HTTP_201_CREATED)
        
        print('error testing')
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
