import functools
import inspect
import sys
import time
from datetime import datetime, timedelta
from collections import defaultdict
from io import StringIO
import builtins
import functools
import inspect
import asyncio

from colorama import init, Fore, Style
import os
from datetime import datetime

init(autoreset=True)
_call_counts = defaultdict(int)
_call_times = {}
_last_call_time = defaultdict(lambda: 0)


class loggers:
import functools
import time
import inspect
import sys
from io import StringIO
import builtins
from colorama import init, Fore

init(autoreset=True)

class DebugUtils:
	@staticmethod
	def log_call_details(color="cyan", log_time=True, log_return=True):
		color_map = {
			"red": Fore.RED,
			"green": Fore.GREEN,
			"yellow": Fore.YELLOW,
			"blue": Fore.BLUE,
			"cyan": Fore.CYAN,
			"magenta": Fore.MAGENTA,
			"white": Fore.WHITE,
		}

		color_code = color_map.get(color.lower(), Fore.CYAN)

		def decorator(func):
			func_name = func.__qualname__
			loggers._call_counts[func_name] = 0
			is_coroutine = inspect.iscoroutinefunction(func)

			def check_and_print_args(bound):
				for name, val in bound.arguments.items():
					print(color_code + f"↪ {name} = {val} ({type(val).__name__})")

			if not is_coroutine:
				@functools.wraps(func)
				def wrapper(*args, **kwargs):
					loggers._call_counts[func_name] += 1
					call_count = loggers._call_counts[func_name]

					print(color_code + f"\n🔍 Calling function: {func.__name__} (call #{call_count})")

					signature = inspect.signature(func)
					bound = signature.bind(*args, **kwargs)
					bound.apply_defaults()
					check_and_print_args(bound)


					old_stdout = sys.stdout
					sys.stdout = mystdout = StringIO()


					original_input = builtins.input
					def logged_input(prompt=""):
						sys.stdout.write(Fore.YELLOW + f"📥 input requested: {prompt}")
						return original_input(prompt)

					builtins.input = logged_input

					start = time.perf_counter() if log_time else None

					try:
						result = func(*args, **kwargs)
					except Exception as e:
						sys.stdout = old_stdout
						builtins.input = original_input
						print(Fore.RED + f"❌ Exception: {type(e).__name__} - {e}")
						return None

					sys.stdout = old_stdout
					builtins.input = original_input

					output = mystdout.getvalue()
					if output.strip():
						print(Fore.MAGENTA + "📤 Output during function:")
						print(Fore.MAGENTA + output.strip())

					if log_return:
						print(color_code + f"✅ Returned: {result} ({type(result).__name__})")

					if log_time:
						duration = time.perf_counter() - start
						print(color_code + f"⏱ Execution time: {duration:.4f} seconds")

					return result

				return wrapper

			else:
				@functools.wraps(func)
				async def async_wrapper(*args, **kwargs):
					loggers._call_counts[func_name] += 1
					call_count = loggers._call_counts[func_name]

					print(color_code + f"\n🔍 (async) Calling function: {func.__name__} (call #{call_count})")

					signature = inspect.signature(func)
					bound = signature.bind(*args, **kwargs)
					bound.apply_defaults()
					check_and_print_args(bound)

					old_stdout = sys.stdout
					sys.stdout = mystdout = StringIO()

					original_input = builtins.input
					def logged_input(prompt=""):
						sys.stdout.write(Fore.YELLOW + f"📥 input requested: {prompt}")
						return original_input(prompt)

					builtins.input = logged_input

					start = time.perf_counter() if log_time else None

					try:
						result = await func(*args, **kwargs)
					except Exception as e:
						sys.stdout = old_stdout
						builtins.input = original_input
						print(Fore.RED + f"❌ Exception: {type(e).__name__} - {e}")
						return None

					sys.stdout = old_stdout
					builtins.input = original_input

					output = mystdout.getvalue()
					if output.strip():
						print(Fore.MAGENTA + "📤 Output during function:")
						print(Fore.MAGENTA + output.strip())

					if log_return:
						print(color_code + f"✅ Returned: {result} ({type(result).__name__})")

					if log_time:
						duration = time.perf_counter() - start
						print(color_code + f"⏱ Execution time: {duration:.4f} seconds")

					return result

				return async_wrapper

		return decorator

	@staticmethod
		def limit_calls(max_runs=3, color="cyan", silent=False):
			color_map = {
				"red": Fore.RED,
				"green": Fore.GREEN,
				"yellow": Fore.YELLOW,
				"blue": Fore.BLUE,
				"cyan": Fore.CYAN,
				"magenta": Fore.MAGENTA,
				"white": Fore.WHITE,
			}
			color_code = color_map.get(color.lower(), Fore.CYAN)
	
			def decorator(func):
				func_name = func.__qualname__
				is_async = inspect.iscoroutinefunction(func)
	
				@functools.wraps(func)
				async def async_wrapper(*args, **kwargs):
					_call_counts[func_name] += 1
					call_count = _call_counts[func_name]
	
					if call_count > max_runs:
						if not silent:
							print(Fore.RED + f"⛔ Function `{func.__name__}` blocked after {max_runs} calls.")
						return None
	
					if not silent:
						print(color_code + f"🔁 Function `{func.__name__}` called ({call_count}/{max_runs})")
	
					return await func(*args, **kwargs)
	
				@functools.wraps(func)
				def sync_wrapper(*args, **kwargs):
					_call_counts[func_name] += 1
					call_count = _call_counts[func_name]
	
					if call_count > max_runs:
						if not silent:
							print(Fore.RED + f"⛔ Function `{func.__name__}` blocked after {max_runs} calls.")
						return None
	
					if not silent:
						print(color_code + f"🔁 Function `{func.__name__}` called ({call_count}/{max_runs})")
	
					return func(*args, **kwargs)
	
				return async_wrapper if is_async else sync_wrapper
	
			return decorator

	@staticmethod
	def limit_time_window(max_seconds=10, color="cyan", silent=False):
		color_map = {
			"red": Fore.RED,
			"green": Fore.GREEN,
			"yellow": Fore.YELLOW,
			"blue": Fore.BLUE,
			"cyan": Fore.CYAN,
			"magenta": Fore.MAGENTA,
			"white": Fore.WHITE,
		}
		color_code = color_map.get(color.lower(), Fore.CYAN)

		def decorator(func):
			func_name = func.__qualname__
			_call_times[func_name] = None
			is_async = inspect.iscoroutinefunction(func)

			@functools.wraps(func)
			async def async_wrapper(*args, **kwargs):
				now = datetime.now()

				if _call_times[func_name] is None:
					_call_times[func_name] = now
					if not silent:
						print(color_code + f"🕒 Started timing for `{func.__name__}`")
					return await func(*args, **kwargs)

				elapsed = (now - _call_times[func_name]).total_seconds()
				if elapsed > max_seconds:
					if not silent:
						print(Fore.RED + f"⛔ Function `{func.__name__}` blocked after {max_seconds} seconds.")
					return None

				if not silent:
					remaining = max_seconds - elapsed
					print(color_code + f"⏱ `{func.__name__}` called ({elapsed:.2f}s passed, {remaining:.2f}s left)")

				return await func(*args, **kwargs)

			@functools.wraps(func)
			def sync_wrapper(*args, **kwargs):
				now = datetime.now()

				if _call_times[func_name] is None:
					_call_times[func_name] = now
					if not silent:
						print(color_code + f"🕒 Started timing for `{func.__name__}`")
					return func(*args, **kwargs)

				elapsed = (now - _call_times[func_name]).total_seconds()
				if elapsed > max_seconds:
					if not silent:
						print(Fore.RED + f"⛔ Function `{func.__name__}` blocked after {max_seconds} seconds.")
					return None

				if not silent:
					remaining = max_seconds - elapsed
					print(color_code + f"⏱ `{func.__name__}` called ({elapsed:.2f}s passed, {remaining:.2f}s left)")

				return func(*args, **kwargs)

			return async_wrapper if is_async else sync_wrapper

		return decorator

    @staticmethod
    def enforce_type_hints(func):
        signature = inspect.signature(func)
        return_annotation = signature.return_annotation
        is_coroutine = inspect.iscoroutinefunction(func)

        def check_type(name, value, expected_type):
            if expected_type != inspect.Parameter.empty:
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{name}' باید از نوع {expected_type} باشد، اما مقدار {value} از نوع {type(value)} است."
                    )

        def check_return_type(value, expected_type):
            if expected_type != inspect.Signature.empty:
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"مقدار بازگشتی باید از نوع {expected_type} باشد، اما مقدار {value} از نوع {type(value)} است."
                    )

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()


            for name, value in bound.arguments.items():
                param = signature.parameters[name]
                check_type(name, value, param.annotation)

            result = await func(*args, **kwargs)


            check_return_type(result, return_annotation)

            return result

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()


            for name, value in bound.arguments.items():
                param = signature.parameters[name]
                check_type(name, value, param.annotation)

            result = func(*args, **kwargs)

            check_return_type(result, return_annotation)

            return result

        return async_wrapper if is_coroutine else sync_wrapper






	@staticmethod
	def retry_on_failure(max_retries=3, delay=1, exceptions=(Exception,), silent=False):
		def decorator(func):
			is_coroutine = inspect.iscoroutinefunction(func)

			@functools.wraps(func)
			def sync_wrapper(*args, **kwargs):
				for attempt in range(1, max_retries + 1):
					try:
						return func(*args, **kwargs)
					except exceptions as e:
						if not silent:
							print(Fore.YELLOW + f"⚠️ Attempt {attempt} failed: {e}")
						if attempt < max_retries:
							time.sleep(delay)
						else:
							if not silent:
								print(Fore.RED + f"❌ All {max_retries} attempts failed.")
							raise

			@functools.wraps(func)
			async def async_wrapper(*args, **kwargs):
				for attempt in range(1, max_retries + 1):
					try:
						return await func(*args, **kwargs)
					except exceptions as e:
						if not silent:
							print(Fore.YELLOW + f"⚠️ Attempt {attempt} failed (async): {e}")
						if attempt < max_retries:
							await asyncio.sleep(delay)
						else:
							if not silent:
								print(Fore.RED + f"❌ All {max_retries} async attempts failed.")
							raise

			return async_wrapper if is_coroutine else sync_wrapper

		return decorator





	@staticmethod
	def rate_limit_cooldown(seconds=10, color="cyan", silent=False):
		color_map = {
			"red": Fore.RED,
			"green": Fore.GREEN,
			"yellow": Fore.YELLOW,
			"blue": Fore.BLUE,
			"cyan": Fore.CYAN,
			"magenta": Fore.MAGENTA,
			"white": Fore.WHITE,
		}
		color_code = color_map.get(color.lower(), Fore.CYAN)
	
		def decorator(func):
			func_name = func.__qualname__
	
			if inspect.iscoroutinefunction(func):
				@functools.wraps(func)
				async def async_wrapper(*args, **kwargs):
					now = time.time()
					last = _last_call_time[func_name]
	
					if now - last < seconds:
						if not silent:
							remaining = seconds - (now - last)
							print(Fore.RED + f"⏳ Async function `{func.__name__}` is on cooldown. Try again in {remaining:.1f} seconds.")
						return None
	
					_last_call_time[func_name] = now
					if not silent:
						print(color_code + f"✅ Async function `{func.__name__}` executed.")
					return await func(*args, **kwargs)
	
				return async_wrapper
	
			else:
				@functools.wraps(func)
				def sync_wrapper(*args, **kwargs):
					now = time.time()
					last = _last_call_time[func_name]
	
					if now - last < seconds:
						if not silent:
							remaining = seconds - (now - last)
							print(Fore.RED + f"⏳ Function `{func.__name__}` is on cooldown. Try again in {remaining:.1f} seconds.")
						return None
	
					_last_call_time[func_name] = now
					if not silent:
						print(color_code + f"✅ Function `{func.__name__}` executed.")
					return func(*args, **kwargs)
	
				return sync_wrapper
	
		return decorator




	@staticmethod
	def password_protected(password, color="yellow", silent=False):
		color_map = {
			"red": Fore.RED,
			"green": Fore.GREEN,
			"yellow": Fore.YELLOW,
			"blue": Fore.BLUE,
			"cyan": Fore.CYAN,
			"magenta": Fore.MAGENTA,
			"white": Fore.WHITE,
		}
		color_code = color_map.get(color.lower(), Fore.YELLOW)
	
		def decorator(func):
			if inspect.iscoroutinefunction(func):
				@functools.wraps(func)
				async def wrapper(*args, **kwargs):
					try:
						input_pass = input("🔐 Enter password to access this function: ")
						if input_pass != password:
							if not silent:
								print(Fore.RED + "❌ Access denied. Incorrect password.")
							return None
						if not silent:
							print(color_code + f"✅ Access granted to `{func.__name__}`.")
						return await func(*args, **kwargs)
					except Exception as e:
						print(Fore.RED + f"⚠️ Error: {e}")
						return None
			else:
				@functools.wraps(func)
				def wrapper(*args, **kwargs):
					try:
						input_pass = input("🔐 Enter password to access this function: ")
						if input_pass != password:
							if not silent:
								print(Fore.RED + "❌ Access denied. Incorrect password.")
							return None
						if not silent:
							print(color_code + f"✅ Access granted to `{func.__name__}`.")
						return func(*args, **kwargs)
					except Exception as e:
						print(Fore.RED + f"⚠️ Error: {e}")
						return None
			return wrapper
		return decorator


	@staticmethod
	def log_to_file(filepath="log.txt", log_return=True, log_time=True, log_errors=True, encoding="utf-8"):
		def decorator(func):
			is_coroutine = inspect.iscoroutinefunction(func)


			os.makedirs(os.path.dirname(filepath), exist_ok=True)

			def log(message):
				with open(filepath, "a", encoding=encoding) as f:
					f.write(message + "\n")

			@functools.wraps(func)
			def sync_wrapper(*args, **kwargs):
				timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				log(f"[{timestamp}] Called `{func.__name__}` with args={args}, kwargs={kwargs}")
				start = time.time()
				try:
					result = func(*args, **kwargs)
					if log_return:
						log(f"[{timestamp}] → Return: {repr(result)}")
					if log_time:
						log(f"[{timestamp}] ⏱ Duration: {time.time() - start:.4f} seconds")
					return result
				except Exception as e:
					if log_errors:
						log(f"[{timestamp}] ❌ Exception: {type(e).__name__}: {e}")
					raise

			@functools.wraps(func)
			async def async_wrapper(*args, **kwargs):
				timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				log(f"[{timestamp}] Called (async) `{func.__name__}` with args={args}, kwargs={kwargs}")
				start = time.time()
				try:
					result = await func(*args, **kwargs)
					if log_return:
						log(f"[{timestamp}] → Return: {repr(result)}")
					if log_time:
						log(f"[{timestamp}] ⏱ Duration: {time.time() - start:.4f} seconds")
					return result
				except Exception as e:
					if log_errors:
						log(f"[{timestamp}] ❌ Exception: {type(e).__name__}: {e}")
					raise

			return async_wrapper if is_coroutine else sync_wrapper

		return decorator



	def user_confirm_required(prompt="Are you sure? (y/n): ", color="yellow", silent=False):
		color_map = {
			"red": Fore.RED,
			"green": Fore.GREEN,
			"yellow": Fore.YELLOW,
			"blue": Fore.BLUE,
			"cyan": Fore.CYAN,
			"magenta": Fore.MAGENTA,
			"white": Fore.WHITE,
		}
		color_code = color_map.get(color.lower(), Fore.YELLOW)
	
		def decorator(func):
			is_async = inspect.iscoroutinefunction(func)
	
			@functools.wraps(func)
			async def async_wrapper(*args, **kwargs):
				if not silent:
					answer = input(color_code + prompt).strip().lower()
					if answer not in ("y", "yes"):
						print(Fore.RED + "❌ Operation cancelled by user.")
						return None
				return await func(*args, **kwargs)
	
			@functools.wraps(func)
			def sync_wrapper(*args, **kwargs):
				if not silent:
					answer = input(color_code + prompt).strip().lower()
					if answer not in ("y", "yes"):
						print(Fore.RED + "❌ Operation cancelled by user.")
						return None
				return func(*args, **kwargs)
	
			return async_wrapper if is_async else sync_wrapper
	
		return decorator