# 🛫 History of All Flight Crash Map — Contribution Guidelines  

Welcome to the **History of All Flight Crash Map Project!** ✈️  
This project visualizes **global flight crash data (1908–2022)** through interactive and informative maps. Originally developed as a **Streamlit dashboard**, this project is now evolving into a **fully static HTML + CSS + JS website**, hosted on **Vercel**, making it lightweight, responsive, and easily deployable.  

This repository is maintained under the **Winter of Social Courses (WOSC)** initiative, where contributors collaborate to create socially impactful open-source projects.  

---

## 📘 Project Overview  

The **Flight Crash Map** provides a comprehensive and visually interactive representation of flight accidents throughout history. The original repository ([vinaysingh282006/History-of-all-flight-crash-map](https://github.com/vinaysingh282006/History-of-all-flight-crash-map)) used **Streamlit**, **Plotly**, and **Folium** to display crash data dynamically.  

We are now transitioning to a **static website model** that provides similar features — but faster, more portable, and deployable via **Vercel** for seamless public access.  

### 🔍 Key Objectives  

1. Convert the Streamlit-based map visualization into a **static HTML/JS web interface**.  
2. Create a **responsive and modern UI** compatible with mobile and desktop.  
3. Host the final version on **Vercel** with automatic deployments from GitHub.  
4. Allow contributors to easily **extend or improve** both the dataset and visualization logic.  
5. Improve documentation and contributor onboarding for easier collaboration.  

---

## 🌍 Features (Current and Planned)  

### ✅ Existing Features (From Original Repo)
- Flight crash data covering **1908–2022**.  
- Interactive map visualizations with **location markers** and crash summaries.  
- Data loaded from CSV/JSON sources.  
- Streamlit dashboard with Plotly charts.  

### 🚀 New Additions (Static Site)
- Fully static **index.html** with embedded **Leaflet.js or Mapbox** map.  
- **Dynamic filtering**: by year, airline, aircraft type, and region.  
- **Search functionality** for quick access to specific crashes.  
- **About** and **Data Insight** pages with background info and statistics.  
- **Dark/Light mode toggle** for accessibility.  
- Optimized **loading performance** via lazy data loading.  

---

## 🧩 Repository Structure  

```
History-of-all-flight-crash-map/
│
├── public/
│   ├── index.html              # Main page for the interactive map
│   ├── about.html              # About the project & data sources
│   ├── styles/
│   │   └── main.css            # Core styling for layout, colors, fonts
│   ├── scripts/
│   │   ├── map.js              # Handles map initialization and rendering
│   │   ├── filters.js          # Controls for search/filter options
│   │   └── ui.js               # Manages dynamic DOM updates
│   └── assets/
│       ├── icons/              # Custom map icons, markers, etc.
│       └── images/             # Screenshots, logos, and visuals
│
├── data/
│   ├── flight_crashes.csv      # Original dataset (1908–2022)
│   └── flight_crashes.json     # Processed JSON for web use
│
├── build/
│   └── process_data.py         # Preprocessing script to convert CSV → JSON
│
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow for Vercel deployment
│
├── LICENSE                     # MIT License for open-source usage
├── README.md                   # Project overview
└── CONTRIBUTING.md              # This contribution guideline
```

---

## 🛠️ Getting Started  

### 1️⃣ Fork & Clone the Repository  
```bash
git clone https://github.com/<your-username>/History-of-all-flight-crash-map.git
cd History-of-all-flight-crash-map
```

### 2️⃣ Create a New Branch  
```bash
git checkout -b feature/your-feature-name
```

### 3️⃣ Set Up Your Local Environment  
- Install Python dependencies (if modifying backend preprocessing):  
  ```bash
  pip install -r requirements.txt
  ```
- If working on the static web version:  
  Simply open `public/index.html` in your browser to test changes.  

### 4️⃣ Make Your Changes  
- Modify **HTML**, **CSS**, or **JS** files to improve layout or functionality.  
- Update **data/** files only if needed — and document your changes clearly.  

### 5️⃣ Commit & Push  
```bash
git add .
git commit -m "Add: brief description of your feature"
git push origin feature/your-feature-name
```

### 6️⃣ Submit a Pull Request  
- Go to your forked repo on GitHub.  
- Click **Compare & Pull Request** → Base: `main`.  
- Clearly describe your change and why it’s beneficial.  
- Link related issues if applicable.  

---

## 📦 Deployment via Vercel  

We use **Vercel** for automatic deployment of the static site.  

### 🔧 Setup
1. Log in to [Vercel](https://vercel.com).  
2. Import the repository directly from GitHub.  
3. Set the project root to `/public`.  
4. Every merge to `main` will automatically redeploy the updated site.  

### 🧰 Optional (Manual Build)
If the dataset requires preprocessing:
```bash
python build/process_data.py
```
This will generate a fresh `flight_crashes.json` file for your static map.

---

## 🧾 Contribution Guidelines  

To maintain a clean and scalable project:  

### 💡 Code Quality  
- Use **consistent indentation (2 spaces for JS, 4 for Python)**.  
- Add comments explaining key logic.  
- Prefer modular code — separate JS into logical files (`map.js`, `filters.js`, etc.).  

### 🧰 Commit Message Format  
```
Add: Short description of feature
Fix: Short description of fix
Update: Short description of improvement
Docs: Updated documentation
```

### 🧱 Pull Requests  
- Keep PRs focused and small.  
- Reference the issue number in the PR body (e.g., "Fixes #12").  
- Ensure there are **no console errors** in browser tests.  

---

## 🧭 Roadmap  

| Feature | Description | Status |
|----------|--------------|--------|
| Static HTML Conversion | Convert Streamlit UI into static web pages | 🟢 In Progress |
| Map Visualization | Implement Leaflet.js map for crash locations | 🟢 In Progress |
| Year & Airline Filters | Add filter dropdowns and sliders | 🟡 Planned |
| Dark/Light Mode | Theme toggle for accessibility | 🟡 Planned |
| Vercel Auto Deploy | Continuous deployment via GitHub Actions | 🟢 In Progress |
| Data Analytics | Add overview charts (fatalities per year, etc.) | 🟠 Planned |
| Mobile Optimization | Improve responsive layout for phones/tablets | 🔵 Planned |
| Docs & Wiki | Detailed usage guide for contributors | 🟡 In Progress |

---

## 🌟 Contributors  

A huge thank you to all contributors who make this project possible!  

| Name | Role | Contribution |
|------|------|---------------|
| **Subramaniam** | 🧑‍💻 Project Admin | Project Lead & Core Developer |
| **Vinay Kumar Singh** | 💻 Founder | Original Repository Author |
| *You?* | 🌍 Contributor | Add your feature, fix, or documentation! |

To get featured in this table, contribute and open your first pull request! 🎉  

---

## 💬 Communication  

If you have questions, ideas, or suggestions:  
- Open a **GitHub Issue** for bugs or new features.  
- Use **GitHub Discussions** for general questions and brainstorming.  
- Stay respectful, inclusive, and professional — we welcome all contributors!  

---

## 📄 License  

This project is licensed under the **MIT License**, meaning you can freely use, modify, and distribute the code with proper attribution.  
See the [LICENSE](LICENSE) file for full details.  

---

## ✈️ Final Note  

This project combines **data science**, **frontend design**, and **open-source collaboration** to bring awareness to aviation safety history.  
Your contributions — big or small — make a difference.  

Let’s build something that **educates, informs, and inspires**. 🌍  
Thank you for being part of this journey! 💙  

---
