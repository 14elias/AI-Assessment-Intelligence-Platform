from fastapi import FastAPI
from api.v1 import exam_route, dep_route, topic_route, course_route


app = FastAPI()
app.include_router(exam_route.router)
app.include_router(dep_route.router)
app.include_router(topic_route.router)
app.include_router(course_route.router)

@app.get('/')
def main():
    return 'hello guys'

if __name__ == "__main__":
    main()
