# 🌾 Smart Farming Advisor - Agentic AI System

An intelligent multi-tool AI system for precision agriculture, combining crop recommendation, disease detection, and farming knowledge Q&A.

---
## 🎯 Project Overview
**Smart Farming Advisor** is an agentic AI system that helps farmers make data-driven decisions through:
1.  **🌾 Crop Recommendation** - Predicts optimal crops based on soil and climate conditions
2.  **🍃 Disease Detection** - Identifies plant diseases from leaf images
3.  **❓ Farming Q&A** - Answers farming questions using RAG (Retrieval-Augmented Generation)

The system uses an **intelligent agent** to automatically route user queries to the appropriate tool.

---
## 📊 Performance Metrics

| Component | Model/Method | Accuracy/Score | Status |
|-----------|-------------|----------------|---------|
| **Crop Recommendation** | Random Forest + Feature Engineering | **99.39%** | ✅ Excellent |
| **Disease Detection** | ResNet50 (Transfer Learning) | **98.97%** | ✅ Research-grade |
| **RAG Q&A** | FAISS + Sentence Transformers | **Hit Rate: 100%<br>MRR: 1.0** | ✅ Production-ready |
| **Agent Routing** | Intent Classification | **100%** (4/4 correct) | ✅ Perfect |

---
## 🏗️ System Architecture
```bash

        User Query          → Intelligent Agent               → Tool Router 
         ┌────────────────────────────┼───────────────────────────────────┐ 
         ↓                            ↓                                   ↓ 
    Crop Predictor         Disease Detector                      RAG Q&A 
    (Random Forest)           (ResNet50)                       (FAISS + LLM)

```
## 🚀 Quick Start

### Prerequisites

-   Python 3.8+
-   pip
-   4GB+ RAM
-   (Optional) CUDA-capable GPU for faster inference

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/juni2003/smart-farming-advisor.git](https://github.com/juni2003/smart-farming-advisor.git)
    cd smart-farming-advisor
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up environment variables:**
    ```bash
    cp .env.example .env
    # Edit .env and add your GOOGLE_API_KEY (for Gemini LLM - optional)
    ```
4.  **Download large model files:**
    The ResNet50 model file (`disease_model_resnet50.pth`, ~98MB) is too large for GitHub.

    * **Option A:** Download from a host (e.g., Google Drive):
        [Download ResNet50 Model](<INSERT_YOUR_DOWNLOAD_LINK_HERE>)
        Place in `models/disease_model_resnet50.pth`
    * **Option B:** Train yourself (see Training section)

### 💻 Usage
**Option 1: Interactive Agent**
```python
from src.agent.farming_agent import FarmingAgent

# Initialize agent
agent = FarmingAgent()
agent.initialize()

# Example 1: Crop Recommendation
crop_params = {
    'N': 90, 'P': 42, 'K': 43,
    'temperature': 20, 'humidity': 82,
    'ph': 6.5, 'rainfall': 202
}
response = agent.process_query(
    "What crop should I plant?",
    crop_params=crop_params
)
print(response['response'])
# Output: "Based on your soil and climate conditions, I recommend: rice (Confidence: 93.0%)"

# Example 2: Disease Detection
response = agent.process_query(
    "My plant looks sick, can you identify the disease?",
    image_path="path/to/leaf_image.jpg"
)
print(response['response'])
# Output: "Disease Detected: Tomato_Early_blight (Confidence: 99.5%)"

# Example 3: Farming Q&A
response = agent.process_query(
    "How often should I water tomato plants?"
)
print(response['response'])
# Output: "Tomato plants should be watered every 2-3 days, keeping the soil moist but not waterlogged."

```


**Option 2: Indiviual tools**

```python
# Crop Predictor
from src.tools.crop_predictor_tool import CropPredictorTool

tool = CropPredictorTool()
result = tool.predict(N=90, P=42, K=43, temperature=20, 
                      humidity=82, ph=6.5, rainfall=202)
print(f"Recommended crop: {result['recommended_crop']}")

# Disease Detector
from src.tools.disease_detector_tool import DiseaseDetectorTool

tool = DiseaseDetectorTool()
result = tool.predict("path/to/leaf_image.jpg")
print(f"Disease: {result['predicted_disease']}")

# RAG Q&A
from src.tools.rag_qa_tool import RAGQATool

tool = RAGQATool()
result = tool.answer_question("What is the best time to plant rice?")
print(result['answer'])

```
## 📚 Dataset Information
| Dataset | Source | Samples | Classes | Purpose |
|---|---|---|---|---|
| Crop Recommendation | Kaggle | 2,200 | 22 crops | Soil-based crop prediction |
| Plant Disease | PlantVillage | 20,639 images | 15 diseases | Disease identification |
| FAQ Knowledge Base | Custom | 10 documents | - | Farming Q&A |

---
## 🧠 Model Details
### 1. Crop Recommendation Model
-   **Algorithm:** Random Forest Classifier
-   **Features:** N, P, K, Temperature, Humidity, pH, Rainfall + 4 engineered features
-   **Training:** 80/20 train-test split, 5-fold cross-validation
-   **Performance:**
    -   Test Accuracy: `99.39%`
    -   Macro F1-Score: `99.37%`
-   **Training time:** ~2 seconds

### 2. Disease Detection Model
-   **Architecture:** ResNet50 (Transfer Learning)
-   **Pretrained on:** ImageNet
-   **Fine-tuning:** Last 30 layers trainable
-   **Input:** 224x224 RGB images
-   **Training:**
    -   GPU: Google Colab (T4)
    -   Epochs: 15 (early stopping at 14)
    -   Time: 33 minutes
    -   Augmentation: Rotation, flip, color jitter
-   **Performance:**
    -   Test Accuracy: `98.97%`
    -   Validation Accuracy: `99.00%`
    -   All 3 test predictions: `100%` confidence

### 3. RAG System
-   **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`
-   **Vector Store:** FAISS (IndexFlatL2)
-   **LLM:** Google Gemini 2.0 Flash (optional)
-   **Performance:**
    -   Hit Rate@3: `100%`
    -   Mean Reciprocal Rank: `1.0`
    -   Average Relevance: `63.99%`
    -   Top-1 Relevance: `75.61%`

---
## 🧪 Testing & Evaluation
Run comprehensive tests:
```bash
# Test all components
python src/agent/farming_agent.py

# Test individual components
python src/tools/crop_predictor_tool.py
python src/tools/disease_detector_tool.py
python src/tools/rag_qa_tool.py

# Evaluate RAG system
python src/evaluation/rag_evaluation.py


```
Evaluation results are saved in outputs/results/.
---
## 🎓 Training Models from Scratch
### Train Crop Model
```bash
python src/data/preprocess_crop.py    # Preprocess data
python src/models/crop_model.py       # Train model

```
## Train Disease Detection Model
**Local (CPU):**
```bash
python src/data/preprocess_disease.py  # Preprocess images
python src/models/disease_model.py     # Train Simple CNN (~4 hours)
```
**Google Colab (GPU - Recommended):**
1.  Upload preprocessed data to Google Drive
2.  Use provided Colab notebook: `notebooks/disease_training_colab.ipynb`
3.  Training time: ~33 minutes on T4 GPU
4.  Download trained model and place in `models/`

---
## 📁 Project Structure
```bash
smart-farming-advisor/
├── src/
│   ├── data/           # Data download & preprocessing
│   ├── models/         # Model training scripts
│   ├── rag/            # RAG pipeline
│   ├── tools/          # Individual tools
│   ├── agent/          # Intelligent agent
│   └── evaluation/     # Evaluation scripts
├── models/             # Trained models
├── outputs/            # Results & visualizations
├── config.py           # Configuration
├── requirements.txt    # Dependencies
└── README.md           # This file
```

## 📦 Requirements
```bash
# Core
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
joblib>=1.3.0

# Deep Learning
torch>=2.0.0
torchvision>=0.15.0
Pillow>=10.0.0

# RAG
sentence-transformers>=2.2.0
faiss-cpu>=1.7.4
google-generativeai>=0.3.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
tqdm>=4.65.0
```

## 🎯 Key Features
-   ✅ **Multi-modal AI System** - Text, images, and structured data
-   ✅ **Agentic Routing** - Intelligent query classification
-   ✅ **Transfer Learning** - ResNet50 pretrained on ImageNet
-   ✅ **RAG Implementation** - Semantic search with FAISS
-   ✅ **Production-Ready** - 98-99% accuracy across all models
-   ✅ **Modular Architecture** - Easy to extend and maintain
-   ✅ **Comprehensive Testing** - All components tested

---
## 📊 Results Summary
### Crop Recommendation
-   ✅ 99.39% test accuracy
-   ✅ Perfect predictions for rice, wheat, cotton
-   ✅ All 22 crops classified correctly

### Disease Detection
-   ✅ 98.97% test accuracy
-   ✅ 100% confidence on test samples
-   ✅ Perfect classification: Pepper Bacterial Spot, Potato Early Blight, etc.

### RAG Q&A
-   ✅ 100% hit rate (all queries found relevant documents)
-   ✅ MRR of 1.0 (relevant docs always rank #1)
-   ✅ 75.61% average top-1 relevance

### Agent System
-   ✅ 100% intent classification accuracy
-   ✅ Correct tool routing for all test queries

---
## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

---
## 📄 License
This project is licensed under the MIT License.

---
## 👨‍💻 Author
-   **juni2003** - [GitHub Profile](https://github.com/juni2003)
-   **Assignment:** AI Agentic System - Smart Farming Advisor
-   **Date:** November 2025

---
## 🙏 Acknowledgments
-   **Datasets:**
    -   [Crop Recommendation Dataset (Kaggle)](<https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?utm_source=chatgpt.com>)
    -   [PlantVillage Disease Dataset](<https://www.kaggle.com/datasets/emmarex/plantdisease>)
    -   [Farmer Support Faq Dataset](<https://www.opendatabay.com/data/synthetic/fa678ba5-8ed4-4a9e-8faa-dc87b2a5ce66?utm_source=chatgpt.com>)
-   **Pretrained Models:**
    -   ResNet50 (ImageNet, PyTorch)
    -   `sentence-transformers/all-MiniLM-L6-v2` (HuggingFace)
-   **Tools:**
    -   Google Colab (GPU training)
    -   FAISS (Facebook AI Similarity Search)
    -   Google Gemini API (LLM)

---
## 📞 Contact
For questions or feedback, please contact: **juni.xatti@gmail.com**

---
⭐ If you find this project helpful, please give it a star!
