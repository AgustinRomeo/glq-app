from graphene import Schema
from fastapi import FastAPI
from starlette_graphene3 import *
from app.db.database import prepare_database, Session
from app.gql.querys import Query
from app.db.models import Employer, Job
from app.gql.mutations import Mutation

schema = Schema(query=Query, mutation=Mutation)

app = FastAPI()


@app.on_event("startup")
def startup_event():
    prepare_database()


@app.get("/employers")
def get_employers():
    with Session() as session:
        return session.query(Employer).all()


@app.get("/jobs")
def get_jobs():
    with Session() as session:
        return session.query(Job).all()


app.mount("/", GraphQLApp(
    schema=schema,
    on_get=make_playground_handler()
))
