# Plant-Disease-Detection-
# 🌿 Plant Disease Detection

An AI-powered web application that identifies plant diseases from leaf images using a Roboflow-hosted inference workflow. The application provides a simple interface where users can upload a plant image and view the model's predictions with confidence scores.

## 📌 Project Overview

Plant diseases can affect crop health and agricultural productivity. Early identification can help users recognize potential plant health issues.

This project provides an image-based plant disease detection interface built with **Python, Streamlit, and Roboflow**. Users can upload an image of a plant leaf, and the application sends it to a trained inference workflow to generate predictions.

## ✨ Features

- Upload plant leaf images through a web interface.
- Detect potential plant diseases using a Roboflow inference workflow.
- Display predicted classes and confidence scores.
- Simple and interactive interface built with Streamlit.
- Cloud-based inference through the Roboflow API.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| Roboflow Inference SDK | Model inference |
| Pillow (PIL) | Image handling |
| Roboflow Workflow | Image prediction |

## ⚙️ How It Works

1. The user uploads a plant leaf image.
2. The application processes the uploaded image.
3. The image is sent to the Roboflow-hosted inference workflow.
4. The workflow analyzes the image and returns predictions.
5. The application displays the predicted classes and confidence scores.

## 📂 Project Structure

```text
Plant-Disease-Detection/
│
├── app.py
├── roboflow_test.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Plant-Disease-Detection
```

### 3. Create a virtual environment

```bash
py -3.11 -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
py -3.11 -m pip install -r requirements.txt
```

### 6. Configure the Roboflow API key

Set your private Roboflow API key in PowerShell:

```powershell
$env:ROBOFLOW_API_KEY="YOUR_PRIVATE_API_KEY"
```

**Important:** Keep your API key private. Never upload it to GitHub or include it directly in your source code.

### 7. Run the application

```bash
py -3.11 -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `ROBOFLOW_API_KEY` | Private API key used to authenticate with Roboflow |

## 🧪 Testing

The project includes `roboflow_test.py`, which can be used to test the Roboflow inference workflow independently.

```bash
py -3.11 -u roboflow_test.py
```

## 🔮 Future Improvements

- Support for additional plant species and disease categories.
- Display disease-specific information and possible preventive measures.
- Improve the user interface and prediction visualization.
- Add prediction history and image-based reporting.

## 👩‍💻 Author

**Jayita Saikia**

B.Tech – Artificial Intelligence & Machine Learning
Jayita Saikia

---

*Developed as an AI/ML project exploring image-based plant disease identification using cloud inference.*
