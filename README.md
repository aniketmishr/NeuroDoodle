# 🧠🎨 NeuroDoodle

**NeuroDoodle** is a lightweight AI-powered web app that allows users to draw doodles on a canvas and instantly get real-time classification results using a fine-tuned deep learning model.

---

## Live Demo

🔗 [Web App](https://your-app-link.com)  

![Demo Image](asset/demo_image.png)

---

## About the AI

The AI model behind NeuroDoodle is a **Vision Transformer (ViT)** that was fine-tuned on a subset of the [Quick, Draw! Dataset](https://github.com/googlecreativelab/quickdraw-dataset). The dataset contains millions of user-drawn doodles across various categories. The model has been trained to recognize common doodle patterns with high accuracy.

---

## Getting Started

Follow these steps to run **NeuroDoodle** locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aniketmishr/NeuroDoodle.git

cd NeuroDoodle
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download the Model Weights

```bash
python download_weight.py
```

### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## How It Works ? 

- Draw a doodle of any object on the left-side canvas.
- NeuroDoodle uses the fine-tuned ViT model to classify your drawing.
- The prediction appears instantly on the right side.

---
