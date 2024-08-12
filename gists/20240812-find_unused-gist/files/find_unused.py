from collections import defaultdict
from typing import List
from typing import Set


def find_unused(lines: List[str]) -> List[str]:
    """
    Identify variables that are assigned but never used.

    Examples:
    ```find_unused(["a = 1", "b = a", "c = 2", "log(b)"])    # ["c"]```

    ```find_unused(["a = 1", "b = a", "c = 2", "log(c)"])    # ["a", "b"]```

    Args:
    lines (List[str]): A list of strings representing lines of code.

    Returns:
    List[str]: A list of unused variables.
    """
    assigned_vars: Set[str] = set()
    used_vars: Set[str] = set()
    dependencies = defaultdict(list)

    for line in map(str.strip, lines):
        if "=" in line:
            var_name, expression = map(str.strip, line.split("="))
            assigned_vars.add(var_name)
            dependencies[var_name] = [
                token for token in expression.split() if token in assigned_vars
            ]
        elif line.startswith("log("):
            used_vars.update(
                var.strip() for var in line[4:-1].split(",") if var.strip()
            )

    def propagate_usage(var: str) -> None:
        """Mark all dependencies of a used variable as used."""
        to_process = {var}

        while to_process:
            current_var = to_process.pop()
            used_vars.add(current_var)
            to_process.update(set(dependencies[current_var]) - used_vars)

    for var in used_vars.copy():
        propagate_usage(var)

    return sorted(assigned_vars - used_vars)


assert find_unused(["a = 1", "b = a", "c = 2", "log(b)"]) == ["c"]
assert find_unused(["a = 1", "b = a", "c = 2", "log(c)"]) == ["a", "b"]
assert find_unused(["x = 10", "y = x", "z = 5", "log(x)", "log(z)"]) == ["y"]
assert find_unused(["x = 10", "y = x", "z = 5", "log(y)", "log(z)"]) == []
assert find_unused(["p = 1", "q = p", "r = 2", "log(q)", "log(r)"]) == []
assert find_unused(["p = 1", "q = p", "r = 2", "log(q)"]) == ["r"]
assert find_unused(["m = 3", "n = m"]) == ["m", "n"]
assert find_unused(["m = 3", "n = m", "log(m)"]) == ["n"]
assert find_unused(["m = 3", "n = m", "log(n)"]) == []
assert find_unused([]) == []
assert find_unused(["a = 1", "log(a)", "b = a + 1", "c = b", "log(b)"]) == ["c"]

print("All tests passed!")
