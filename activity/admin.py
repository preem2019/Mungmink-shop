from django.contrib import admin
from .models import Item, History


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # กำหนดคอลัมน์ที่จะโชว์ในหน้าลิสต์สินค้า
    list_display = ("name", "cost", "stock", "recommended_sell_price", "profit_status")

    # เพิ่มระบบค้นหาด้วยชื่อสินค้า
    search_fields = ("name",)

    # เพิ่มตัวกรอง (Filter) ด้านข้าง
    list_filter = ("stock",)

    # ฟังก์ชันคำนวณราคาขายแนะนำ (เพื่อให้ได้กำไร 200 บาท หลังหัก 17%)
    def recommended_sell_price(self, obj):
        # สูตร: (Cost + 200) / 0.83
        price = (obj.cost + 200) / 0.83
        return f"{round(price, 2)} ฿"

    recommended_sell_price.short_description = "ราคาขายแนะนำ (กำไร 200฿)"

    # ฟังก์ชันโชว์สถานะสต็อกแบบสี
    def profit_status(self, obj):
        if obj.stock > 0:
            return "✅ พร้อมสุ่ม"
        return "❌ ของหมด"

    profit_status.short_description = "สถานะ"


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "item_given", "created_at")
    list_filter = ("created_at", "item_given")
    search_fields = ("customer_name",)
