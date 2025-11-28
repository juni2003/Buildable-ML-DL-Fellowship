# Buildable ML/DL Fellowship 🤖🚀

Welcome to the **Buildable ML/DL Fellowship** repository!   
This is a **3-month immersive journey** into Machine Learning (ML) and Deep Learning (DL), designed to build strong foundations in AI while practicing hands-on coding and real-world projects.  

This repository showcases my complete learning progression—from Python fundamentals to building production-ready agentic AI systems—through weekly assignments, comprehensive projects, and a capstone project.

---

## 🌍 About Buildables

**Buildables** is a learning community in Pakistan focused on empowering students and developers in AI, ML, and Deep Learning.   
Through collaborative projects, mentorship, and peer discussions, it encourages learners to explore **intelligent systems** and apply their skills to real-world problems.  

---

## 📚 What I Learned

Throughout this fellowship, I gained **practical skills and theoretical foundations** in ML/DL, progressing from basic programming to advanced AI systems.  Here's my learning journey organized from foundational concepts to advanced implementations:

### 🐍 **Python Fundamentals & Programming Logic**
- Writing clean, efficient Python code with proper structure
- Data structures: Mutable vs Immutable (lists, tuples, dictionaries)
- Input validation, error handling, and conditional logic
- Function creation, lambda functions, and functional programming
- Statistical operations (mean, median, max, min)
- File handling and data manipulation

### 📊 **Data Handling & Preprocessing**
- Working with NumPy and Pandas for data manipulation
- Handling missing values with multiple imputation strategies
- Data cleaning, transformation, and normalization
- Feature encoding (one-hot encoding, label encoding)
- Feature scaling and standardization
- Data augmentation techniques with Gaussian noise
- Creating reproducible data pipelines

### 📈 **Exploratory Data Analysis (EDA)**
- Statistical summarization and descriptive analysis
- Data visualization with Matplotlib and Seaborn
- Creating histograms, scatter plots, box plots, and correlation heatmaps
- Identifying patterns, outliers, and anomalies
- Domain-specific data exploration (weather, automotive, real estate, agriculture)

### 🔧 **Feature Engineering**
- Creating derived features from existing data
- Text feature extraction and processing
- Geospatial feature engineering
- Feature interaction and polynomial features
- Feature selection and dimensionality reduction
- Domain knowledge application for better features

### 🤖 **Machine Learning Foundations**
- **Supervised Learning**: Regression and Classification
- **Model Training**: Train-test splitting, stratified sampling
- **Algorithms Implemented**:
  - Linear/Logistic Regression
  - Decision Trees
  - Random Forest (ensemble learning)
  - Support Vector Machines
  - K-Nearest Neighbors
- **Model Evaluation**: Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix
- **Cross-Validation**: K-fold validation for robust performance estimation
- **Model Serialization**: Saving models with joblib for deployment

### 🧠 **Deep Learning Essentials**
- Neural network architecture design
- **Artificial Neural Networks (ANNs)**: Fully connected layers, activation functions
- **Convolutional Neural Networks (CNNs)**: Conv2D, MaxPooling, feature extraction
- Understanding backpropagation and gradient descent
- Optimizer selection (Adam, SGD)
- Loss functions (Binary Crossentropy, Categorical Crossentropy)
- Regularization techniques (Dropout, Early Stopping)
- Model callbacks (EarlyStopping, ModelCheckpoint)
- Training loops and epoch management

### 🖼️ **Computer Vision & Image Classification**
- Image preprocessing and normalization
- Building CNNs from scratch for image classification
- **Transfer Learning**: Fine-tuning pretrained models (ResNet50)
- Data augmentation (rotation, flipping, color jitter)
- Handling different image datasets:
  - MNIST (28x28 grayscale, 10 classes) → 98.64% accuracy
  - Cat vs Dog (150x150 RGB, binary) → 69% accuracy
  - Plant Disease (224x224 RGB, 15 classes) → 98.97% accuracy
- Performance comparison: ANN vs CNN architectures
- Training on GPU with Google Colab

### 🔍 **Advanced ML Techniques**
- End-to-end ML pipeline development
- Hyperparameter tuning strategies
- Handling class imbalance
- Ensemble methods and model stacking
- Feature importance analysis
- Model interpretability
- Binary and multi-class classification
- Regression modeling for continuous predictions

### 🤝 **Collaboration & Version Control**
- Git/GitHub workflows (branches, commits, pull requests)
- Repository organization and documentation
- Professional README creation
- Code commenting and documentation practices
- Collaborative development workflows

### 🤖 **Agentic AI Systems & RAG Implementation**
- **Retrieval-Augmented Generation (RAG)**: 
  - Vector embeddings with sentence-transformers
  - FAISS vector database for semantic search
  - Context retrieval and relevance ranking
  - LLM integration (Google Gemini API)
- **Intent Classification**: Query understanding and routing
- **Multi-Tool Agent Systems**: Intelligent tool selection
- **Production AI Architecture**: Modular, maintainable system design
- **Multi-Modal AI**: Combining text, images, and structured data

---

## 🎯 Key Projects & Achievements

### 📁 **Synthetic Data Pipeline**
Built an end-to-end ML pipeline with data generation, cleaning, augmentation, and model training. 
- **Models**: Logistic Regression vs Random Forest
- **Best Result**: 84% accuracy with Random Forest (ROC-AUC: 0.89)
- **Key Skills**: Data augmentation, pipeline automation, artifact management

### 🌦️ **Weather Classification System**
Multi-class classification predicting weather types from meteorological features.
- **Dataset**: 11 features (temperature, humidity, wind speed, precipitation, etc.)
- **Target**: 4 weather types (Rainy, Sunny, Cloudy, Snowy)
- **Models**: Logistic Regression, Decision Tree, Random Forest
- **Key Skills**: Multi-class classification, categorical encoding, model comparison

### 🚗 **Car Price Analysis**
Regression analysis on Pakistani used car market data (PakWheels dataset).
- **Features**: Make, Model, Year, Engine CC, Mileage, Transmission
- **Focus**: Comprehensive EDA and preprocessing for price prediction
- **Key Skills**: Real-world data cleaning, regression preprocessing

### 🐱🐶 **Image Classification: ANN vs CNN**
Comparative study demonstrating CNN superiority for image tasks.
- **MNIST Digits**: ANN (97.74%) vs CNN (98.64%)
- **Cat vs Dog**: ANN (57.30%) vs CNN (69%)
- **Key Finding**: CNNs excel at spatial feature extraction
- **Key Skills**: Deep learning, model comparison, transfer learning basics

### 🏠 **Airbnb Listing Analysis**
Complete ML/DL project analyzing Albany, NY Airbnb data.
- **Tasks**: Price prediction (regression) + Popularity classification
- **Features**: Text extraction, geospatial engineering, categorical encoding
- **Models**: Traditional ML + Neural Networks
- **Key Skills**: Feature engineering, hybrid ML/DL approach, end-to-end project

### 🌾 **Smart Farming Advisor (Final Capstone)**
Production-ready agentic AI system for precision agriculture with three integrated tools. 

**1. Crop Recommendation Tool**
- **Algorithm**: Random Forest with feature engineering
- **Accuracy**: **99.39%** on 22 crop types
- **Features**: Soil nutrients (N, P, K), climate (temp, humidity, pH, rainfall)

**2. Disease Detection Tool**
- **Architecture**: ResNet50 (Transfer Learning)
- **Accuracy**: **98.97%** on 15 plant diseases
- **Training**: Google Colab T4 GPU (33 minutes)
- **Dataset**: 20,639 images with data augmentation

**3. RAG Q&A System**
- **Components**: FAISS vector DB + Gemini LLM
- **Hit Rate**: **100%** (perfect retrieval)
- **MRR**: **1.0** (best document always ranked first)
- **Knowledge Base**: 10 farming FAQ documents

**Intelligent Agent**
- **Routing Accuracy**: **100%** (4/4 test queries)
- **Functionality**: Automatic intent classification and tool selection

**Key Skills**: Multi-modal AI, transfer learning, RAG, vector databases, agentic systems, production architecture

---

## 📊 Performance Highlights

| Project | Model/Method | Metric | Achievement |
|---------|-------------|---------|-------------|
| Synthetic Pipeline | Random Forest | ROC-AUC | 89. 89% |
| MNIST Classification | CNN | Accuracy | 98.64% |
| Cat vs Dog | CNN | Accuracy | 69% |
| **Crop Recommendation** | **Random Forest** | **Accuracy** | **99.39%** ✅ |
| **Disease Detection** | **ResNet50** | **Accuracy** | **98.97%** ✅ |
| **RAG Q&A** | **FAISS + Gemini** | **Hit Rate@3** | **100%** ✅ |
| **Agent Routing** | **Intent Classifier** | **Routing** | **100%** ✅ |

---

## 🛠️ Technologies & Tools Mastered

**Programming & Core Libraries**
- Python 3. 8+, Jupyter Notebook, Google Colab

**Data Science Stack**
- NumPy, Pandas, Matplotlib, Seaborn

**Machine Learning**
- scikit-learn (Classification, Regression, Ensemble Methods)
- Feature Engineering, Cross-Validation, Model Evaluation

**Deep Learning Frameworks**
- TensorFlow/Keras (CNNs, ANNs, Callbacks)
- PyTorch (Transfer Learning, ResNet50)

**Advanced AI**
- FAISS (Vector Database)
- sentence-transformers (Embeddings)
- Google Gemini API (LLM Integration)

**Development Tools**
- Git/GitHub (Version Control, Branching, PRs)
- joblib (Model Serialization)
- Environment Management

---

## 📁 Repository Structure

```
Buildable-ML-DL-Fellowship/
├── Week_1/                          # Python fundamentals & logic
├── Week_3/                          # Data pipeline & ML basics
│   └── synthetic_data_pipeline_project/
├── Week_4/                          # Classification & Regression
│   ├── classification/              # Weather prediction
│   └── regression/                  # Car price analysis
├── Week_6/                          # Deep Learning (ANN vs CNN)
├── Week_7/                          # Airbnb analysis project
└── final-project-smart-farming-advisor/  # Capstone agentic AI system
    ├── src/
    │   ├── data/                    # Data preprocessing
    │   ├── models/                  # Model training
    │   ├── rag/                     # RAG pipeline
    │   ├── tools/                   # Three AI tools
    │   ├── agent/                   # Intelligent agent
    │   └── evaluation/              # Metrics & testing
    ├── models/                      # Trained models
    ├── outputs/                     # Results & visualizations
    └── notebooks/                   # Colab training notebooks
```

---

## 🌟 Fellowship Experience

This fellowship was uniquely flexible, providing:
- **Self-paced learning** with curated materials
- **Hands-on weekly assignments** focusing on practical skills
- **3 weeks for the final project** allowing deep exploration
- **Real-world datasets** from Kaggle and public sources
- **Mentorship and community support** through Buildables

This repo documents my journey—it's more than just code, it's about **thinking like a researcher, building like an engineer, and collaborating like a team player**. 

---

## 🚀 Key Learnings & Takeaways

✅ **Progression from basics to advanced**: Python → ML → DL → Production AI  
✅ **Hands-on implementation**: 20+ models trained across various domains  
✅ **Real-world problem solving**: Weather, automotive, real estate, agriculture  
✅ **Production-ready skills**: 99%+ accuracy systems, modular architecture  
✅ **Multi-modal AI**: Text, images, structured data integration  
✅ **Best practices**: Version control, documentation, testing, evaluation  

---

## 🎓 What's Next? 

- Advanced NLP and transformer architectures
- Model deployment with FastAPI and Docker
- MLOps practices and experiment tracking
- Reinforcement Learning fundamentals
- Contributing to open-source AI projects

---

## 🤝 Connect

Let's continue the **Buildables** spirit:  
- Share ideas 💡  
- Collaborate on projects 🤝  
- Grow together as an AI community 🌍  

**GitHub**: [@juni2003](https://github.com/juni2003)  
**Email**: juni. xatti@gmail.com

Happy Learning & Coding!  🚀
