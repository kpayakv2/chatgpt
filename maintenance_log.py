# สร้างโปรแกรมบันทึกการซ่อมบำรุง
# ฟังก์ชัน: บันทึกชิ้นส่วน, บันทึกระยะทาง, คำนวณการสึกหรอ
"""โมดูลสำหรับบันทึกการซ่อมบำรุง"""
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class MaintenanceLog(Base):
    __tablename__ = 'maintenance_log'
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.utcnow)
    part = Column(String(100), nullable=False)
    mileage = Column(Integer)
    notes = Column(String(200))

engine = create_engine('sqlite:///maintenance.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def add_log(part, mileage=None, notes=None):
    """บันทึกรายการซ่อมบำรุงใหม่"""
    session = Session()
    log = MaintenanceLog(part=part, mileage=mileage, notes=notes)
    session.add(log)
    session.commit()
    session.close()


def get_logs():
    """ดึงรายการซ่อมบำรุงทั้งหมด"""
    session = Session()
    logs = (
        session.query(MaintenanceLog)
        .order_by(MaintenanceLog.date.desc())
        .all()
    )
    session.close()
    return logs
requirements.txt
ใหม่
+2
-0

Flask
Flask-SQLAlchemy
templates/add.html
ใหม่
+20
-0

<!doctype html>
<html lang="th">
<head>
    <meta charset="utf-8">
    <title>เพิ่มรายการซ่อมบำรุง</title>
</head>
<body>
    <h1>เพิ่มรายการซ่อมบำรุง</h1>
    <form method="post">
        <label for="part">ชิ้นส่วน:</label>
        <input type="text" name="part" id="part" required><br>
        <label for="mileage">ระยะทาง:</label>
        <input type="number" name="mileage" id="mileage"><br>
        <label for="notes">หมายเหตุ:</label>
        <textarea name="notes" id="notes"></textarea><br>
        <button type="submit">บันทึก</button>
    </form>
    <a href="{{ url_for('index') }}">กลับหน้าหลัก</a>
</body>
</html>