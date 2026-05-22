import sqlite3


DB_NAME = "incidents.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_log TEXT NOT NULL,
            issue_summary TEXT,
            root_cause TEXT,
            severity TEXT,
            suggested_fix TEXT,
            next_action TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_incident(input_log: str, analysis: dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO incidents (
            input_log,
            issue_summary,
            root_cause,
            severity,
            suggested_fix,
            next_action
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        input_log,
        analysis.get("issue_summary"),
        analysis.get("root_cause"),
        analysis.get("severity"),
        analysis.get("suggested_fix"),
        analysis.get("next_action")
    ))

    conn.commit()
    conn.close()


def get_all_incidents():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            id,
            input_log,
            issue_summary,
            root_cause,
            severity,
            suggested_fix,
            next_action,
            created_at
        FROM incidents
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    incidents = []

    for row in rows:
        incidents.append({
            "id": row[0],
            "input_log": row[1],
            "issue_summary": row[2],
            "root_cause": row[3],
            "severity": row[4],
            "suggested_fix": row[5],
            "next_action": row[6],
            "created_at": row[7]
        })

    return incidents