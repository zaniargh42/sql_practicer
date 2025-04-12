# SQL Dialect to SQLite Runner

A Streamlit web app that allows you to input SQL in various dialects, automatically converts it to SQLite-compatible SQL, and runs it against the Chinook sample database.

![Chinook Schema](chinook_schema.png)

## Features

- 🔄 Supports multiple SQL dialects (MySQL, Postgres, TSQL, Snowflake, etc.)
- 📥 Converts to SQLite using [`sqlglot`](https://github.com/tobymao/sqlglot)
- 📊 Executes translated queries on the Chinook SQLite DB
- 🖼 Displays results in a clean, interactive table
- 🧭 Includes a schema diagram of the Chinook database

## Requirements

Install dependencies:

```bash
pip install streamlit pandas sqlglot
```

## Usage

1. Clone the repository.
2. Ensure `Chinook_Sqlite.sqlite` and `chinook_schema.png` are in the root folder.
3. Run the app:

```bash
streamlit run app.py
```

## Files

- `app.py` — Main Streamlit app
- `Chinook_Sqlite.sqlite` — SQLite database file (not included, [download here](https://github.com/lerocha/chinook-database))
- `chinook_schema.png` — Schema diagram for the Chinook database

## License

MIT

