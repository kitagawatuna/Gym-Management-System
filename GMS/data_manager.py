import json
import csv
import os

class DataManager:
    def __init__(self):
        self.ensure_file("equipment.json", [])
        self.ensure_file("trainers.json", [])
        self.ensure_file("packages.json", [])
        self.ensure_file("members.json", [])
        self.ensure_file("subscriptions.json", [])
        self.ensure_file("attendance.csv", [])

    def ensure_file(self, filename, default_content):
        if not os.path.exists(filename):
            if filename.endswith(".json"):
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(default_content, f, indent=4)
            elif filename.endswith(".csv"):
                with open(filename, "w", newline='', encoding="utf-8") as f:
                    f.write("member_id,date,status\n")

    def save_json(self, data, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_json(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def save_csv(self, filename, fieldnames, rows):
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def load_csv(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return list(reader)
        except:
            return []
