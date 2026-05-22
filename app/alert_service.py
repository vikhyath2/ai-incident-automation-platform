def send_alert(incident: dict):

    print("\n🚨 CRITICAL INCIDENT ALERT 🚨")

    print(f"Issue Summary: {incident.get('issue_summary')}")
    print(f"Root Cause: {incident.get('root_cause')}")
    print(f"Severity: {incident.get('severity')}")
    print(f"Suggested Fix: {incident.get('suggested_fix')}")
    print(f"Next Action: {incident.get('next_action')}")

    print("🚨 ALERT SENT SUCCESSFULLY 🚨\n")