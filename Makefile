setup:
	python3 -m pip install -r requirements.txt

pipeline:
	python3 load_data.py
	python3 analyze_data.py

dashboard:
	python3 -m streamlit run dashboard.py