"""3. Write a python program the Categorical values in numeric format for a
given dataset.
"""
import pandas as pd
info={
    'gender':['male','female','male','female','female','male','male','male','female'],
    'position':['head','asst.prof','asst.prof','associate prof','head','associate prof','asst.prof','asst.prof','associate prof']
}
print(info)

infodf=pd.DataFrame(info)
print(infodf)

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

gender_encoded=le.fit_transform(infodf['gender'])
position_encoder=le.fit_transform(infodf['position'])

infodf['gender_encoded']=gender_encoded
infodf['position_encoder']=position_encoder

print(infodf)

