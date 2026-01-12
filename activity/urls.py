from django.urls import path
from . import views  # <<--- เพิ่มบรรทัดนี้เข้าไปครับ (จุด . หมายถึงโฟลเดอร์ปัจจุบัน)

urlpatterns = [
    path("", views.home, name="activity_home"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
