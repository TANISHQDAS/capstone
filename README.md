# Meeting Intelligence Agent (Beginner-Friendly Version)

> **A Simple, Easy-to-Understand AI Agent for Meeting Audio & Task Automation**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

The **Meeting Intelligence Agent** turns meeting audio into actionable tasks. It processes unstructured speech, extracts action items (Task, Assignee, Due Date), and creates tickets in your task management tool.

---

## 🎯 How It Works in 3 Simple Steps

1. 🎙️ **Step 1: Audio Input**: Upload meeting audio or paste transcript text.
2. 🧠 **Step 2: AI Task Extraction**: AI identifies tasks, owners, and due dates.
3. 📝 **Step 3: Ticket Creation**: The agent creates and verifies task tickets in your task tool (e.g. Linear).

---

## 👥 5-Person Team Work Division

| Member ID | Role | Primary Focus | Assigned Lead |
|---|---|---|---|
| **Member 1** | Audio & Speech | Audio file ingestion and transcript formatting | `[ Unassigned ]` |
| **Member 2** | AI Task Extractor | LLM prompt setup for task extraction | `[ Unassigned ]` |
| **Member 3** | Data Storage | Saving meetings and tasks to database | `[ Unassigned ]` |
| **Member 4** | Task Integration | Connecting to Linear task manager | `[ Unassigned ]` |
| **Member 5** | Web Interface | Building simple light mode UI and Vercel hosting | `[ Unassigned ]` |

---

## 🚀 Running the Project (Beginner Guide)

### 1. Run the Python Backend
```bash
cd backend
python -m venv venv
# Windows:
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open `http://localhost:8000/docs` in your browser to test the API endpoints directly!

### 2. Run the Web Dashboard
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:3000` to interact with the beginner-friendly web UI.

---

## 🌐 Deploy to Vercel
Deploy the project to Vercel with a single command:
```bash
vercel
```
Configured via `vercel.json`.
