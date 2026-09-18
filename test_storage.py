from analyzer.storage import (
    load_results,
    save_results,
    find_cached_alert
)


test_alert = {
    "threat": "Possible Brute Force Attack",
    "ip": "185.220.101.5",
    "description": "Multiple failed login attempts detected."
}


results = load_results()

print("\n===== STORAGE TEST =====")

print("Initial results:")
print(results)


cached = find_cached_alert(
    test_alert,
    results
)

print("\nCached alert:")
print(cached)


test_data = [
    test_alert
]

save_results(test_data)

print("\nResult saved successfully.")

loaded = load_results()

print("\nLoaded results:")
print(loaded)