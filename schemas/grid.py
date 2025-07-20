from pydantic import BaseModel
from typing import List

class BusSchema(BaseModel):
    id: int
    name: str
    vn_kv: float
    type: str
    
class GridImportExport(BaseModel):
    buses: List[BusSchema]
    branches: List[BrancSchema]
    transformers: List[TransformerSchema]