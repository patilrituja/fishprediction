import pickle
import json
import config
import numpy as np

class Fish_Market():
    def __init__(self,Length1,Length2,Length3,Height,Width,Species) :
        self.Length1=Length1
        self.Length2=Length2
        self.Length3=Length3
        self.Height=Height
        self.Width=Width
        self.Species=Species

        return

    def __load_model(self):
        with open(r"Artifacts\linear_model.pkl",'rb') as f:
            self.model=pickle.load(f)
            print("load model is :",self.model)

        with open(r'Artifacts\project_data.json','r')as f:
            self.project_data=json.load(f)
            print("project data is :",self.project_data)

        return

    def get_predicted_weight(self):
        self.__load_model()

        test_array=np.zeros((1,self.model.n_features_in_))
        test_array[0][0]=self.Length1
        test_array[0][1]=self.Length2
        test_array[0][2]=self.Length3
        test_array[0][3]=self.Height
        test_array[0][4]=self.Width
        Species='Species_'+ self.Species
        index=self.project_data['Column Names'].index(Species)

        test_array[0][index]=1

        print("test array is :",test_array)
        #scaled_test_array=self.normal_scale.transform(test_array)
        
        predicted_weight=self.model.predict(test_array)[0]

        print("Predicted weight is :",predicted_weight)
        return predicted_weight
