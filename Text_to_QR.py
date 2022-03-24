import pyqrcode
import pandas as pd


def createQRCode():


    df = pd.read_csv("myfile0.csv")

    for index, values in df.iterrows():

        Id = values["id"]
        first_name = values["firstname"]
        lastname = values["lastname"]
        email = values["email"]
        profession=values["profession"]

        data = f'''
        id: {id} \n
        firstname: {first_name} \n
        lastname: {lastname} \n
        email: {email} \n
        profession: {profession}
        '''
        image = pyqrcode.create(data)
        image.png(f"{first_name}_{lastname}.png", scale="5")
        print(data)



createQRCode()