# 🎓 Campus Management System on AWS

This project is a simple **Campus Management System** built entirely using AWS serverless services.  
It allows adding courses, registering students, and recording attendance with a lightweight frontend.

---

## 🚀 Architecture
- **Amazon S3** → Hosts the static website (HTML + JS).
- **Amazon API Gateway** → Handles HTTP requests from the frontend.
- **AWS Lambda** → Contains backend logic written in Python.
- **Amazon DynamoDB** → Stores data for:
  - Courses
  - Students
  - Attendance

![Architecture](architecture/campus_system_architecture.png)

---

## 📂 Project Structure
