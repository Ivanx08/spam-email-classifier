#!/bin/bash

echo "🔧 Setting up the Spam Email Classifier project..."

# Step 1: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 2: Upgrade pip
pip install --upgrade pip

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the Streamlit app
echo "🚀 Launching the app..."
streamlit run app.py
