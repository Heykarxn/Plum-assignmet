from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services.ocr import extract_raw_tokens
from services.normalize import normalize_tokens
from services.classify import classify_amounts
from services.response import build_final_response


# ------------------ App Init ------------------
app = FastAPI(
    title="AI-Powered Amount Detection",
    description="Extract and classify amounts from medical bills",
    version="1.0"
)


# ------------------ Request Model ------------------
class AmountDetectionRequest(BaseModel):
    text: str


# ------------------ Routes ------------------
@app.get("/")
def root():
    return {"message": "AI-Powered Amount Detection API is running"}


@app.post("/detect-amounts")
def detect_amounts(request: AmountDetectionRequest):
    """
    Full pipeline:
    Step 1 -> OCR/Text extraction
    Step 2 -> Normalization
    Step 3 -> Context classification
    Step 4 -> Final response
    """

    text = request.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    # Step 1: OCR / Token extraction
    ocr_result = extract_raw_tokens(text)
    if "status" in ocr_result:
        return ocr_result

    # Step 2: Normalization
    normalized = normalize_tokens(ocr_result["raw_tokens"])

    # Step 3: Classification
    classified = classify_amounts(text, normalized["normalized_amounts"])

    # Step 4: Response building
    final_output = build_final_response(classified, text)

    return final_output


# ------------------ Optional: favicon fix ------------------
@app.get("/favicon.ico")
def favicon():
    return {}

