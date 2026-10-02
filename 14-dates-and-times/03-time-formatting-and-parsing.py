"""
Python Time Formatting and Parsing
===================================

This file covers:
- strftime()
- strptime()
- ISO 8601
- Formatting dates and times
- Parsing strings into datetime objects
- API timestamps
- User-friendly date formatting
- Common date parsing mistakes
"""

from datetime import datetime, date, time, timezone
from zoneinfo import ZoneInfo


# ============================================================
# 1. Formatting datetime With strftime()
# ============================================================

current_time = datetime.now()

formatted = current_time.strftime("%Y-%m-%d")

print(formatted)


# ============================================================
# 2. Common Format Codes
# ============================================================

current_time = datetime.now()

print(current_time.strftime("%Y"))  # Year
print(current_time.strftime("%m"))  # Month
print(current_time.strftime("%d"))  # Day
print(current_time.strftime("%H"))  # Hour
print(current_time.strftime("%M"))  # Minute
print(current_time.strftime("%S"))  # Second


# ============================================================
# 3. Common Date Formats
# ============================================================

current_time = datetime.now()

print(current_time.strftime("%Y-%m-%d"))
print(current_time.strftime("%d/%m/%Y"))
print(current_time.strftime("%m/%d/%Y"))
print(current_time.strftime("%Y/%m/%d"))


# ============================================================
# 4. Time Formats
# ============================================================

current_time = datetime.now()

print(current_time.strftime("%H:%M"))
print(current_time.strftime("%H:%M:%S"))


# 12-hour format

print(current_time.strftime("%I:%M %p"))


# ============================================================
# 5. Full Date and Time
# ============================================================

current_time = datetime.now()

formatted = current_time.strftime(
    "%Y-%m-%d %H:%M:%S"
)

print(formatted)


# ============================================================
# 6. Day and Month Names
# ============================================================

current_time = datetime.now()

print(current_time.strftime("%A"))
print(current_time.strftime("%a"))

print(current_time.strftime("%B"))
print(current_time.strftime("%b"))


# ============================================================
# 7. Human-Friendly Date
# ============================================================

current_time = datetime.now()

formatted = current_time.strftime(
    "%A, %B %d, %Y"
)

print(formatted)


# Example:
#
# Friday, October 02, 2026


# ============================================================
# 8. Parsing String With strptime()
# ============================================================

date_string = "2026-10-02"

parsed_date = datetime.strptime(
    date_string,
    "%Y-%m-%d",
)

print(parsed_date)


# strptime() performs the opposite operation
# of strftime().


# ============================================================
# 9. strftime vs strptime
# ============================================================

current_time = datetime.now()

# datetime -> string
text = current_time.strftime("%Y-%m-%d")

print(text)


# string -> datetime
parsed = datetime.strptime(
    text,
    "%Y-%m-%d",
)

print(parsed)


# ============================================================
# 10. Parsing Date and Time
# ============================================================

date_string = "2026-10-02 18:30:45"

parsed = datetime.strptime(
    date_string,
    "%Y-%m-%d %H:%M:%S",
)

print(parsed)


# ============================================================
# 11. Parsing Different Formats
# ============================================================

date_string = "02/10/2026"

parsed = datetime.strptime(
    date_string,
    "%d/%m/%Y",
)

print(parsed)


date_string = "10/02/2026"

parsed = datetime.strptime(
    date_string,
    "%m/%d/%Y",
)

print(parsed)


# The format must match the input string.


# ============================================================
# 12. Parsing User Input
# ============================================================

user_input = "25/12/2026"

birthday = datetime.strptime(
    user_input,
    "%d/%m/%Y",
)

print("Birthday:", birthday.date())


# ============================================================
# 13. Handling Invalid Dates
# ============================================================

date_string = "31/02/2026"

try:
    parsed = datetime.strptime(
        date_string,
        "%d/%m/%Y",
    )

    print(parsed)

except ValueError:
    print("Invalid date")


# ============================================================
# 14. ISO 8601
# ============================================================

current_time = datetime.now(timezone.utc)

iso_string = current_time.isoformat()

print(iso_string)


# Example:
#
# 2026-10-02T12:30:00+00:00


# ISO 8601 is widely used for APIs and data exchange.


# ============================================================
# 15. Parsing ISO 8601
# ============================================================

iso_string = "2026-10-02T12:30:00+00:00"

parsed = datetime.fromisoformat(
    iso_string
)

print(parsed)
print(parsed.tzinfo)


# ============================================================
# 16. ISO Date Only
# ============================================================

today = date.today()

iso_date = today.isoformat()

print(iso_date)


parsed_date = date.fromisoformat(
    iso_date
)

print(parsed_date)


# ============================================================
# 17. ISO Time
# ============================================================

current_time = datetime.now()

time_string = current_time.time().isoformat()

print(time_string)


# ============================================================
# 18. UTC API Timestamp
# ============================================================

created_at = datetime.now(timezone.utc)

api_timestamp = created_at.isoformat()

print(api_timestamp)


# This format is suitable for sending a timestamp
# through an API.


# ============================================================
# 19. Converting API Timestamp
# ============================================================

api_timestamp = "2026-10-02T12:30:00+00:00"

created_at = datetime.fromisoformat(
    api_timestamp
)

print(created_at)


# ============================================================
# 20. Displaying API Time For User
# ============================================================

api_timestamp = "2026-10-02T12:30:00+00:00"

created_at = datetime.fromisoformat(
    api_timestamp
)

user_timezone = ZoneInfo("Asia/Tehran")

local_time = created_at.astimezone(
    user_timezone
)

display_time = local_time.strftime(
    "%Y-%m-%d %H:%M"
)

print(display_time)


# ============================================================
# 21. Backend Response Example
# ============================================================

created_at = datetime.now(timezone.utc)

response = {
    "id": 1001,
    "status": "completed",
    "created_at": created_at.isoformat(),
}

print(response)


# Example API response:
#
# {
#     "id": 1001,
#     "status": "completed",
#     "created_at": "2026-10-02T12:30:00+00:00"
# }


# ============================================================
# 22. Database Timestamp
# ============================================================

database_timestamp = datetime.now(timezone.utc)

database_value = database_timestamp.isoformat()

print("Database value:", database_value)


# A backend can store the actual moment in UTC
# and format it only when displaying it.


# ============================================================
# 23. Formatting A Date For A UI
# ============================================================

created_at = datetime(
    2026,
    10,
    2,
    18,
    45,
)

display_date = created_at.strftime(
    "%B %d, %Y"
)

print(display_date)


# ============================================================
# 24. Formatting An Order Date
# ============================================================

order_created_at = datetime(
    2026,
    10,
    2,
    14,
    35,
)

order_date = order_created_at.strftime(
    "%Y-%m-%d %H:%M"
)

print("Order created:", order_date)


# ============================================================
# 25. Formatting A Persian-Locale-Friendly Date
# ============================================================

# Python's standard datetime formatting does not convert
# Gregorian dates into the Persian calendar.
#
# It only formats the Gregorian date.
#
# Example:

created_at = datetime.now()

print(
    created_at.strftime("%Y/%m/%d")
)


# Persian calendar conversion requires
# an additional library or custom calendar logic.


# ============================================================
# 26. Parsing A Date From A Form
# ============================================================

form_value = "2026-11-15"

try:
    appointment_date = datetime.strptime(
        form_value,
        "%Y-%m-%d",
    ).date()

    print("Appointment:", appointment_date)

except ValueError:
    print("Invalid appointment date")


# ============================================================
# 27. Parsing A DateTime From A Form
# ============================================================

form_value = "2026-11-15 14:30"

try:
    appointment = datetime.strptime(
        form_value,
        "%Y-%m-%d %H:%M",
    )

    print("Appointment:", appointment)

except ValueError:
    print("Invalid appointment")


# ============================================================
# 28. Converting Between Formats
# ============================================================

original = "2026-10-02"

parsed = datetime.strptime(
    original,
    "%Y-%m-%d",
)

converted = parsed.strftime(
    "%d/%m/%Y"
)

print("Original:", original)
print("Converted:", converted)


# ============================================================
# 29. Parsing Multiple Formats
# ============================================================

date_string = "02/10/2026"

formats = [
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%m/%d/%Y",
]

parsed_date = None

for date_format in formats:
    try:
        parsed_date = datetime.strptime(
            date_string,
            date_format,
        )

        break

    except ValueError:
        continue


if parsed_date:
    print("Parsed:", parsed_date)
else:
    print("Could not parse date")


# ============================================================
# 30. Unix Timestamp
# ============================================================

current_time = datetime.now(timezone.utc)

timestamp = current_time.timestamp()

print("Unix timestamp:", timestamp)


# Convert Unix timestamp back to datetime.

converted_time = datetime.fromtimestamp(
    timestamp,
    tz=timezone.utc,
)

print(converted_time)


# ============================================================
# 31. Unix Timestamp Example
# ============================================================

expiration_time = datetime.now(timezone.utc)

expiration_timestamp = expiration_time.timestamp()

print(expiration_timestamp)


# Unix timestamps are commonly used
# in some APIs and authentication systems.


# ============================================================
# 32. Formatting With Microseconds
# ============================================================

current_time = datetime.now()

print(
    current_time.strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )
)


# %f represents microseconds.


# ============================================================
# 33. RFC-Like Timestamp
# ============================================================

current_time = datetime.now(timezone.utc)

formatted = current_time.strftime(
    "%a, %d %b %Y %H:%M:%S GMT"
)

print(formatted)


# ============================================================
# 34. Practical Event API Example
# ============================================================

event = {
    "id": 42,
    "name": "Python Workshop",
    "starts_at": datetime(
        2026,
        10,
        10,
        14,
        0,
        tzinfo=ZoneInfo("Asia/Tehran"),
    ),
}

api_event = {
    "id": event["id"],
    "name": event["name"],
    "starts_at": event["starts_at"]
    .astimezone(timezone.utc)
    .isoformat(),
}

print(api_event)


# ============================================================
# 35. Practical User Display Example
# ============================================================

event_timestamp = "2026-10-10T10:30:00+00:00"

event_time = datetime.fromisoformat(
    event_timestamp
)

user_timezone = ZoneInfo("Asia/Tehran")

user_event_time = event_time.astimezone(
    user_timezone
)

formatted_event_time = user_event_time.strftime(
    "%A, %B %d at %H:%M"
)

print(formatted_event_time)


# ============================================================
# 36. Common Mistakes
# ============================================================

# Mistake 1:
# Confusing strftime() and strptime().
#
# strftime -> datetime to string
# strptime -> string to datetime


# Mistake 2:
# Using the wrong format.

# Example:
#
# datetime.strptime(
#     "02/10/2026",
#     "%Y-%m-%d",
# )
#
# This raises ValueError.


# Mistake 3:
# Removing timezone information accidentally.


# Mistake 4:
# Using local time when an API expects UTC.


# Mistake 5:
# Manually manipulating date strings instead of
# using datetime tools.


# ============================================================
# 37. Recommended Backend Pattern
# ============================================================

# Receive:
#
# ISO 8601 timestamp
#
#        ↓
#
# Parse:
#
# datetime.fromisoformat()
#
#        ↓
#
# Normalize:
#
# UTC
#
#        ↓
#
# Store:
#
# Database
#
#        ↓
#
# Convert:
#
# User timezone
#
#        ↓
#
# Display:
#
# strftime()


# ============================================================
# 38. Quick Reference
# ============================================================

# datetime -> string:
#
# datetime.strftime(format)


# string -> datetime:
#
# datetime.strptime(string, format)


# datetime -> ISO string:
#
# datetime.isoformat()


# ISO string -> datetime:
#
# datetime.fromisoformat(string)


# date -> ISO string:
#
# date.isoformat()


# ISO string -> date:
#
# date.fromisoformat(string)


# datetime -> Unix timestamp:
#
# datetime.timestamp()


# Unix timestamp -> datetime:
#
# datetime.fromtimestamp()


# ============================================================
# 39. Final Example
# ============================================================

created_at = datetime.now(timezone.utc)

print("Stored:", created_at.isoformat())

user_timezone = ZoneInfo("Asia/Tehran")

user_time = created_at.astimezone(
    user_timezone
)

print(
    "Displayed:",
    user_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    ),
)