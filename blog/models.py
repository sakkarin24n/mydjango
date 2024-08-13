from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # ชื่อของสินค้า
    description = models.TextField(blank=True, null=True)  # คำอธิบายสินค้า
    price = models.DecimalField(max_digits=10, decimal_places=2)  # ราคาสินค้า
    stock = models.IntegerField(default=0)  # จำนวนสินค้าที่มีในสต็อก
    created_at = models.DateTimeField(auto_now_add=True)  # วันที่สร้าง
    updated_at = models.DateTimeField(auto_now=True)  # วันที่แก้ไขล่าสุด





    def __str__(self):
        return self.name  # แสดงชื่อของสินค้าใน Admin และที่อื่นๆ
# Create your models here.
