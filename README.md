
```markdown
# 🏎️ F1 Strategy Analytics

A data-driven Formula 1 analytics project that extracts race insights using the OpenF1 API.  
This project focuses on analyzing race performance, position changes, and tyre strategies to simulate real-world race strategy analysis.

---

## 🚀 Features

- 📊 **Performance Analysis**
  - Average pace (lap time)
  - Driver consistency (variance)

- 📈 **Race Progression**
  - Position changes over time
  - Positions gained/lost analysis

- 🛞 **Tyre Strategy Analysis**
  - Stint breakdown (compound, lap range)
  - Strategy storytelling in plain English
  - Strategy comparison across drivers

- 📉 **Visualizations**
  - Position trend chart with tyre overlays
  - Tyre strategy timeline (intuitive & non-technical friendly)

- 👥 **Single & Multi Driver Mode**
  - Analyze one driver in detail
  - Compare multiple drivers side-by-side

---

## 🧠 Example Insight

> Charles Leclerc started strongly on soft tyres and switched to hard tyres for the majority of the race. Despite a stable strategy, his position dropped significantly in the later stages, suggesting performance or reliability issues rather than strategy inefficiency.

---

## 🛠️ Tech Stack

- Python
- Pandas
- Matplotlib
- OpenF1 API

---

## 📂 Project Structure

```

f1-strategy-analytics/
│
├── src/
│   ├── api/
│   ├── processing/
│   ├── analysis/
│   ├── visualization/
│
├── main.py
├── requirements.txt
└── README.md

````

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
````

2. Run the project:

```bash
python main.py
```

3. Choose mode:

* `single` → analyze one driver
* `multi` → compare multiple drivers

---

## 📊 Sample Visualizations

* Position changes over race progression
* Tyre strategy timeline
* Strategy comparison across drivers

*(Add screenshots here after running your project)*

---

## ⚠️ Data Note

Position data from OpenF1 is based on telemetry snapshots rather than full lap-by-lap tracking.
As a result, race progression is approximated but still captures meaningful trends.

---

## 🔮 Future Improvements

* Web dashboard (Next.js / Streamlit)
* Interactive filters (race, driver, season)
* Multi-race comparison
* Deployment for public access

---

## 💡 Motivation

This project was built to simulate real-world Formula 1 strategy analysis using data, combining technical analytics with storytelling to make insights understandable for both technical and non-technical audiences.

---

## 👤 Author

**Danish Hariss**
Data Analytics Enthusiast

```
