# 20240819-calculate_execution_times-gist

**Gist file**: [https://gist.github.com/rjvitorino/b0d006f34acc61a0c5dd7f926684e0fd](https://gist.github.com/rjvitorino/b0d006f34acc61a0c5dd7f926684e0fd)

**Description**: Cassidoo's interview question of the week: a function that given an array of logs, where each log consists of a function name, a timestamp, and an event (either start or end), returns the total execution time for each function

## calculate_execution_times.py

```Python
from collections import defaultdict
from typing import Dict, List


class LogEntry:
    """
    Represents a log entry for a function call.

    Attributes:
        name (str): The name of the function.
        time (int): The timestamp in milliseconds since the program started.
        event (str): The event type, either 'start' or 'end'.
    """

    def __init__(self, name: str, time: int, event: str):
        self.name = name
        self.time = time
        self.event = event


def calculate_execution_times(logs: List[LogEntry]) -> Dict[str, int]:
    """
    Calculate the total execution time for each function from the logs, handling
    cases where logs are unordered by revisiting unmatched events.

    Args:
        logs (List[LogEntry]): A list of LogEntry objects representing the function logs.

    Returns:
        Dict[str, int]: A dictionary with function names as keys and their total
                        execution time in milliseconds as values, sorted by function name.
    """
    execution_times: Dict[str, int] = defaultdict(int)
    start_times: Dict[str, int] = {}
    pending_logs: List[LogEntry] = []

    # First pass: Attempt to match start and end events
    for log in logs:
        if log.event == "start":
            start_times[log.name] = log.time
        elif log.event == "end":
            if log.name in start_times:
                execution_times[log.name] += log.time - start_times.pop(log.name)
            else:
                pending_logs.append(log)

    # Second pass: Process any remaining unmatched end events
    for log in pending_logs:
        if log.name in start_times:
            execution_times[log.name] += log.time - start_times.pop(log.name)

    # Sort the dictionary by function name and return as a regular dictionary
    return dict(sorted(execution_times.items()))


# Example usage with unsorted logs
logs_unsorted = [
    LogEntry("subTask1", 10, "end"),
    LogEntry("main", 0, "start"),
    LogEntry("subTask1", 5, "start"),
    LogEntry("main", 25, "end"),
    LogEntry("subTask2", 20, "end"),
    LogEntry("subTask2", 15, "start"),
]

result = calculate_execution_times(logs_unsorted)
print(result)  # Output: {'main': 25, 'subTask1': 5, 'subTask2': 5}

```