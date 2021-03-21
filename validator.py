from pydantic import BaseModel, ValidationError


class Values(BaseModel):
    # model for instance  id: int
   


input_json = """ {

   #input json for instance "id": 1
  }"""


try:
  values = Values.parse_raw(input_json)
except ValidationError as e:
  print(e.json())

values = Values.parse_raw(input_json)
print(values)