from .debug_utils import DebugUtils

log_call_details = DebugUtils.log_call_details
limit_calls = DebugUtils.limit_calls
limit_time_window = DebugUtils.limit_time_window
enforce_type_hints = DebugUtils.enforce_type_hints
retry_on_failure = DebugUtils.retry_on_failure
rate_limit_cooldown = DebugUtils.rate_limit_cooldown
password_protected = DebugUtils.password_protected
log_to_file = DebugUtils.log_to_file
user_confirm_required = DebugUtils.user_confirm_required

__all__ = [
    "log_call_details",
    "limit_calls",
    "limit_time_window",
    "enforce_type_hints",
    "retry_on_failure",
    "rate_limit_cooldown",
    "password_protected",
    "log_to_file",
    "user_confirm_required",
    "DebugUtils",
]