from pydantic import BaseModel, Field


# Input for data validation
class Input(BaseModel):
    SepalLengthCm: float = Field(..., gt=0)
    SepalWidthCm: float = Field(..., gt=0)
    PetalLengthCm: float = Field(..., gt=0)
    PetalWidthCm: float = Field(..., gt=0)

    class Config:
        schema_extra = {
            "SepalLengthCm": 4.9, 
            "SepalWidthCm": 3.0, 
            "PetalLengthCm": 1.4, 
            "PetalWidthCm": 0.2,
        }


# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction: int