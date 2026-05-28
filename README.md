# RetailPulse

RetailPulse is a compact analytics toolkit for retail data: sales analytics, customer
segmentation, demand forecasting, churn analysis and inventory optimization. It
ties together data preparation utilities, interactive pages, simple models and
notebooks so you can reproduce analyses or use parts as a starting point for
production workflows.

Why this project exists
- Provide repeatable notebooks and scripts for common retail analytics tasks
- Separate data preparation from modeling so experiments are easy to reproduce
- Keep the codebase lightweight so it can be shared without large raw datasets

Quick start
1. Create a Python virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate     # Windows
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Notes about data and models
- The repository intentionally excludes raw datasets and large model artifacts.
  See the `data/` and `models/` folders for placeholders. To reproduce the
  analyses you'll need to obtain the raw data (e.g., `online_retail_II.csv`) and
  place it in `data/raw/` before running the data preparation steps.
- If you want to include model artifacts, move them into `models/` and update
  the README or scripts with the paths you used.

Repository layout
- `app.py` — small entry point used by the interactive pages
- `requirements.txt` — Python dependencies
- `data/` — data inputs and processing outputs (raw and processed data are
  excluded from the GitHub push by default; see `.gitignore`)
- `models/` — model artifacts (generally excluded by default to avoid large
  binary files)
- `notebooks/` — exploratory notebooks (week_1.ipynb, week_2.ipynb)
- `pages/` — analysis scripts / Dash / Streamlit pages
- `utils/` — helper functions: `data_loader.py`, `ui.py`

Common tasks
- Prepare data: use the scripts inside `utils/` and the notebooks in `notebooks/`.
- Run analysis pages: `python app.py` (follow the specific page's instructions).


Contact
If you have questions or want to collaborate, open an issue or reach out.
