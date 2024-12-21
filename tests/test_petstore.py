import pytest
from pages.petstore_page import PetstorePage


class TestPetstore:
    @pytest.fixture(scope="class")
    def petstore(self):
        return PetstorePage()

    def test_create_pet(self, petstore):
        pet_data = {"id": 12345, "name": "Buddy", "status": "available"}
        response = petstore.create_pet(pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Buddy"
        assert response.json()["status"] == "available"

    def test_get_pet(self, petstore):
        pet_id = 12345
        response = petstore.get_pet(pet_id)
        assert response.status_code == 200
        assert response.json()["id"] == pet_id

    def test_not_get_pet(self, petstore):
        pet_id = 124232323345
        response = petstore.get_pet(pet_id)
        assert response.status_code == 404

    def test_find_by_status_positive(self, petstore):
        status = "available"
        response = petstore.find_by_status(status)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert all(pet["status"] == status for pet in response.json())

    def test_find_by_status_negative(self, petstore):
        invalid_status = "unknown_status"
        response = petstore.find_by_status(invalid_status)
        assert response.status_code == 200
        assert response.json() == []

    def test_update_pet(self, petstore):
        pet_data = {"id": 12345, "name": "Max", "status": "sold"}
        response = petstore.update_pet(pet_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Max"
        assert response.json()["status"] == "sold"

    def test_not_update_pet(self, petstore):
        pet_data = {"id": 1234324234234234242445, "name": "Max", "status": "sold"}
        response = petstore.update_pet(pet_data)
        assert response.status_code == 500

    def test_delete_pet(self, petstore):
        pet_id = 12345
        response = petstore.delete_pet(pet_id)
        assert response.status_code == 200

    def test_not_delete_pet(self, petstore):
        pet_id = 1234523123213123213
        response = petstore.delete_pet(pet_id)
        assert response.status_code == 404