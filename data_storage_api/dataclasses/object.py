import base64
import json

from dataclasses import dataclass


@dataclass
class ObjectDataclass:
    id: str
    data: str
    
    @property
    def decoded_data(self):
        return json.loads(base64.b64decode(self.data).decode())
