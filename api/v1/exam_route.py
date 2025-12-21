from fastapi import APIRouter, UploadFile, File, HTTPException
from services import pdf_service, segmentation_service, text_normalizer, exam_canonicalizer
from utils import text_cleaning

router = APIRouter()


@router.post('/upload_exam')
def upload_exam(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    content = pdf_service.extract_text_from_pdf(file)
    normalized = text_normalizer.normalize_text(content)
    canonical = exam_canonicalizer.canonicalize(normalized)
    questions, rejected = segmentation_service.segment_questions(canonical)
    
    print(f'rejected: {len(rejected)}')
    print(f'questions: {len(questions)}')
    return questions

@router.post('/test_upload_exam')
def test_upload_exam(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    content = pdf_service.extract_text_from_pdf(file)
    print(content)
    cleaned_content = text_cleaning.clean_text(content)
    segmented_text = segmentation_service.test_segment_questions(cleaned_content)
    return segmented_text