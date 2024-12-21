import requests


class PetstorePage:
    BASE_URL = "https://petstore.swagger.io/v2/pet"
    HEADERS = {"Content-Type": "application/json"}

    def create_pet(self, pet_data):
        response = requests.post(self.BASE_URL, json=pet_data, headers=self.HEADERS)
        return response

    def get_pet(self, pet_id):
        response = requests.get(f"{self.BASE_URL}/{pet_id}", headers=self.HEADERS)
        return response

    def find_by_status(self, status):
        response = requests.get(f"{self.BASE_URL}/findByStatus?status={status}", headers=self.HEADERS)
        return response

    def update_pet(self, pet_data):
        response = requests.put(self.BASE_URL, json=pet_data, headers=self.HEADERS)
        return response

    def delete_pet(self, pet_id):
        response = requests.delete(f"{self.BASE_URL}/{pet_id}", headers=self.HEADERS)
        return response
