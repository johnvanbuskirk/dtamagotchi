from nose.tools import *
import pungi
from rest_framework.test import APIClient
from django.conf import settings
import responses
import json
from pet.models import Pet
from django.core.exceptions import PermissionDenied


with describe('A Pet'):
     with it ('should instantiate'):
          ok_(Pet())
     with it ('should be able to save'):
          p = Pet(name="Test")
          p.save()
          sut = Pet.objects.get(pk=p.pk)
          eq_(p.name, "Test")
     with describe('when living'):
          with it ('should be able to die'):
               p = Pet(name="Test")
               p.alive = False
               ok_(p.alive == False)
     with describe('when dead'):
          with it('should not come back to life'):
               p = Pet(name="Test", alive=False)
               with assert_raises(PermissionDenied):
                    p.alive = True
                    p.save()
