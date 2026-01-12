from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    cost = models.FloatField()
    stock = models.IntegerField(default=0)

    # เพิ่มส่วนนี้เข้าไปครับ
    @property
    def estimated_profit(self):
        # คำนวณกำไร: (ราคาขาย 490 * 0.83) - ต้นทุน
        return (490 * 0.83) - self.cost

    def __str__(self):
        return self.name


class History(models.Model):
    customer_name = models.CharField(max_length=100, blank=True)
    item_given = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
