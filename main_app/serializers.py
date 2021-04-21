from rest_framework import serializers
from main_app.models import Research, Member, Contact, Publication, People, Faculty

class ResearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Research
        fields = ['heading', 'imagePath', 'desc', 'linkName', 'externalLink']

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['name','designation', 'department', 'college', 'mobile', 'email']

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ['year','heading','linkPath']

class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ['name', 'email', 'description', 'imagePath']

class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name', 'email', 'description', 'imagePath']
