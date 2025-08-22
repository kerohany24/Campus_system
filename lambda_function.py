import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")

# اسم الجداول (لازم تكون موجودة في DynamoDB بنفس الأسماء دي)
COURSE_TABLE = "Courses"
STUDENT_TABLE = "Students"
ATTENDANCE_TABLE = "Attendance"

def lambda_handler(event, context):
    try:
        path = event["resource"]   # هيكون /courses أو /students أو /attendance
        method = event["httpMethod"]

        body = json.loads(event["body"])

        if method == "POST":
            if path == "/courses":
                table = dynamodb.Table(COURSE_TABLE)
                table.put_item(Item={
                    "course_id": body["course_id"],
                    "name": body["name"]
                })
                return response(200, {"message": "Course added successfully"})

            elif path == "/students":
                table = dynamodb.Table(STUDENT_TABLE)
                table.put_item(Item={
                    "student_id": body["student_id"],
                    "name": body["name"]
                })
                return response(200, {"message": "Student added successfully"})

            elif path == "/attendance":
                table = dynamodb.Table(ATTENDANCE_TABLE)
                table.put_item(Item={
                    "course_id": body["course_id"],
                    "date_student": body["date_student"],  # format: date#studentId
                    "status": body["status"]
                })
                return response(200, {"message": "Attendance recorded successfully"})

        return response(400, {"error": "Invalid path or method"})

    except Exception as e:
        return response(500, {"error": str(e)})


def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": json.dumps(body)
    }