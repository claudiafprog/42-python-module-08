# The Matrix — Welcome to the Real World of Data Engineering

Master virtual environments, dual dependency management (`pip` vs. `Poetry`), and multi-environment configuration (`.env` & secret safety) for resilient data pipelines.

---

## 📁 Repository Structure

```text
├── ex0/
│   └── construct.py           # Virtual environment inspector & guide
├── ex1/
│   ├── loading.py             # NumPy/Pandas/Matplotlib Matrix analyzer
│   ├── requirements.txt       # Pip dependency manifest
│   └── pyproject.toml         # Poetry project & dependency metadata
└── ex2/
    ├── oracle.py              # Dev/Prod configuration & security checker
    ├── requirements.txt       # Python-dotenv manifest
    ├── .env.example           # Config template
    └── .gitignore             # Secrets & environment isolation guard
```

# 🛠️ General Rules & Requirements

* Python: 3.10+Standards: flake8 + mypy typed (Note: import-related lint exceptions are permitted in ex1 per spec).
* Safety: Defensive exception handling for missing packages/configs.
* Exclusions: Never commit virtual environments or real .env secrets.

## 📦 Exercise Breakdown

Exercise 0: Entering the Matrix (ex0/construct.py)
* Core Concept: Environment isolation and path inspection.
* Key Actions: Detects global vs. venv interpreter, extracts site-packages location, and outputs CLI activation snippets for Unix/Windows when plugged into the global grid.

Exercise 1: Loading Programs (ex1/)
* Core Concept: NumPy data simulation (1000 points), Pandas manipulation, Matplotlib visualization (matrix_analysis.png), and package comparison across pip and Poetry.
* Key Actions: Gracefully catches missing dependencies and reports installed version matrices.

Exercise 2: Accessing the Mainframe (ex2/)
* Core Concept: Hierarchical configuration management (os.environ $\ge$ .env $\ge$ defaults) using python-dotenv.
* Variables Tracked: MATRIX_MODE (development/production), DATABASE_URL, API_KEY, LOG_LEVEL, ZION_ENDPOINT. Validates zero hardcoded secrets and visualizes dev/prod behavioral shifts.

# 🚀 Quick Start / Verification

```bash
# --- Exercise 0 ---
python3 ex0/construct.py
python3 -m venv matrix_env
source matrix_env/bin/activate  # (Windows: matrix_env\Scripts\activate)
python3 ex0/construct.py

# --- Exercise 1 ---
python3 ex1/loading.py          # Test missing dependency warning
pip install -r ex1/requirements.txt
python3 ex1/loading.py          # Run pip analysis

# Optional Poetry test
cd ex1 && poetry install && poetry run python loading.py && cd ..

# --- Exercise 2 ---
cp ex2/.env.example ex2/.env
python3 ex2/oracle.py
MATRIX_MODE=production API_KEY=override_secret python3 ex2/oracle.py
```
