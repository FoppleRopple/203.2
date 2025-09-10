import random
import datetime
 
class HealthMetric:
    def __init__(self, name, unit, value):
        self.name = name
        self.unit = unit
        self.value = value
        self.history = [(datetime.date.today(), value)]
 
    def update_value(self, new_value):
        self.value = new_value
        self.history.append((datetime.date.today(), new_value))
 
    def show_trend(self):
        print(f"\nTrend for {self.name}:")
        for date, val in self.history:
            print(f"  {date}: {val}{self.unit}")
 
 
class HealthTrackApp:
    def __init__(self):
        self.metrics = {
            "Heart Rate": HealthMetric("Heart Rate", " bpm", 72),
            "Blood Pressure": HealthMetric("Blood Pressure", " mmHg", "120/80"),
            "Blood Glucose": HealthMetric("Blood Glucose", " mg/dL", 95),
            "Sleep Hours": HealthMetric("Sleep Hours", " hrs", 7),
            "Calories": HealthMetric("Calories", " kcal", 2000),
            "Medication Taken": HealthMetric("Medication Taken", "", "Yes")
        }
        self.alert_thresholds = {
            "Heart Rate": (50, 100),
            "Blood Glucose": (70, 140)
        }
 
    def dashboard(self):
        print("\n===== USER DASHBOARD =====")
        for metric in self.metrics.values():
            print(f"{metric.name}: {metric.value}{metric.unit}")
        print("==========================")
 
    def track_metric(self):
        print("\nWhich metric would you like to update?")
        for i, key in enumerate(self.metrics.keys(), 1):
            print(f"{i}. {key}")
        choice = int(input("Enter choice: "))
        metric_name = list(self.metrics.keys())[choice - 1]
        new_value = input(f"Enter new value for {metric_name}: ")
        self.metrics[metric_name].update_value(new_value)
        print(f"{metric_name} updated successfully!")
 
    def view_trends(self):
        for metric in self.metrics.values():
            metric.show_trend()
 
    def simulate_real_time(self):
        print("\nSimulating real-time data updates...")
        for name, metric in self.metrics.items():
            if isinstance(metric.value, (int, float)):
                new_val = random.randint(40, 150)
                metric.update_value(new_val)
                if name in self.alert_thresholds:
                    low, high = self.alert_thresholds[name]
                    if new_val < low or new_val > high:
                        print(f"ALERT: {name} at {new_val}{metric.unit} is out of safe range!")
        print("Real-time simulation complete.")
 
    def share_data(self):
        print("\nExporting health report...")
        filename = "health_report.txt"
        with open(filename, "w") as file:
            file.write("HEALTHTRACK REPORT\n")
            file.write("=================\n")
            for metric in self.metrics.values():
                file.write(f"{metric.name}: {metric.value}{metric.unit}\n")
        print(f"Report saved as {filename}. Share with provider securely.")
 
    def main_menu(self):
        while True:
            print("\n===== HEALTH TRACK MENU =====")
            print("1. View Dashboard")
            print("2. Update Health Metric")
            print("3. View Trends")
            print("4. Simulate Real-Time Data & Alerts")
            print("5. Share Data with Provider")
            print("6. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.dashboard()
            elif choice == "2":
                self.track_metric()
            elif choice == "3":
                self.view_trends()
            elif choice == "4":
                self.simulate_real_time()
            elif choice == "5":
                self.share_data()
            elif choice == "6":
                print("Exiting HealthTrack Prototype...")
                break
            else:
                print("Invalid choice. Please try again.")
 
 
if __name__ == "__main__":
    app = HealthTrackApp()
    app.main_menu()
