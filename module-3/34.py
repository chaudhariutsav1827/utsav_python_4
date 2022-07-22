'''
Write a Python script to concatenate following dictionaries to create a 
new one.
'''
cityCode={'Ahmedabad':79, 'Mumbai':22,'Pune':20,'Delhi':11}
cityFamousPlace={"Banglore":"IIM","Nasik":"Metro","Kashmir":"Bollywood"}
print("Before updating the cityCode is ",cityCode)
cityCode.update(cityFamousPlace)
print("updated cityCode ",cityCode)
