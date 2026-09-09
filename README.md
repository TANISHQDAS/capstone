# Meeting Intelligence Agent (Unified Single-Deployment Version)

> **Full-Stack Next.js Application with Built-in API Routes & Vercel Hosting**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

The **Meeting Intelligence Agent** turns meeting audio & speech into verified task tickets. Both the web interface and the API backend are combined into **ONE single Next.js project** for instant, 1-click deployment on Vercel.

---

## 🎯 How It Works in 3 Simple Steps

1. 🎙️ **Step 1: Speech Transcript**: Input what people said in the meeting.
2. 🧠 **Step 2: AI Reads Tasks**: AI identifies tasks, responsible person, and due date.
3. 📝 **Step 3: Create Ticket**: Automatically creates and verifies task tickets in Linear.

---

## 🌐 Built-in API Routes (Single Deployment)

No separate backend server needed! All API endpoints run directly inside Next.js:

- `POST /api/extract-tasks`: Extracts action items from meeting transcripts.
- `POST /api/create-ticket`: Creates and verifies Linear tickets.
- `GET /api/download-pdf`: Serves meeting summary report.

---

## 👥 5-Person Team Work Division

| Member ID | Role | Primary Focus | Assigned Lead |
|---|---|---|---|
| **Member 1** | Audio & Speech | Audio input and transcript formatting | `[ Unassigned ]` |
| **Member 2** | AI Task Extractor | LLM prompt setup for task extraction | `[ Unassigned ]` |
| **Member 3** | Data Storage | Saving meetings and tasks to storage | `[ Unassigned ]` |
| **Member 4** | Task Integration | Connecting to Linear task manager | `[ Unassigned ]` |
| **Member 5** | Web Interface & API | Next.js UI, API routes, and Vercel hosting | `[ Unassigned ]` |

---

## 🚀 One-Click Vercel Deployment

```bash
# Deploy to Vercel
vercel
```
Configured via `vercel.json` with standard Next.js App Router optimization.
