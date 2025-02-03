# 20250203-evaluate_postfix-gist

**Gist file**: [https://gist.github.com/rjvitorino/941de3f7494ff7c07f830d8da9740217](https://gist.github.com/rjvitorino/941de3f7494ff7c07f830d8da9740217)

**Description**: Cassidy's interview question of the week: a function that evaluates a postfix expression (also known as Reverse Polish Notation) and returns the result

## evaluate_postfix.py

```Python
from typing import Dict, Callable, Final
from operator import add, sub, mul, floordiv


OPERATORS: Final[Dict[str, Callable[[int, int], int]]] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv,
}


def evaluate_postfix(expression: str) -> int:
    """Evaluates a postfix expression and returns the result.

    Args:
        expression: A string containing a valid postfix expression with single-digit integers
                   and operators +, -, *, /. Example: "12+" evaluates to 3

    Returns:
        The integer result of evaluating the expression

    Raises:
        ValueError: If the expression is invalid, empty, or contains invalid tokens

    Examples:
        >>> evaluate_postfix("12+")
        3
        >>> evaluate_postfix("53*2+")
        17
    """
    if not expression:
        raise ValueError("Expression cannot be empty")

    # Initialise stack to store operands
    stack: list[int] = []

    for token in expression.strip():
        if token.isdigit():
            # If token is a number, convert to int and push to stack
            stack.append(int(token))
        elif token in OPERATORS:
            # If token is an operator, pop two operands in reverse order and apply the operation
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression: insufficient operands")
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Push the result back to the stack
            stack.append(OPERATORS[token](operand1, operand2))
        elif not token.isspace():
            # Token is neither a number nor an operator (and not whitespace), so invalid
            raise ValueError(f"Invalid token in expression: {token}")

    # After processing all tokens, stack should have exactly one value
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression: too many operands")

    return stack[0]


def main() -> None:
    """Run test cases for the evaluate_postfix function."""
    test_cases = [
        ("12+", 3),
        ("56+7*", 77),
        ("34-", -1),
        ("92/", 4),
        ("53*2+", 17),
        ("82-3*", 18),
        ("91-8*", 64),
        ("234++", 9),
        ("23*4*", 24),
    ]

    for expression, expected in test_cases:
        result = evaluate_postfix(expression)
        assert (
            result == expected
        ), f"Failed: {expression} = {result}, expected {expected}"

    print("All checks passed!")


if __name__ == "__main__":
    main()

```