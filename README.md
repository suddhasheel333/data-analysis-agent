# AI Data Analysis Agent

An end-to-end AI-powered data analysis web app built with Python and Streamlit.

## What it does
- Loads any CSV into a Pandas DataFrame
- Converts data into a SQLite database and runs SQL queries
- Auto-generates summary statistics and detects column types
- Sends data summary to Groq (LLaMA 3.3) and generates 5 key insights
- Visualizes data with bar charts, pie charts, and trend lines

## Tech Stack
- Python
- Pandas + SQLite
- Groq API (LLaMA 3.3-70b)
- Matplotlib + Seaborn
- Streamlit

## How to run
1. Clone the repo
2. Install dependencies
   pip install -r requirements.txt
3. Add your Groq API key to a .env file
   GROQ_API_KEY=your_key_here
4. Run the app
   streamlit run app.py