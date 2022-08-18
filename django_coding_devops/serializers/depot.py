from rest_framework import serializers

from django_coding_devops.models import BaseDepot


class BaseDepotSerializer(serializers.ModelSerializer):
    https_url = serializers.HyperlinkedIdentityField()
    ssh_url = serializers.HyperlinkedIdentityField()
    web_url = serializers.HyperlinkedIdentityField()

    class Meta:
        model = BaseDepot
