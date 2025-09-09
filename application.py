from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Optional, Literal
import pandas as pd
import pickle
from fastapi.responses import JSONResponse


app = FastAPI()

# Load the pre-trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

class UserInput(BaseModel):
    age: int = Field(..., example=45, description="Age of the person")
    weight: float = Field(..., example=70.5, description="Weight in kg")
    height: float = Field(..., example=175.0, description="Height in cm")
    income_lpa: float = Field(..., example=5.5, description="Income in LPA")
    smoker: bool = Field(..., example=False, description="Is the person a smoker?")
    city: str = Field(..., example="New York", description="City of residence")
    occupation: str = Field(..., example="Engineer", description="Occupation of the person")
    
    @computed_field
    @property
    # Feature 1: BMI
    def bmi(self) -> float:
        bmi = self.weight / (self.height** 2)
        return bmi
    
    @computed_field
    @property
    # Feature 2: Age Group
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    # Feature 3: Lifestyle Risk
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    # Feature 4: City Tier
    
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

@app.post("/predict")
def predict_insurance_premium(data: UserInput):
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])
     
    prediction = model.predict(input_df)[0]
    return JSONResponse(content={"predicted_premium": prediction}, status_code=200)
