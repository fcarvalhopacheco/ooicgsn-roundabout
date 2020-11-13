from django.db import models


# CSV Import configuration model
# class ImportConfig(models.Model):
#     def __str__(self):
#         return self.created_at.strftime("%m/%d/%Y")
#     def get_object_type(self):
#         return 'import_configuration'
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     require_cal_coefficient_values = models.BooleanField(blank=False, default=True)
#     require_cal_notes = models.BooleanField(blank=False, default=False)
#     require_dep_sensor_uid = models.BooleanField(blank=False, default=True)
#     require_cruise_ship_name = models.BooleanField(blank=False, default=True)
#     require_cruise_start_date = models.BooleanField(blank=False, default=True)
#     require_cruise_stop_date = models.BooleanField(blank=False, default=True)
#     require_cruise_notes = models.BooleanField(blank=False, default=True)