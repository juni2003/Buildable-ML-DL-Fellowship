import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# PROJECT PATHS
# ============================================================================
BASE_DIR = Path(__file__).parent.absolute()
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = BASE_DIR / "models"
OUTPUTS_DIR = BASE_DIR / "outputs"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"

# Create directories if they don't exist
for dir_path in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, OUTPUTS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# ============================================================================
# DATASET PATHS
# ============================================================================
# Crop Dataset
CROP_RAW_DIR = RAW_DATA_DIR / "crop"
CROP_PROCESSED_PATH = PROCESSED_DATA_DIR / "crop_processed.csv"

# Disease Dataset
DISEASE_RAW_DIR = RAW_DATA_DIR / "disease"
DISEASE_PROCESSED_DIR = PROCESSED_DATA_DIR / "disease_processed"

# FAQ Dataset
FAQ_RAW_DIR = RAW_DATA_DIR / "faq"
FAQ_PROCESSED_PATH = PROCESSED_DATA_DIR / "knowledge_base.txt"

# ============================================================================
# MODEL PATHS
# ============================================================================
CROP_MODEL_PATH = MODELS_DIR / "crop_model.pkl"
CROP_SCALER_PATH = MODELS_DIR / "crop_scaler.pkl"
CROP_LABEL_ENCODER_PATH = MODELS_DIR / "crop_label_encoder.pkl"

DISEASE_MODEL_PATH = MODELS_DIR / "disease_model.h5"
DISEASE_LABEL_ENCODER_PATH = MODELS_DIR / "disease_label_encoder.pkl"

VECTOR_STORE_PATH = MODELS_DIR / "vector_store"

# ============================================================================
# CROP MODEL CONFIGURATION
# ============================================================================
CROP_MODEL_CONFIG = {
    "test_size": 0.15,
    "val_size": 0.15,
    "random_state": 42,
    "features": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
    "target": "label",
    "models_to_train": {
        "logistic_regression": True,
        "random_forest": True,
        "xgboost": True
    }
}

# ============================================================================
# DISEASE MODEL CONFIGURATION
# ============================================================================
DISEASE_MODEL_CONFIG = {
    "image_size": (224, 224),
    "batch_size": 32,
    "epochs": 20,
    "learning_rate": 0.001,
    "validation_split": 0.15,
    "test_split": 0.15,
    "augmentation": {
        "rotation_range": 20,
        "width_shift_range": 0.2,
        "height_shift_range": 0.2,
        "horizontal_flip": True,
        "zoom_range": 0.2,
        "brightness_range": [0.8, 1.2]
    },
    "models_to_train": {
        "cnn": True,
        "resnet50": True,
        "mobilenetv2": False
    }
}

# ============================================================================
# RAG CONFIGURATION
# ============================================================================
RAG_CONFIG = {
    "chunk_size": 500,
    "chunk_overlap": 50,
    "top_k": 5,
    "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
    "llm_model": "gemini-pro",
    "temperature": 0.7,
    "max_tokens": 1024
}

# ============================================================================
# AGENT CONFIGURATION
# ============================================================================
AGENT_CONFIG = {
    "framework": "langchain",  # or "llamaindex"
    "llm_model": "gemini-pro",
    "temperature": 0.3,
    "verbose": True,
    "max_iterations": 5
}

# ============================================================================
# API KEYS
# ============================================================================
GOOGLE_API_KEY = os.getenv("AIzaSyCs6Bd4u4IA2rfgL9dFUM0i4bfwGKIliQU")

# FAQ paths
FAQ_PROCESSED_PATH = PROCESSED_DATA_DIR / "knowledge_base.txt"
# ============================================================================
# VERIFICATION
# ============================================================================
def verify_setup():
    """Verify that all required components are in place"""
    
    print("=" * 70)
    print("🌾 SMART FARMING ADVISOR - CONFIGURATION CHECK 🌾")
    print("=" * 70)
    
    # Check API Key
    if GOOGLE_API_KEY:
        print("✅ Google API Key loaded")
    else:
        print("⚠️  WARNING: GOOGLE_API_KEY not found in .env file")
        print("   Get your key from: https://makersuite.google.com/app/apikey")
    
    # Check Crop Dataset
    print("\n📊 CROP DATASET:")
    crop_files = list(CROP_RAW_DIR.glob("*.csv"))
    if crop_files:
        print(f"   ✅ Found {len(crop_files)} CSV file(s)")
        for f in crop_files:
            print(f"      - {f.name}")
    else:
        print(f"   ⚠️  No CSV files found in {CROP_RAW_DIR}")
    
    # Check Disease Dataset
    print("\n🍃 DISEASE DATASET:")
    if DISEASE_RAW_DIR.exists():
        subdirs = [d for d in DISEASE_RAW_DIR.iterdir() if d.is_dir()]
        if subdirs:
            print(f"   ✅ Found {len(subdirs)} folder(s)")
            # Count images
            total_images = sum(len(list(d.glob("**/*.jpg"))) + len(list(d.glob("**/*.png"))) for d in subdirs)
            print(f"   📸 Total images found: {total_images}")
        else:
            print(f"   ⚠️  No subfolders found in {DISEASE_RAW_DIR}")
    else:
        print(f"   ⚠️  Disease directory not found: {DISEASE_RAW_DIR}")
    
    # Check FAQ Dataset
    print("\n📚 FAQ DATASET:")
    faq_files = list(FAQ_RAW_DIR.glob("*.csv")) + list(FAQ_RAW_DIR.glob("*.json")) + list(FAQ_RAW_DIR.glob("*.txt"))
    if faq_files:
        print(f"   ✅ Found {len(faq_files)} file(s)")
        for f in faq_files:
            print(f"      - {f.name}")
    else:
        print(f"   ⚠️  No FAQ files found in {FAQ_RAW_DIR}")
    
    print("\n" + "=" * 70)
    print(f"📁 Base Directory: {BASE_DIR}")
    print("=" * 70)

# Run verification when config is imported
if __name__ == "__main__":
    verify_setup()