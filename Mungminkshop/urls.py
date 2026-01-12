from django.contrib import admin

admin.site.site_header = "ระบบจัดการหลังบ้าน MungMink Shop"
admin.site.site_title = "MungMink Admin"
admin.site.index_title = "จัดการสต็อกและประวัติการสุ่ม"

from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls")),  # หน้าแรกสุดจะเรียกแอป store
    path("activity/", include("activity.urls")),  # หน้าสุ่มจะย้ายไปที่ /activity/
]
