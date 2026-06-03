<div align="center">

# 🎯 SSC CGL Mock Test Simulator

### A real exam-day interface for SSC aspirants — Tier-wise patterns, sectional timing & live scoring.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Open_App-1e3a8a?style=for-the-badge)](https://anubhav-kaushik.github.io/quizzes/)
[![Made With](https://img.shields.io/badge/Made_with-HTML%20%7C%20CSS%20%7C%20JS-f97316?style=for-the-badge)](https://anubhav-kaushik.github.io/quizzes/)
[![Hosted On](https://img.shields.io/badge/Hosted_on-GitHub_Pages-181717?style=for-the-badge&logo=github)](https://pages.github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-16a34a?style=for-the-badge)](#-license)

**🔗 Live App → https://anubhav-kaushik.github.io/quizzes/**

</div>

---

## ✨ Overview

The **SSC CGL Mock Test Simulator** is a free, browser-based practice platform that recreates the actual **SSC (Staff Selection Commission) CGL exam interface** — complete with sectional timers, a NTA/SSC-style question palette, mark-for-review workflow, sectional locking, and an auto-scored result dashboard.

Built with vanilla **HTML, CSS, and JavaScript** — no frameworks, no backend, no tracking. Just open the link and start practicing.

> 🇮🇳 Designed for serious **SSC CGL Tier-I and Tier-II aspirants** preparing for one of India's most competitive government exams.

---

## 🚀 Features

### 📋 Real Exam Interface
- **Authentic SSC layout** with navy + saffron theme matching the official portal
- **Live countdown timer** with color-coded warnings (green → amber → red)
- **Candidate header bar** with section progress indicator
- **Fullscreen mode** for distraction-free practice

### 🧭 Question Navigation
- **NTA-style question palette** with five color-coded states:
  - 🟢 **Answered** &nbsp; 🔴 **Not Answered** &nbsp; ⚪ **Not Visited** &nbsp; 🟣 **Marked for Review** &nbsp; 🟦 **Answered & Marked**
- **Save & Next**, **Previous**, **Mark for Review**, and **Clear Response** controls
- **Section tabs** with lock icons — *you cannot jump sections until the current one is locked or its timer expires* (just like the real exam!)

### ⏱️ Sectional Timer & Locking
- Each section has its own **independent timer** (e.g., 15 min × 4 sections for Tier-I)
- Sections **auto-lock** when their time runs out
- Once locked, a section **cannot be revisited** — enforcing real exam discipline
- Confirmation modals show live stats (answered / unanswered) before locking or submitting

### 📊 Dynamic Instructions
- Instructions box updates **automatically based on the selected paper's `exam_level`** (Tier-I, Tier-II, etc.)
- Live summary of total sections, total questions, total time, and per-section marking scheme
- Tier-specific descriptions (objective screening, descriptive, DEST/CPT, etc.)

### 📈 Auto-Scored Result Analysis
- **Net Score** computed per official SSC marking rules (+2 / −0.5 for Tier-I)
- **Per-section breakdown** with correct, incorrect, skipped & sectional score
- **Accuracy %** based on attempted questions
- **Print-friendly report** for offline review or sharing

### 📱 Fully Responsive
- **Desktop:** Two-column layout with sticky palette sidebar
- **Tablet:** Single-column flow with palette below the question
- **Mobile:** Bottom-sheet drawer palette accessible via a floating **"Palette" FAB**
- Optimized touch targets, swipeable section tabs, and stacked footer buttons on phones
- 🖨️ **Print-optimized** result report

### 🗂️ Real Question Bank
The simulator ships with question sets compiled from previous-year SSC papers, including:
- **CGL 2025 Tier-I** (Sept 2025 shifts)
- **CGL 2024 Tier-I** (Sept 2024 shifts)
- **CGL 2023 Tier-I** (July 2023 shifts)
- **CGL 2022 Tier-II** (March 2023)
- **CGL 2014 Tier-I** (October 2014 shifts)

---

## 🖥️ Live Demo

Open the simulator directly in your browser — **no installation, no signup**:

👉 **https://anubhav-kaushik.github.io/quizzes/**

Works seamlessly on Chrome, Firefox, Safari, Edge, and mobile browsers.

---

## 🎮 How to Use

1. **Open the live link** → https://anubhav-kaushik.github.io/quizzes/
2. **Pick a mock paper** from the dropdown (sorted by exam year and date).
3. **Read the auto-generated instructions** — sections, timing, marking will appear based on the chosen paper's tier.
4. **Tick the declaration checkbox** to acknowledge exam discipline.
5. Click **🚀 Start Mock Test**.
6. Inside the exam:
   - Select an option → click **Save & Next**
   - Use **Mark for Review** to revisit later
   - Tap the **palette** to jump between questions within the current section
   - Click **🔒 Lock Section & Continue** to move forward (or wait for timer)
7. After all sections are complete, hit **✅ Submit Full Test** to view your scorecard.
8. Optionally **🖨️ Print** the result report or **🔁 Take Another Test**.

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
| **Markup** | HTML5 |
| **Styling** | CSS3 (custom design system, CSS variables, responsive media queries) |
| **Logic** | Vanilla JavaScript (ES6+) — no frameworks |
| **Fonts** | [Inter](https://fonts.google.com/specimen/Inter) + [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) |
| **Data** | Plain JS object in `data.js` (`EXAM_DATABASE`, `EXAM_SCHEMA`) |
| **Hosting** | GitHub Pages |

> ⚡ **Zero dependencies.** The entire app is a single HTML file + one data file. Loads in milliseconds, works offline once cached.

---

## 📂 Project Structure

```
quizzes/
├── index.html          # The full exam simulator UI + logic
├── data.js             # EXAM_DATABASE (question bank) + EXAM_SCHEMA (rules)
└── README.md           # You are here
```

### `data.js` Schema

```js
const EXAM_SCHEMA = {
  exam_level: {
    "Tier-I": {
      sections: {
        "General Intelligence and Reasoning": {
          time_allotted: 15,
          marking_schema: { correct: 2, incorrect: -0.5, unattempted: 0 }
        },
        // ...other sections
      }
    },
    "Tier-II": { /* ... */ }
  }
};

const EXAM_DATABASE = {
  "cgl_2025_tier1_12_09": {
    title: "Combined Graduate Level Examination 2025 Tier I",
    exam_level: "Tier-I",
    exam_date: "12.09.2025",
    questions: [
      {
        id: 1,
        section: "General Intelligence and Reasoning",
        question: "...",
        options: ["...", "...", "...", "..."],
        correct_answer: "..."
      }
      // ...100 questions
    ]
  }
  // ...more papers
};
```

---

## 💻 Run Locally

```bash
# Clone the repo
git clone https://github.com/anubhav-kaushik/quizzes.git
cd quizzes

# Just open index.html in your browser — no build step required
# (Or use a tiny local server)
python3 -m http.server 8080
# Then visit http://localhost:8080
```

---

## 🤝 Contributing

Contributions are warmly welcomed! 🎉 Here's how you can help:

- 📝 **Add more papers** to `data.js` (previous-year SSC question sets)
- 🐛 **Report bugs** or UI glitches via [Issues](https://github.com/anubhav-kaushik/quizzes/issues)
- 💡 **Suggest features** — explanations, bookmarks, dark mode, leaderboard, etc.
- 🌐 **Translate** the interface for regional aspirants
- ⭐ **Star the repo** if it helped you prepare!

### Steps
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 🗺️ Roadmap

- [ ] 🌙 Dark mode toggle
- [ ] 📚 Solution explanations after submission
- [ ] 🔖 Bookmark questions for revision
- [ ] 📊 Historical performance tracker (localStorage)
- [ ] 🌐 Hindi & regional language UI
- [ ] 📥 Downloadable PDF reports
- [ ] 🎯 Tier-II calculator paper support
- [ ] 🏆 Leaderboard with anonymous IDs

---

## 📜 License

This project is open-sourced under the **MIT License**. Feel free to fork, modify, and use it for your own preparation portal — a credit back is always appreciated. ❤️

---

## 👨‍💻 Developer

<div align="center">

### Designed & Developed with ❤ by **Anubhav Sharma**

*An effort to give SSC aspirants a free, ad-free, distraction-free mock test platform.*

[![GitHub](https://img.shields.io/badge/GitHub-anubhav--kaushik-181717?style=for-the-badge&logo=github)](https://github.com/anubhav-kaushik)

</div>

---

## 🙏 Acknowledgements

- 🇮🇳 **Staff Selection Commission (SSC)** for the official exam patterns used as inspiration
- 📚 **SSC aspirants community** for years of shared question banks and study material
- ✍️ **Open-source community** for the fonts, color palette inspiration, and design principles

---

## ⚠️ Disclaimer

> This simulator is an **independent, unofficial practice tool** for educational purposes only. It is **not affiliated with, endorsed by, or sponsored by** the Staff Selection Commission (SSC) or the Government of India. Question data is compiled from publicly available previous-year papers for revision purposes. For official information, always refer to **[ssc.gov.in](https://ssc.gov.in)**.

---

<div align="center">

### ⭐ If this project helped your preparation, please consider giving it a star!

**Best of luck for your SSC journey, future officer! 🇮🇳**

</div>
