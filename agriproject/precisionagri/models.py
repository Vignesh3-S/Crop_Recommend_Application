from django.db import models
class agriculture(models.Model):
    state_choices = [("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),
                     ("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),
                     ("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),
                     ("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),
                     ("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),
                     ("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),
                     ("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),
                     ("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),
                     ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),
                     ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),
                     ("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry")]
    State_Name = models.CharField(max_length=200,verbose_name="StateName",choices=state_choices)
    District = models.CharField(max_length=300,verbose_name="DistrictName")
    Nitrogen = models.FloatField(verbose_name="Nitrogen")
    Phosphorous = models.FloatField(verbose_name="Phosphorus")
    Potassium = models.FloatField(verbose_name="Potassium")
    Temperature = models.FloatField(verbose_name="Temperature")
    Humidity = models.FloatField(verbose_name="Humidity")
    PH = models.FloatField(verbose_name="PH")
    Rainfall = models.FloatField(verbose_name="Rainfall")
    Crop_Label  = models.CharField(max_length=100,verbose_name="Crop")

    def __str__(self):
        return self.State_Name

class NPK(models.Model):
    Crop_Name  = models.CharField(max_length=50,verbose_name="Crop Name")
    Std_nitrogen = models.CharField(max_length=15,verbose_name="Standard Nitrogen")
    Std_phosphorous = models.CharField(max_length=15,verbose_name="Standard Phosphorus")
    Std_potassium = models.CharField(max_length=15,verbose_name="Standard Potassium")

    def __str__(self):
        return self.Crop_Name
    
