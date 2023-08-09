from django.db import models

class CommitteeMembers(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name

class Candidates(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    institution_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    profile_image = models.TextField(null=True)
    status_choices = [
        ('active', 'Active'),
        ('suspend', 'Suspend'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="active")

    def __str__(self):
        return self.name

class Judges(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=25, null=True)
    password = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    status_choices = [
        ('active', 'Active'),
        ('suspend', 'Suspend'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="active")

    def __str__(self):
        return self.name

class Programs(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    program_name = models.CharField(max_length=255, null=True)
    details = models.TextField(null=True)
    date = models.CharField(max_length=10, null=True)
    time = models.CharField(max_length=25, null=True)
    venue = models.CharField(max_length=100, null=True)
    committee_member = models.ForeignKey(CommitteeMembers,on_delete=models.SET_NULL,null=True)
    judge = models.ForeignKey(Judges,on_delete=models.SET_NULL,null=True)
    status_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    published = models.CharField(max_length=7, choices=status_choices, default="no")

    def __str__(self):
        return self.program_name

class ProgramsApplied(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    program = models.ForeignKey(Programs,on_delete=models.SET_NULL,null=True)
    candidate = models.ForeignKey(Candidates,on_delete=models.SET_NULL,null=True)
    attended_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    attended = models.CharField(max_length=7, choices=attended_choices, default="no")
    marks = models.FloatField(null=True, blank=True, default=0.0)
    remarks = models.TextField(null=True)
    status_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="no")

    def __str__(self):
        return self.id

class Results(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    program_id = models.IntegerField(null=True)
    candidate_won = models.IntegerField(null=True)
    candidate_grade = models.CharField(max_length=10, null=True)
    judges_participated = models.IntegerField(null=True)
    venue = models.CharField(max_length=100, null=True)
    remarks = models.TextField(null=True, default = '')
    status_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="no")

    def __str__(self):
        return self.id

class Accommodation(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    accommodation_name = models.CharField(max_length=100, null=True)
    accommodation_address = models.TextField(max_length=100, null=True)
    incharge_name = models.CharField(max_length=100, null=True)
    person_to_contact = models.CharField(max_length=100, null=True)
    committee_member = models.IntegerField(null=True)

    def __str__(self):
        return self.accommodation_name

class Accomodated_candidates(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    accommodation_id = models.IntegerField(null=True)
    candidate_id = models.IntegerField(null=True)
    committee_member = models.IntegerField(null=True)

    def __str__(self):
        return self.id

class Institution(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    institution_name = models.CharField(max_length=100, null=True)
    institution_address = models.TextField(max_length=100, null=True)
    incharge_name = models.CharField(max_length=100, null=True)
    person_to_contact = models.CharField(max_length=100, null=True)
    committee_member = models.IntegerField(null=True)

    def __str__(self):
        return self.institution_name

class Contact_message(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

