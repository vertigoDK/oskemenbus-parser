from app.services.api_parser import ApiParser
import json

api_parser = ApiParser()

print(json.dumps(api_parser.get_schedule("17409"), indent=4, ensure_ascii=False))