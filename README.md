# Django Web Application

โปรเจกต์ Django เชื่อมต่อฐานข้อมูล Neon PostgreSQL

## การติดตั้งและตั้งค่า

1. **สร้าง Virtual Environment และติดตั้ง Dependencies**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # บน Windows
   pip install -r requirements.txt
   ```

2. **ตั้งค่า Environment Variables**:
   สร้างไฟล์ `.env` ที่ root directory:
   ```env
   DATABASE_URL=postgresql://user:password@host/dbname?sslmode=require
   ```

3. **รัน Migration และเริ่มใช้งาน**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
"# Django_Database" 
"# Django_Database" 
