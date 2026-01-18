def analyze_log_file(file_path):
    error_count = 0
    failed_login_count = 0
    ip_counter = {}

    error_codes = ["400", "401", "403", "404", "500"]
    failed_login_codes = ["401", "403"]

    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.split()

                # Extract IP address (first element)
                ip = parts[0]

                # Count IP frequency
                if ip in ip_counter:
                    ip_counter[ip] += 1
                else:
                    ip_counter[ip] = 1

                # Check for error codes
                for code in error_codes:
                    if code in line:
                        error_count += 1
                        break

                # Check for failed login attempts
                for code in failed_login_codes:
                    if code in line:
                        failed_login_count += 1
                        break

        # Find most frequent IP
        most_frequent_ip = max(ip_counter, key=ip_counter.get)

        print("\n LOG FILE ANALYSIS REPORT")
        print("-" * 30)
        print(f"Total Errors Found       : {error_count}")
        print(f"Failed Login Attempts    : {failed_login_count}")
        print(
            f"Most Frequent IP Address : {most_frequent_ip} "
            f"({ip_counter[most_frequent_ip]} times)"
        )

    except FileNotFoundError:
        print(" Error: Log file not found. Please check the file path.")
    except Exception as e:
        print(f" Unexpected error occurred: {e}")


# Run the analyzer
analyze_log_file("server.log")
