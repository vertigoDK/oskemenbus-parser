import requests
import base64
import json
from typing import Dict, Any, List

class Tools:

    @staticmethod
    def decode_base64(data: str) -> str:
        return base64.b64decode(data).decode('utf-8')

class ApiParser:
    def __init__(self) -> None:
        self._base_url = "https://oskemenbus.kz/api/"
        self.default_boundary_circle: Dict[str, Any] = {"Latitude": 49.956492, "Longitude": 82.610013, "Radius": 30}

    def search(self, query: str) -> Dict[str, Any]:
        url = f"{self._base_url}Search"
        params: Dict[str, Any] = {
            "Text": query,
            "BoundaryCircle": self.default_boundary_circle,
            "AdditionalParams": "layers=venue,address&lang=ru"
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.post(url, json=params, headers=headers)
        if response.status_code == 204:
            return {"error": "No Content: HTTP status code 204; transport: missing content-type field", "code": 2}
        return response.json()
        
    def get_schedule(self, stop_id: str) -> Dict[str, Any]:
        """
        Gets the bus schedule for a specific stop.
        
        Args:
            stop_id: The ID of the bus stop
            
        Returns:
            Formatted dictionary with route information and arrival times
        """
        url = f"{self._base_url}GetScoreboard"
        params: Dict[str, Any] = {
            "StopId": stop_id,
            "Types": None
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.post(url, json=params, headers=headers)
        
        # Handle the unusual response format (multiple JSON objects without array)
        results = []
        if response.status_code == 200:
            text = response.text
            # Split by "{"result" to find each JSON object
            parts = text.split('{"result"')
            
            for part in parts:
                if part.strip():
                    # Reconstruct the JSON object
                    json_str = '{"result"' + part if not part.startswith(':') else '{"result"' + part
                    try:
                        results.append(json.loads(json_str))
                    except json.JSONDecodeError:
                        continue
        
        # Format the response according to requirements
        routes = []
        for item in results:
            if 'result' in item:
                result = item['result']
                route = {
                    "number": result.get("Number", ""),
                    "end_stop": result.get("EndStop", ""),
                    "arrival_times": []
                }
                
                info_m = result.get("InfoM", [])
                for time in info_m:
                    if time is not None:
                        if time < 0:
                            route["arrival_times"].append("на остановке")
                        else:
                            route["arrival_times"].append(f"через {time} минуты")
                
                routes.append(route)
        
        return {
            "stop_id": stop_id,
            "routes": routes
        }