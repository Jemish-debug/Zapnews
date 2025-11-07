# ZapNews

A personalized news aggregation platform that curates and displays articles based on user-selected interests. ZapNews focuses on *relevance over overload* by filtering content from multiple RSS news sources and presenting it in an organized, user-friendly interface.

---

## 🌟 Key Features
- **Personalized Feeds:** Users receive news based on their chosen categories.
- **Real-Time Aggregation:** Fetches the latest articles from multiple RSS feeds.
- **Clean & Responsive UI:** Clear, structured layout for easy browsing.
- **Scalable Backend:** Built for future expansion and intelligent recommendation systems.

---

## 🛠️ Tech Stack
| Layer | Technologies |
|------|--------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS |
| Database | MySQL |
| Data Source | RSS Feed Integration |

---

## 🧭 System Architecture

```mermaid
graph TD;
    User(User) --> UI[Frontend (HTML/CSS)]
    UI --> Flask[Flask Backend]
    Flask --> DB[(MySQL Database)]
    Flask --> RSS[RSS News Sources]
    RSS --> Flask
```

The workflow follows:
1. User interacts with the UI to select news categories.
2. The system gathers articles from various RSS providers.
3. Content is filtered and stored/retrieved from MySQL.
4. Results are displayed to the user in a clean, organized layout.

---

## 📦 Installation & Setup
```bash
# Clone the repository
git clone <repository-url>
cd zapnews

# Install dependencies
pip install -r requirements.txt

# Configure your MySQL database in the application config

# Run the application
flask run
```

---

## 🚀 Future Enhancements
- **AI-based Recommendation System** for improved personalization
- **NLP-powered Article Classification**
- **Switch to API-based News Sources** for reliability and scalability

---

## 👥 Contributors
- **Jemish Koladiya** – Backend & System Design
- **Collaborators & Reviewers**

---

## 📄 License
This project is licensed under the **MIT License**. Feel free to modify and build upon it.
