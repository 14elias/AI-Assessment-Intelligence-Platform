from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Form, Request
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from services import pdf_service, segmentation_service, text_normalizer, exam_canonicalizer, exam_normalizer_AI
from utils import map_questions_to_objectives, format_question, build_prompt
from schema.course_offering_schema import CreateCourseOffering
from crud import course_offering_crud

router = APIRouter(tags=['exam'])


@router.post('/upload_exam')
async def upload_exam(
    department_id: int = Form(...),
    course_id: int = Form(...),
    academic_year_id: int = Form(...),
    semester_id: int = Form(...),
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    data = CreateCourseOffering(
        department_id=department_id,
        course_id=course_id,
        academic_year_id=academic_year_id,
        semester_id=semester_id,
    )

    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    content = pdf_service.extract_text_from_pdf(file)
    response = await exam_normalizer_AI.extract_questions_with_ai(content)
    # normalized = text_normalizer.normalize_text(content)
    # canonical = exam_canonicalizer.canonicalize(normalized)
    # questions, rejected = segmentation_service.segment_questions(canonical)
    
    # print(f'rejected: {len(rejected)}')
    # print(f'questions: {len(questions)}')
    
    formatted_questions = [
        format_question.format_mcq_question(q) for q in response["questions"]
    ]
    curiculum_objects = await course_offering_crud.get_objectives(data.model_dump(), db)

    prompt = build_prompt.build_prompt(formatted_questions, curiculum_objects)

    result = await map_questions_to_objectives.map_questions_to_objectives(formatted_questions, curiculum_objects)

    return result

