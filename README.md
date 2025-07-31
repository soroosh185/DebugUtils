
---

# 🔧 DebugUtils

A modern Python decorator toolkit designed to make debugging, logging, and controlling function behavior easier and more expressive.  
From runtime type checking to call rate limiting, `DebugUtils` offers powerful tools for every developer's workflow.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success)
![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)

---

## 📦 Installation

```bash
pip install devwraps


---

📚 Features

🔍 Detailed Debug Logging with colors, arguments, return values, and execution time

🔢 Limit Number of Calls and control execution

⏱️ Time-based Rate Limiting

✅ Type Hint Enforcement at runtime

🔁 Retry Mechanism for unstable functions

🔐 Password Protection for sensitive functions

🕒 Cooldown System between calls

📁 Log Output to File

🙋 User Confirmation Prompts before running actions



---

🚀 Quick Start

from devwraps import log_call_details, limit_calls, enforce_type_hints

@log_call_details(color="cyan")
@limit_calls(max_runs=3)
@enforce_type_hints
def greet(name: str) -> str:
    print(f"Hello, {name}!")
    return f"Greeted {name}"

greet("Alice")


---

📘 Usage Examples

🎨 debug — Colorful and Detailed Logging

from devwraps import debug

@debug(color="green")
def say_hello(name: str):
    print(f"Hi, {name}!")

say_hello("John")


---

🔢 limit_calls — Restrict Number of Calls

from devwraps import limit_calls

@limit_calls(max_runs=2)
def show():
    print("Hello again!")

show()
show()
show()  # Will be ignored


---

⏱️ limit_time_window — Time-Based Call Limit

from devwraps import limit_time_window
import time

@limit_time_window(max_seconds=5)
def ping():
    print("Ping!")

ping()
ping()  # Blocked if called within 5 seconds


---

✅ enforce_type_hints — Runtime Type Check

from devwraps import enforce_type_hints

@enforce_type_hints
def add(x: int, y: int) -> int:
    return x + y

add(2, 3)      # ✅
add("2", "3")  # ❌ Raises TypeError


---

🔁 retry_on_failure — Retry Automatically

from devwraps import retry_on_failure
import random

@retry_on_failure(max_retries=3, delay=2)
def unstable():
    if random.random() < 0.7:
        raise Exception("Random fail")
    print("Succeeded!")

unstable()


---

🕒 rate_limit_cooldown — Cooldown Between Calls

from devwraps import rate_limit_cooldown
import time

@rate_limit_cooldown(seconds=3)
def limited():
    print("Executed!")

limited()
limited()  # Will be skipped if within cooldown


---

🔐 password_protected — Secure with Password

from devwraps import password_protected

@password_protected(password="admin123")
def sensitive_action():
    print("Sensitive task done!")

sensitive_action()


---

📁 log_to_file — Output to Log File

from devwraps import log_to_file

@log_to_file(filepath="output.log")
def calc(x):
    print(f"Calculating {x}")
    return x * 2

calc(10)


---

🙋 user_confirm_required — Ask for Confirmation

from devwraps import user_confirm_required

@user_confirm_required(prompt="Proceed with action? (y/n): ")
def dangerous_task():
    print("Task complete!")

dangerous_task()



---

📝 License

This project is licensed under the MIT License — see the LICENSE file for details.


---

👤 Author

Soroosh Fathi
📧 sorooshfathi1385@email.com
💼 GitHub: github.com/soroosh185


---

🌟 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Feel free to star the repo if you find it useful ⭐


---
