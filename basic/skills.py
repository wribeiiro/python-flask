from flask_restful import Resource

skills_lis = ['Python', 'Java', 'Flask', 'PHP']
class Skills(Resource):
    def get(self):
        return skills_lis