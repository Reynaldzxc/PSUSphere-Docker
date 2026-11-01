
from django.forms import ModelForm
from .models import Organization, OrgMember, Student, College, Program


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"


class OrgMemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = ['student', 'organization', 'date_joined']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'lastname',
            'firstname',
            'middlename',
            'program'
        ]

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = ['college_name']

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['prog_name', 'college']