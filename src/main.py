from src.graph import run_travel_planner

if __name__ == "__main__":
    query = "Plan a 2-day trip to New Delhi starting tomorrow"
    output = run_travel_planner(query)

    print("\n=== Travel Plan Output ===")
    print(output)
