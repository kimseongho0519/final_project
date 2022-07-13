from django.db import models

# Create your models here.

class tour_data(models.Model):
    year = models.TextField()
    month = models.TextField()
    sigoon = models.CharField(max_length=10)
    sigoon_vcnt = models.BigIntegerField()
    sns_cnt = models.BigIntegerField()
    spend_type = models.CharField(max_length=10)
    spend_amount = models.BigIntegerField()
    depart_from = models.CharField(max_length=10)
    core_area = models.IntegerField()
    male_ratio = models.FloatField()
    age_10s_under = models.FloatField()
    age_20s = models.FloatField()
    age_30s = models.FloatField()
    age_40s = models.FloatField()
    age_50s = models.FloatField()
    age_60s = models.FloatField()
    age_70s_over = models.FloatField()
    do_cnt = models.BigIntegerField()
    rel_crowded = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tour_data' # db이름 정의