from  rest_framework import serializers
from .models import Artical


class Articlr_serlier(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields='__all__'