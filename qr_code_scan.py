import pyqrcode
import pandas as pd

def qrcode():

	df = pd.read_csv("test.csv")


	for index, Label in df.iterrows():

		Name = Label["Name"]
		#Ticket = Name["Ticket"]
		#Age = Name["Age"]

		data = Label.Name

		"""data = f'''
						
								Name:{name} \n
								Sex: {Sex}\n
								Age:{Age}
								'''"""

		image = pyqrcode.create(data)
		image.save("csv_qr_code.png", scale=7)


print(qrcode())