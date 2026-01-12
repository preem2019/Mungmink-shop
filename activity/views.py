from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Item, History
import random


def home(request):
    # ดึงสินค้าที่มีในสต็อก
    items = Item.objects.filter(stock__gt=0)
    selected_item = None

    if request.method == "POST":
        # รับค่าราคาขายจากหน้าเว็บ (เช่น 490 บาท)
        sell_price = float(request.POST.get("sell_price", 0))

        # กรองสินค้าที่ให้กำไรอย่างน้อย 200 หลังหัก 17%
        # สูตร: (Sell * 0.83) - Cost >= 200
        possible_items = [i for i in items if (sell_price * 0.83) - i.cost >= 200]

        if possible_items:
            selected_item = random.choice(possible_items)
            # ลดสต็อก (Optional)
            # selected_item.stock -= 1
            # selected_item.save()

            # บันทึกประวัติ
            History.objects.create(item_given=selected_item)

    return render(request, "activity/index.html", {"item": selected_item})


def dashboard(request):
    # สถิติภาพรวม
    total_items = Item.objects.count()
    low_stock = Item.objects.filter(stock__lte=3).count()  # ของที่เหลือ <= 3 ชิ้น
    total_history = History.objects.count()

    # ดึงรายการสินค้าทั้งหมด
    items = Item.objects.all().order_by("-stock")  # ต้องเป็น order_by
    context = {
        "total_items": total_items,
        "low_stock": low_stock,
        "total_history": total_history,
        "items": items,
    }
    return render(request, "activity/dashboard.html", context)
