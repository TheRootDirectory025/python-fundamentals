"""
Python Timezones
================

This file covers timezone-aware datetime objects,
UTC, timezone conversion, ZoneInfo, DST, and
common backend mistakes.
"""

# ============================================================
# 1. Why Timezones Matter
# ============================================================

# A datetime without timezone information is called
# a naive datetime.

from datetime import datetime

naive_datetime = datetime.now()

print(naive_datetime)
print(naive_datetime.tzinfo)


# A datetime with timezone information is called
# an aware datetime.


# ============================================================
# 2. UTC
# ============================================================

from datetime import timezone

utc_now = datetime.now(timezone.utc)

print(utc_now)
print(utc_now.tzinfo)


# UTC is commonly used as the standard time reference
# for backend systems and APIs.


# ============================================================
# 3. Creating a UTC Datetime
# ============================================================

created_at = datetime(
    2026,
    10,
    2,
    14,
    30,
    tzinfo=timezone.utc,
)

print(created_at)


# ============================================================
# 4. ZoneInfo
# ============================================================

from zoneinfo import ZoneInfo

new_york_time = datetime.now(
    ZoneInfo("America/New_York")
)

london_time = datetime.now(
    ZoneInfo("Europe/London")
)

tehran_time = datetime.now(
    ZoneInfo("Asia/Tehran")
)

print("New York:", new_york_time)
print("London:", london_time)
print("Tehran:", tehran_time)


# ============================================================
# 5. Converting Between Timezones
# ============================================================

utc_time = datetime.now(timezone.utc)

tehran_time = utc_time.astimezone(
    ZoneInfo("Asia/Tehran")
)

london_time = utc_time.astimezone(
    ZoneInfo("Europe/London")
)

tokyo_time = utc_time.astimezone(
    ZoneInfo("Asia/Tokyo")
)

print("UTC:", utc_time)
print("Tehran:", tehran_time)
print("London:", london_time)
print("Tokyo:", tokyo_time)


# ============================================================
# 6. astimezone()
# ============================================================

# astimezone() converts the same moment
# into another timezone.

utc_time = datetime(
    2026,
    10,
    2,
    12,
    0,
    tzinfo=timezone.utc,
)

tehran_time = utc_time.astimezone(
    ZoneInfo("Asia/Tehran")
)

print("UTC:", utc_time)
print("Tehran:", tehran_time)


# The clock time changes,
# but the actual moment remains the same.


# ============================================================
# 7. Timezone Information
# ============================================================

current_time = datetime.now(
    ZoneInfo("Asia/Tehran")
)

print("Datetime:", current_time)
print("Timezone:", current_time.tzinfo)
print("UTC Offset:", current_time.utcoffset())


# ============================================================
# 8. Comparing Aware Datetimes
# ============================================================

time_1 = datetime(
    2026,
    10,
    2,
    12,
    0,
    tzinfo=timezone.utc,
)

time_2 = datetime(
    2026,
    10,
    2,
    15,
    30,
    tzinfo=ZoneInfo("Asia/Tehran"),
)

print(time_1)
print(time_2)

print(time_1 == time_2)
print(time_1 < time_2)


# Different timezone representations can still
# represent the same moment in time.


# ============================================================
# 9. Naive vs Aware Datetimes
# ============================================================

naive = datetime(2026, 10, 2, 12, 0)

aware = datetime(
    2026,
    10,
    2,
    12,
    0,
    tzinfo=timezone.utc,
)

print("Naive:", naive)
print("Aware:", aware)


# Do not compare naive and aware datetimes directly.
#
# Example:
#
# print(naive < aware)
#
# This raises:
# TypeError: can't compare offset-naive and
# offset-aware datetimes


# ============================================================
# 10. Making A Datetime UTC-Aware
# ============================================================

local_time = datetime(
    2026,
    10,
    2,
    15,
    0,
)

utc_time = local_time.replace(
    tzinfo=timezone.utc
)

print(utc_time)


# IMPORTANT:
#
# replace(tzinfo=...) does NOT convert the time.
# It only attaches timezone information.
#
# Use it only when the original clock time is already
# known to represent that timezone.


# ============================================================
# 11. Converting A Local Time To UTC
# ============================================================

local_time = datetime(
    2026,
    10,
    2,
    15,
    0,
    tzinfo=ZoneInfo("Asia/Tehran"),
)

utc_time = local_time.astimezone(timezone.utc)

print("Local:", local_time)
print("UTC:", utc_time)


# ============================================================
# 12. Daylight Saving Time
# ============================================================

# Some countries change their clocks during the year.
# This is called Daylight Saving Time (DST).
#
# ZoneInfo uses the timezone database to handle
# these changes automatically.


new_york = ZoneInfo("America/New_York")

winter = datetime(
    2026,
    1,
    15,
    12,
    0,
    tzinfo=new_york,
)

summer = datetime(
    2026,
    7,
    15,
    12,
    0,
    tzinfo=new_york,
)

print("Winter:", winter)
print("Winter offset:", winter.utcoffset())

print("Summer:", summer)
print("Summer offset:", summer.utcoffset())


# ============================================================
# 13. User Timezone Example
# ============================================================

user_timezone = "Asia/Tehran"

user_time = datetime.now(
    ZoneInfo(user_timezone)
)

print("User timezone:", user_timezone)
print("User local time:", user_time)


# In a backend application, the user's timezone
# can be stored as a string such as:
#
# Asia/Tehran
# Europe/London
# America/New_York
# Asia/Tokyo


# ============================================================
# 14. Converting An API Timestamp
# ============================================================

api_timestamp = "2026-10-02T12:30:00+00:00"

parsed_time = datetime.fromisoformat(api_timestamp)

print("API time:", parsed_time)

user_time = parsed_time.astimezone(
    ZoneInfo("Asia/Tehran")
)

print("User time:", user_time)


# ============================================================
# 15. Storing Timestamps In UTC
# ============================================================

created_at = datetime.now(timezone.utc)

print("Created at:", created_at)


# A common backend pattern is:
#
# Store timestamps in UTC
# Convert to the user's timezone when displaying them.


# ============================================================
# 16. Database Example
# ============================================================

user = {
    "id": 101,
    "username": "mohsen",
    "created_at": datetime.now(timezone.utc),
}

print(user)


# The database timestamp represents one exact moment.
# The frontend can convert it to the user's local timezone.


# ============================================================
# 17. Token Expiration Example
# ============================================================

from datetime import timedelta

issued_at = datetime.now(timezone.utc)

expires_at = issued_at + timedelta(hours=2)

print("Issued at:", issued_at)
print("Expires at:", expires_at)


# Check whether a token has expired.

now = datetime.now(timezone.utc)

if now >= expires_at:
    print("Token expired")
else:
    print("Token is still valid")


# ============================================================
# 18. Scheduled Event Example
# ============================================================

event_time = datetime(
    2026,
    10,
    10,
    18,
    0,
    tzinfo=ZoneInfo("Asia/Tehran"),
)

print("Event time:", event_time)

event_in_utc = event_time.astimezone(timezone.utc)

print("Event in UTC:", event_in_utc)


# ============================================================
# 19. Backend Best Practice
# ============================================================

# A typical backend strategy:
#
# 1. Receive timestamps.
# 2. Parse them into aware datetime objects.
# 3. Store them in UTC.
# 4. Perform calculations using aware datetimes.
# 5. Convert to the user's timezone for presentation.


# Example:

created_at = datetime.now(timezone.utc)

user_timezone = ZoneInfo("Asia/Tehran")

display_time = created_at.astimezone(user_timezone)

print("Stored:", created_at)
print("Displayed:", display_time)


# ============================================================
# 20. Common Mistakes
# ============================================================

# Mistake 1:
# Using datetime.now() for backend timestamps.

naive_now = datetime.now()

print("Naive:", naive_now)


# Better:

aware_now = datetime.now(timezone.utc)

print("UTC:", aware_now)


# Mistake 2:
# Comparing naive and aware datetimes.


# Mistake 3:
# Using replace(tzinfo=...) when you actually need
# timezone conversion.


# Mistake 4:
# Storing local time instead of UTC in a backend system.


# Mistake 5:
# Assuming every timezone has a fixed UTC offset.


# ============================================================
# 21. Useful Timezone Names
# ============================================================

timezones = [
    "UTC",
    "Asia/Tehran",
    "Asia/Tokyo",
    "Europe/London",
    "Europe/Berlin",
    "America/New_York",
    "America/Los_Angeles",
]

for timezone_name in timezones:
    current = datetime.now(
        ZoneInfo(timezone_name)
    )

    print(timezone_name, "->", current)


# ============================================================
# 22. Practical Order Example
# ============================================================

order = {
    "id": 5001,
    "created_at": datetime.now(timezone.utc),
}

customer_timezone = ZoneInfo("Asia/Tehran")

order_display_time = order["created_at"].astimezone(
    customer_timezone
)

print("Order ID:", order["id"])
print("Created:", order_display_time)


# ============================================================
# 23. Practical Meeting Example
# ============================================================

meeting_time = datetime(
    2026,
    10,
    5,
    14,
    0,
    tzinfo=ZoneInfo("Europe/London"),
)

print("London:", meeting_time)

print(
    "Tehran:",
    meeting_time.astimezone(
        ZoneInfo("Asia/Tehran")
    ),
)

print(
    "Tokyo:",
    meeting_time.astimezone(
        ZoneInfo("Asia/Tokyo")
    ),
)


# ============================================================
# 24. Key Rules
# ============================================================

# Rule 1:
# Prefer timezone-aware datetime objects.

# Rule 2:
# Use UTC for backend storage and system-level timestamps.

# Rule 3:
# Use ZoneInfo for real-world timezone conversions.

# Rule 4:
# Use astimezone() for conversion.

# Rule 5:
# Do not mix naive and aware datetimes.

# Rule 6:
# Use local timezones when presenting dates to users.

# Rule 7:
# Store timezone names such as "Asia/Tehran"
# rather than manually storing fixed offsets.