# Quick Start Guide

## Method 1: Simple Python Launcher (Recommended)

```bash
python run.py
```

## Method 2: Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run src\streamlit_app.py
```

## Method 3: One-liner for Unix/Linux/Mac

```bash
pip install -r requirements.txt && streamlit run src\streamlit_app.py
```

## Method 4: Windows PowerShell One-liner

```powershell
pip install -r requirements.txt; streamlit run src\streamlit_app.py
```

## Troubleshooting

### Python Not Found

- Install Python 3.8+ from [python.org](https://python.org)
- Make sure Python is added to PATH

### Permission Errors

```bash
# Use user installation
pip install --user -r requirements.txt
```

### Port Already in Use

```bash
# Use different port
streamlit run src\streamlit_app.py --server.port 8502
```

### Module Not Found

```bash
# Upgrade pip first
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 50MB for application + dataset
- **Browser**: Chrome, Firefox, Safari, or Edge
