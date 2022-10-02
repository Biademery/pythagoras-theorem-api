from dataclasses import fields
from pydoc import classname
from pyexpat import model
from rest_framework import serializers
from .models import Result

class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'c', 'a', 'b')