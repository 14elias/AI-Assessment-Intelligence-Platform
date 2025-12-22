from fastapi import FastAPI
from api.v1 import (
    exam_route, 
    dep_route, 
    topic_route, 
    course_route, 
    objective_route, 
    academic_year_route,
    course_offering_route,
    semister_route
)

app = FastAPI()
app.include_router(exam_route.router)
app.include_router(dep_route.router)
app.include_router(topic_route.router)
app.include_router(course_route.router)
app.include_router( objective_route.router)
app.include_router( academic_year_route.router)
app.include_router( course_offering_route.router)
app.include_router( semister_route.router)

@app.get('/')
def main():
    return 'hello guys'

if __name__ == "__main__":
    main()
