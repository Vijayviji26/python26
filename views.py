from django.shortcuts import render

# Create your views here.
 

def rice(request):
    if(request.method=="POST"):
        data=request.POST
        area=data.get('textarea')
        majoraxislength=data.get('textmajoraxislength')
        minoraxislength=data.get('textminoraxislength')
        eccentricity=data.get('texteccentricity')
        convexarea=data.get('textconvexarea')
        equivdiameter=data.get('textequivdiameter')
        extent=data.get('textextent')
        perimeter=data.get('textperimeter')
        roundness=data.get('textroundness')
        aspectration=data.get('textaspectration')
        if('buttonpredict' in request.POST):
            import pandas as pd
            path="C:/Users/91808/OneDrive/Desktop/New folder (3)/riceClassification.csv"
            data=pd.read_csv(path)
            

            inputs=data.drop(['id','Class'],axis=1)
            output=data['Class']
            

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            

            import sklearn
            from sklearn.ensemble import RandomForestClassifier
            model=RandomForestClassifier(n_estimators=50)
            model.fit(x_train,y_train)

            y_pred=model.predict(x_test)

            result=model.predict([[int(area),float(majoraxislength),float(minoraxislength),float(eccentricity),int(convexarea),float(equivdiameter),float(extent),float(perimeter),float(roundness),float(aspectration)]])
            return render(request,'rice.html',context={'result':result})
    return render(request,'rice.html')
            
