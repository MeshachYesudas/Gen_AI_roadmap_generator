# Gen_AI_roadmap_generator
# 🛣️ Roadmap Generation using LLaMA-2 & Streamlit

This project is a GenAI-powered **Roadmap Generator** designed to help users master any skill by generating personalized, step-by-step learning paths along with curated free resources.

---

## 🔍 Scenario

A user enters a **desired skill** into the **Roadmapper** web application. The application uses the **LLaMA-2 language model** to generate a personalized learning roadmap. Users receive detailed steps and relevant free resources to guide their learning journey toward proficiency.

---

## 🔁 Project Flow

1. Users interact with the web UI by entering their learning goal (e.g., "Learn Python").
2. Streamlit captures this input and sends it to the backend.
3. Input is passed to a **LLaMA-2 pre-trained model** via the **CTransformers** interface.
4. LLaMA-2 processes the prompt and returns a structured roadmap.
5. The generated output is rendered in the Streamlit web app for the user to follow.

---

## ✅ Milestones & Tasks

To accomplish this project, the following tasks must be completed:

- 🔹 Getting the LLaMA-2 Model
- 🔹 Downloading and saving the model inside the `model/` folder
- 🔹 Interfacing with the pre-trained model using CTransformers
- 🔹 Designing prompt templates
- 🔹 Generating GenAI responses from the model
- 🔹 Deploying the model and integrating it with the Streamlit app
- 🔹 Building a clean, responsive UI

---

## 📁 Project Structure

roadmap-generator/
├── app.py # Main Streamlit application
├── model/ # Folder containing the LLaMA-2 model files
├── requirements.txt # Python dependencies
├── .env # Environment variables (if any)
└── README.md # Project documentation

## 📚 Prior Knowledge Required

Before diving into the project, familiarity with the following technologies is highly recommended:

- 🧠 [Prompt Engineering Basics](https://www.mygreatlearning.com/blog/prompt-engineering-complete-guide/)
- 🔗 [Langchain](https://python.langchain.com/v0.2/docs/tutorials/)
- 🦙 [LLaMA-2 (GGML format)](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
- 🌐 [Streamlit](https://docs.streamlit.io/)

---

## ⚙️ How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/roadmap-generator.git
   cd roadmap-generator
Install Dependencies

pip install -r requirements.txt
Download LLaMA-2 Model

Download the .bin file from HuggingFace:
LLaMA-2-7B-Chat-GGML

Place the model file inside the model/ folder.

Run the App

streamlit run app.py
