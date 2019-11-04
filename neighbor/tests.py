from django.test import TestCase
from .models import Neighbourhood, Business

class NeighbourhoodTestClass(TestCase):
       def setUp(self):
          self.neighbourhood=Neighbourhood(id=1,neighbourh_name='Rwanda',neighbourh_location='Kigali',occupants=98776)
          
       def tearDown(self):
           Neighbourhood.objects.all().delete()
          
       def test_create_neighbourhood(self):
           new=Neighbourhood.create_neighbourhood('ok','hey',1234)
           self.assertIsInstance(new,Neighbourhood)

       def test_find_neighbourhood(self):
          self.neighbourhood.save_neighbourhood()
          neighbourhood = Neighbourhood.find_neighbourhood(id=self.neighbourhood.id)
          self.assertEquals(neighbourhood,self.neighbourhood)
