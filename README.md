# Project 3 — Web Traffic Analytics

## Deliverables
- `app.py` — interactive Streamlit dashboard
- `Web_Traffic_Analytics.ipynb` — analysis notebook
- `src/analysis.py` — reusable analysis functions
- `data/web_traffic_sessions.csv` — 5,000 synthetic sessions
- `data/page_path_events.csv` — session page-path events
- `data/data_dictionary.csv` — field definitions
- `outputs/project_report.md` — findings and recommendations
- `requirements.txt` — dependencies

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Notebook
```bash
jupyter notebook Web_Traffic_Analytics.ipynb
```

## Dataset note
The included files are synthetic Google Analytics-style data created for demonstration. For a real project, replace them with a GA4 export mapped to the same fields.

## Analysis covered
Bounce rate, top pages, traffic sources, sessions, engagement, funnel conversion, page paths, device performance, monthly trends and UX/conversion recommendations.
