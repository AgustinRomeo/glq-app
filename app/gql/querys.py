from graphene import ObjectType, List as gList, Field, Int
from app.gql.types import JobObject, EmployerObject, UserObject, JobApplicationObject
from app.db.database import Session
from app.db.models import Job, Employer, User, JobApplication


class Query(ObjectType):
    jobs = gList(JobObject)
    job = Field(JobObject, id=Int(required=True))
    employers = gList(EmployerObject)
    employer = Field(EmployerObject, id=Int(required=True))
    users = gList(UserObject)
    job_applications = gList(JobApplicationObject)

    @staticmethod
    def resolve_jobs(root, info):
        return Session().query(Job).all()

    @staticmethod
    def resolve_employers(root, info):
        return Session().query(Employer).all()

    @staticmethod
    def resolve_job(root, info, id):
        return Session().query(Job).filter(Job.id == id).first()

    @staticmethod
    def resolve_employer(root, info, id):
        return Session().query(Employer).filter(Employer.id == id).first()

    @staticmethod
    def resolve_users(root, info):
        return Session().query(User).all()

    @staticmethod
    def resolve_job_applications(root, info):
        return Session().query(JobApplication).all()
