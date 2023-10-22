from django.test import Client, TestCase
from people.models import People, Parent
import json

class PersonTestCase(TestCase):
    def setUp(self):
        People.objects.create(name="Ari", date_of_birth = "2011-11-20T00:00:00Z", people_id = 1, city = "Elad")
        People.objects.create(name="Yael", date_of_birth = "2001-11-20T00:00:00Z", people_id = 2, city = "Petach Tikva")
        Parent.objects.create(name="Ari", date_of_birth = "2001-11-20T00:00:00Z", people_id = 3, city = "Petach Tikva", work_place = "army", salary = "50000")
        self.client = Client()

#  test adult people     
    def test_adult(self):
        ari = People.objects.get(people_id = 1)
        yeal= People.objects.get(people_id = 2)
        self.assertEqual(ari.adult_person(), False)
        self.assertEqual(yeal.adult_person(), True)


#  test to add parent
    def test_add_parent(self):
            parent_data = {
                "name": "Ella",
                "people_id": 87676565,
                "date_of_birth": "1990-08-21T08:15:00Z",
                "city": "New York",
                "work_place": "Finance Corp",
                "salary": 75000
            }
            response = self.client.post("/api/people/AddParent/",parent_data, content_type = 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_add_parent_error(self):
            added_parent = {
                "name": "Ella",
                "people_id": 3223,
                "date_of_birth": "1990-08-21T08:15:00Z",
                "city": "New York",
                "work_place": "Finance Corp",
            } # i did'nt fill all the fields to check the error
            response = self.client.post("/api/people/AddParent/", added_parent, content_type = 'application/json')
            self.assertEqual(response.status_code, 400)


#  test to delete parent
    def test_delete_parent(self):
        Parent.objects.get(people_id=3)
        response =self.client.delete("/api/people/DeleteParent/3/")
        self.assertEqual(response.status_code, 200)
    
    def test_delete_parent_error(self):
        with self.assertRaises(Parent.DoesNotExist):
            Parent.objects.get(people_id = 11) # i put id that don't exist to check the error
        response = self.client.delete("/api/people/DeleteParent/11/")
        self.assertEqual(response.status_code, 400) 

        
# test update parent   
    def test_update_parent(self):
        updated_parent = {
                "name": "Avi",
                "people_id": 3,
                "date_of_birth": "1990-08-21T08:15:00Z",
                "city": "Los Angeles",
                "work_place": "Finance Corp",
                "salary": 1000
            }
        response = self.client.put("/api/people/UpdateParent/", updated_parent, content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_parent_error(self):
        updated_parent = {
                "name": "Avi",
                "people_id": 3223,
                "date_of_birth": "1990-08-21T08:15:00Z",
                "city": "Los Angeles",
                "work_place": "Finance Corp",
                "salary": 1000
            } # i did'nt fill all the fields to check the error
        response = self.client.put("/api/people/UpdateParent/", updated_parent, content_type = 'application/json')
        self.assertEqual(response.status_code, 400)


#  test get specific parent 
    def test_get_all_parent(self):
        response = self.client.get("/api/people/AllParent/")
        self.assertEqual(response.status_code, 200)
        to_json =json.loads(response.content)
        # .decode('utf-8'))
        len_of_json = len(to_json)
        self.assertEqual(len_of_json, 1) 
        

#  test get specific parent 
    def test_get_specific_parent(self):
        Parent.objects.get(people_id=3)
        response = self.client.get("/api/people/SpecificParent/3/")
        self.assertEqual(response.status_code, 200)

    def test_get_specific_parent_error(self):
        with self.assertRaises(Parent.DoesNotExist):
            Parent.objects.get(people_id = 11) # i put id that don't exist to check the error
        response = self.client.get("/api/people/SpecificParent/11/")
        self.assertEqual(response.status_code, 400) 
    
# test related parent
    def test_related_parent(self):
        the_related = {
            "parent_id": 3,
            "children_id": 1
        }
        response = self.client.put("/api/people/RelatedParent/", the_related, content_type = 'application/json')
        self.assertEqual(response.status_code, 200) 

    def test_related_parent_error(self):
        the_related = {
            "parent_id": 33,
            "children_id": 22
        } # i put id that don't exist to check the error
        response = self.client.put("/api/people/RelatedParent/", the_related, content_type = 'application/json')
        self.assertEqual(response.status_code, 400) 

# test rich parent 
    def test_rich_parent(self):
        response = self.client.get("/api/people/RichParent/")
        self.assertEqual(response.status_code, 200)
        to_json =json.loads(response.content)
        len_of_json = len(to_json)
        self.assertEqual(len_of_json, 1)
    
# test find parent
    def test_find_parent(self):
        Parent.objects.get(people_id=3)
        response = self.client.get("/api/people/FindParent/3/")
        self.assertEqual(response.status_code, 200)
    
    def test_find_parent(self):
        with self.assertRaises(Parent.DoesNotExist):
            Parent.objects.get(people_id = 11) # i put id that don't exist to check the error
        response = self.client.get("/api/people/FindParent/11/")
        self.assertEqual(response.status_code, 400) 
         

# test find parent
    def test_find_child(self):
        Parent.objects.get(people_id=3)
        response = self.client.get("/api/people/FindChild/3/")
        self.assertEqual(response.status_code, 200)
    
    def test_find_child_error(self):
        with self.assertRaises(Parent.DoesNotExist):
            Parent.objects.get(people_id = 11) # i put id that don't exist to check the error
        response = self.client.get("/api/people/FindChild/11/")
        self.assertEqual(response.status_code, 400) 


# test find grandparents
    def test_find_grand(self):
        Parent.objects.get(people_id=3)
        response = self.client.get("/api/people/FindGrand/3/")
        self.assertEqual(response.status_code, 200)
    
    def test_find_grand_error(self):
        with self.assertRaises(Parent.DoesNotExist):
            Parent.objects.get(people_id = 11)# i put id that don't exist to check the error
        response = self.client.get("/api/people/FindGrand/11/")
        self.assertEqual(response.status_code, 400) 


# test find siblings
    def test_find_siblings(self):
        Parent.objects.get(people_id=3)
        response = self.client.get("/api/people/FindSiblings/3/")
        self.assertEqual(response.status_code, 200)
    
    def test_find_siblings_error(self):
        with self.assertRaises(Parent.DoesNotExist):
            Parent.objects.get(people_id = 11) # i put id that don't exist to check the error
        response = self.client.get("/api/people/FindSiblings/11/")
        self.assertEqual(response.status_code, 400) 

   
    




