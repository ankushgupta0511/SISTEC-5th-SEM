from django.shortcuts import render
from django.http import HttpResponse

from .seed import get_predicted_value,helper

import pickle
svc = pickle.load(open('model/svc.pkl','rb'))



# Create your views here.


def predict(request):
    print('\n\n')
    print('start')
    print('\n\n')
    
    model = svc.predict([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    # svc.predict(X_test.iloc[100].values.reshape(1,-1))
    print('\n\n')
    print('prediction :- ',model[0])
    print('\n\n')
    
    
    print('\n\n')
    symptoms = 'itching,skin_rash,nodal_skin_eruptions'
    user_symptoms = [s.strip() for s in symptoms.split(',')]
    user_symptoms = [symptom.strip("[]' ") for symptom in user_symptoms]
    predicted_disease = get_predicted_value(user_symptoms)
    print('\n','predicted_disease :- ',predicted_disease,'\n')
    
    
    
    desc, pre, med, die, wrkout = helper(predicted_disease)
    
    
    
    print("=================predicted disease============")
    print(predicted_disease)
    print("=================description==================")
    print(desc)
    print("=================precautions==================")
    i = 1
    for p_i in pre[0]:
        print(i, ": ", p_i)
        i += 1

    print("=================medications==================")
    for m_i in med:
        print(i, ": ", m_i)
        i += 1

    print("=================workout==================")
    for w_i in wrkout:
        print(i, ": ", w_i)
        i += 1

    print("=================diets==================")
    for d_i in die:
        print(i, ": ", d_i)
        i += 1

    return HttpResponse('<h1>Well come in health recommendation system</h1>')