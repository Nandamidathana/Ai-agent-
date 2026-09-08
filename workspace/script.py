# Track portfolio progress - calculate completion rate
import datetime

class PortfolioTracker:
    def __init__(self):
        self.projects = []
    
    def add_project(self, name, status="in_progress"):
        self.projects.append({
            "name": name,
            "status": status,
            "completed_at": None
        })
    
    def complete_project(self, project_name):
        # In real implementation, would update database
        print(f"✅ Completed: {project_name}")
    
    def get_completion_rate(self):
        completed = sum(1 for p in self.projects if p["status"] == "completed")
        total = len(self.projects)
        return f"{completed}/{total} projects completed ({100*completed/total:.1f}%)"

# Usage example
tracker = PortfolioTracker()
tracker.add_project("SaaS Dashboard App", "in_progress")
tracker.add_project("ML Chatbot Prototype", "in_progress")
print(tracker.get_completion_rate())