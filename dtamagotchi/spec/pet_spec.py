from nose.tools import *
import pungi
from rest_framework.test import APIClient
from django.conf import settings
import responses
import json
from pet.models import Pet
from django.core.exceptions import PermissionDenied
from datetime import date, timedelta
from django.utils import timezone

with describe('A Pet'):
    with it('should instantiate'):
        ok_(Pet())
    with it('should be able to save'):
        p = Pet(name="Test")
        p.save()
        sut = Pet.objects.get(pk=p.pk)
        eq_(p.name, "Test")
    with describe('when living'):
        with it('should be able to die'):
            p = Pet(name="Test")
            p.alive = False
            ok_(p.alive == False)
        with it('should feel neglected if not fed for 24 hours'):
            p = Pet(name="Test", last_fed=timezone.now() - timedelta(hours=48))
            eq_(p.neglected, True)
        with it('should not feel neglected if fed in the last 24 hours'):
            p = Pet(name="Test", last_fed=timezone.now() - timedelta(hours=12))
            eq_(p.neglected, False)
        with it('should not learn tricks if dumb'):
            p = Pet(name="Test", iq=55)
            eq_(p.learns_tricks, False)
        with it('should do tricks if not dumb'):
            p = Pet(name="Test", iq=90)
            p.save()
            eq_(p.learns_tricks, True)
        with it('should not learn tricks if too damn smart'):
            p = Pet(name="Test", iq=148)
            eq_(p.learns_tricks, False)
    with describe('when dead'):
        with it('should not come back to life'):
            p = Pet(name="Test", alive=False)
            with assert_raises(PermissionDenied):
                p.alive = True
                p.save()
        with it('should not be able to eat'):
            p = Pet(name="Test", alive=False)
            with assert_raises(PermissionDenied):
                p.fedLast = timezone.now()
                p.save()
