from django.db import models

# Create your models here.


class Patient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    prot_level_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class ProtLevelDesc(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prot_level_desc'

class EmergencyContact(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    login = models.ForeignKey('Login', models.DO_NOTHING)
    patient_id1 = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient_id1')

    class Meta:
        managed = False
        db_table = 'emergency_contact'


class Login(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'

class Diseases(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    conclusion = models.CharField(max_length=100, blank=True, null=True)
    patient_disease = models.ForeignKey('PatientDisease', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'diseases'
        unique_together = (('id', 'patient_disease'),)


class PatientDisease(models.Model):
    id = models.BigIntegerField(primary_key=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    disease_id = models.BigIntegerField(blank=True, null=True)
    personal_data = models.ForeignKey('PersonalData', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_disease'


class PatientSensorTransition(models.Model):
    sensors = models.BigIntegerField(blank=True, null=True)
    personal_data = models.OneToOneField('PersonalData', models.DO_NOTHING, primary_key=True)
    sensor = models.ForeignKey('Sensor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_sensor_transition'
        unique_together = (('personal_data', 'sensor'),)


class PersonalData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    disease_id = models.IntegerField(blank=True, null=True)
    emergency_contact_id = models.BigIntegerField(blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'personal_data'


class Sensor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor'

