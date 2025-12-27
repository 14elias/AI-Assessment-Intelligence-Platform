# AlignEd

AlignEd is a FastAPI-based application designed to align exam questions with curriculum objectives using AI. It extracts questions from PDF exams, normalizes them, and maps them to learning objectives from the curriculum.

## Features

- **PDF Text Extraction**: Upload PDF files and extract text content.
- **AI-Powered Question Extraction**: Use OpenAI's GPT-3.5-turbo via OpenRouter to parse and normalize exam questions.
- **Objective Mapping**: Map questions to curriculum objectives with confidence scores.
- **CRUD Operations**: Manage departments, courses, topics, objectives, and more.
- **Database Integration**: Asynchronous SQLAlchemy with SQLite (configurable).
- **Migrations**: Alembic for database schema management.

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd AlignEd
   ```

2. Install dependencies using Poetry (assuming pyproject.toml is configured):

   ```
   poetry install
   ```

3. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add your OpenRouter API key:
     ```
     API_KEY=your_openrouter_api_key_here
     ```
   - Optionally, configure database URL if not using default SQLite.

4. Run database migrations:
   ```
   alembic upgrade head
   ```

## Usage

1. Activate the virtual environment:

   ```
   poetry shell
   ```

2. Run the application:

   ```
   uvicorn main:app --reload
   ```

3. Access the API documentation at `http://localhost:8000/docs`.

### API Endpoints

The application provides comprehensive CRUD endpoints for managing educational entities, as well as exam processing. Key endpoints include:

#### Departments

- `POST /create_dep`: Create a new department.
- `GET /get_dep`: Retrieve a department by name.
- `GET /get_all_dep`: List all departments.
- `DELETE /get_all_dep`: Delete a department by name.

#### Academic Years

- `POST /create_ayear`: Create a new academic year.
- `GET /get_academic_year`: Retrieve an academic year by year number.

#### Courses

- `POST /create_course`: Create a new course.
- `GET /get_course`: Retrieve a course by name.
- `GET /get_all_course`: List all courses.
- `DELETE /delete_course`: Delete a course by name.

#### Semesters

- `POST /create_semister`: Create a new semester.

#### Topics

- `POST /create_topic`: Create a new topic.
- `GET /get_topic`: Retrieve a topic by name.
- `GET /get_all_topic`: List all topics.
- `DELETE /delete_topic`: Delete a topic by name.

#### Objectives

- `POST /create_objective`: Create a new learning objective.
- `GET /get_all_objective`: List all objectives.
- `DELETE /delete_objective`: Delete an objective by ID.

#### Course Offerings

- `POST /create_course_offering`: Create a new course offering.
- `GET /get_all_course_offering`: List all course offerings.
- `GET /get_course_offering`: Retrieve objectives for a specific course offering.

#### Exams

- `POST /exam/upload`: Upload a PDF exam and get question mappings to objectives.

For detailed request/response schemas and interactive testing, visit `http://localhost:8000/docs`.

## Project Structure

- `api/`: FastAPI route handlers.
- `core/`: Configuration and AI client.
- `crud/`: Database CRUD operations.
- `db/`: Database setup and session management.
- `models/`: SQLAlchemy models.
- `schema/`: Pydantic schemas.
- `services/`: Business logic, including AI services and PDF processing.
- `utils/`: Utility functions for prompts and formatting.

## Dependencies

- FastAPI
- SQLAlchemy
- Alembic
- httpx
- pdfplumber
- pydantic-settings
- OpenRouter API (for AI)

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
