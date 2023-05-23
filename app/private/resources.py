from flask import request, json, jsonify
from flask_restful import Resource, Api

from . import private_bp
from .models import Course
from .schemas import CourseSchema

api = Api(private_bp)
courseSchema = CourseSchema()

class CourseResource(Resource):
    def get(self):
        courses = Course.get_all()
        response = courseSchema.dump(courses, many=True)
        return jsonify(response)

    def post(self):
        data = request.get_json()
        professor = data['professor']
        title = data['title']
        description = data['description']
        url = data['url']
        course = Course(professor=professor, title=title, description=description, url=url)
        course.save()
        return jsonify(id=course.id, professor=course.professor, title=course.title)

    def put(self, id):
        data = request.get_json()
        course = Course.get_by_id(id)
        course.professor = data['professor']
        course.title = data['title']
        course.description = data['description']
        course.url = data['url']
        course.save()
        response = courseSchema.dump(course)
        return response

    def delete(self, id):
        course = Course.get_by_id(id)
        course.delete()
        return {"msg": "Deleted!"}

api.add_resource(CourseResource, '/course')
api.add_resource(CourseResource, '/course/<id>', endpoint='course')
