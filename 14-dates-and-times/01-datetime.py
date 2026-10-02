"""
Python Fundamentals
14 - Dates and Times
Topic: datetime

This file covers:
- date
- time
- datetime
- datetime.now()
- datetime.today()
- datetime.utcnow()
- timedelta
- Comparing dates and times
- Adding and subtracting time
- Formatting dates
- Parsing date strings
- ISO 8601
- Time zones basics
- Practical backend examples
- Best practices
"""


# ============================================================
# 1. Importing datetime
# ============================================================

from datetime import (
    date,
    time,
    datetime,
    timedelta
)


# ============================================================
# 2. Current Date
# ============================================================

today = date.today()

print(today)


"""
date.today() returns today's local date.

Example:

2026-10-02
"""


# ============================================================
# 3. Current Date Components
# ============================================================

today = date.today()

print(today.year)
print(today.month)
print(today.day)


# ============================================================
# 4. Creating a Date
# ============================================================

birthday = date(
    2001,
    5,
    15
)

print(birthday)


"""
date(year, month, day)
"""


# ============================================================
# 5. Date Properties
# ============================================================

birthday = date(
    2001,
    5,
    15
)

print(
    f"Year: {birthday.year}"
)

print(
    f"Month: {birthday.month}"
)

print(
    f"Day: {birthday.day}"
)


# ============================================================
# 6. Current Date and Time
# ============================================================

now = datetime.now()

print(now)


"""
datetime.now() returns the current local date and time.

Example:

2026-10-02 17:30:45.123456
"""


# ============================================================
# 7. datetime Components
# ============================================================

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)


# ============================================================
# 8. Creating a datetime
# ============================================================

created_at = datetime(
    2026,
    10,
    2,
    17,
    30,
    0
)

print(created_at)


"""
Arguments:

year
month
day
hour
minute
second
"""


# ============================================================
# 9. Current Time
# ============================================================

current_time = datetime.now().time()

print(current_time)


"""
time() extracts the time portion from a datetime object.
"""


# ============================================================
# 10. Creating a Time
# ============================================================

meeting_time = time(
    14,
    30,
    0
)

print(meeting_time)


"""
time(hour, minute, second)
"""


# ============================================================
# 11. Time Components
# ============================================================

meeting_time = time(
    14,
    30,
    45
)

print(meeting_time.hour)
print(meeting_time.minute)
print(meeting_time.second)


# ============================================================
# 12. datetime.today()
# ============================================================

today_datetime = datetime.today()

print(today_datetime)


"""
datetime.today() returns the current local date and time.

For most code, datetime.now() is more explicit and commonly used.
"""


# ============================================================
# 13. Combining Date and Time
# ============================================================

meeting_date = date(
    2026,
    10,
    10
)

meeting_time = time(
    14,
    30
)

meeting = datetime.combine(
    meeting_date,
    meeting_time
)

print(meeting)


# ============================================================
# 14. Extracting Date from datetime
# ============================================================

now = datetime.now()

current_date = now.date()

print(current_date)


# ============================================================
# 15. Extracting Time from datetime
# ============================================================

now = datetime.now()

current_time = now.time()

print(current_time)


# ============================================================
# 16. Comparing Dates
# ============================================================

today = date.today()

deadline = date(
    2026,
    12,
    31
)

if today < deadline:
    print("The deadline has not passed.")
else:
    print("The deadline has passed.")


# ============================================================
# 17. Comparing Datetimes
# ============================================================

now = datetime.now()

meeting = datetime(
    2026,
    10,
    2,
    20,
    0
)

if now < meeting:
    print("The meeting is in the future.")
else:
    print("The meeting has started or passed.")


# ============================================================
# 18. timedelta
# ============================================================

one_day = timedelta(
    days=1
)

print(one_day)


"""
timedelta represents a duration.

It can represent:

- Days
- Seconds
- Microseconds
- Weeks
- Hours
- Minutes
"""


# ============================================================
# 19. Adding Days
# ============================================================

today = date.today()

tomorrow = today + timedelta(
    days=1
)

print(tomorrow)


# ============================================================
# 20. Subtracting Days
# ============================================================

today = date.today()

yesterday = today - timedelta(
    days=1
)

print(yesterday)


# ============================================================
# 21. Adding Weeks
# ============================================================

today = date.today()

next_week = today + timedelta(
    weeks=1
)

print(next_week)


# ============================================================
# 22. Adding Hours
# ============================================================

now = datetime.now()

later = now + timedelta(
    hours=3
)

print(later)


# ============================================================
# 23. Adding Minutes
# ============================================================

now = datetime.now()

later = now + timedelta(
    minutes=30
)

print(later)


# ============================================================
# 24. Subtracting Time
# ============================================================

now = datetime.now()

earlier = now - timedelta(
    hours=2,
    minutes=30
)

print(earlier)


# ============================================================
# 25. Difference Between Dates
# ============================================================

start_date = date(
    2026,
    10,
    1
)

end_date = date(
    2026,
    10,
    10
)

difference = end_date - start_date

print(difference)
print(difference.days)


# ============================================================
# 26. Difference Between Datetimes
# ============================================================

start = datetime(
    2026,
    10,
    2,
    10,
    0
)

end = datetime(
    2026,
    10,
    2,
    15,
    30
)

difference = end - start

print(difference)
print(difference.total_seconds())


# ============================================================
# 27. Formatting with strftime()
# ============================================================

now = datetime.now()

formatted = now.strftime(
    "%Y-%m-%d"
)

print(formatted)


"""
Common format codes:

%Y
    Four-digit year

%m
    Month

%d
    Day

%H
    Hour

%M
    Minute

%S
    Second
"""


# ============================================================
# 28. Formatting Date and Time
# ============================================================

now = datetime.now()

formatted = now.strftime(
    "%Y-%m-%d %H:%M:%S"
)

print(formatted)


# ============================================================
# 29. Common Date Formats
# ============================================================

now = datetime.now()

print(
    now.strftime("%Y-%m-%d")
)

print(
    now.strftime("%d/%m/%Y")
)

print(
    now.strftime("%B %d, %Y")
)

print(
    now.strftime("%A, %B %d, %Y")
)


# ============================================================
# 30. Formatting for Logs
# ============================================================

now = datetime.now()

log_time = now.strftime(
    "%Y-%m-%d %H:%M:%S"
)

print(
    f"[{log_time}] User logged in."
)


# ============================================================
# 31. Parsing a String with strptime()
# ============================================================

date_string = "2026-10-02"

parsed_date = datetime.strptime(
    date_string,
    "%Y-%m-%d"
)

print(parsed_date)


"""
strptime() converts a string into a datetime object.
"""


# ============================================================
# 32. Parsing Date and Time
# ============================================================

date_string = "2026-10-02 17:30:00"

parsed_datetime = datetime.strptime(
    date_string,
    "%Y-%m-%d %H:%M:%S"
)

print(parsed_datetime)


# ============================================================
# 33. Parsing User Input
# ============================================================

date_string = "2026-12-31"

try:

    deadline = datetime.strptime(
        date_string,
        "%Y-%m-%d"
    )

    print(
        f"Deadline: {deadline}"
    )

except ValueError:

    print(
        "Invalid date format."
    )


# ============================================================
# 34. ISO 8601 Format
# ============================================================

now = datetime.now()

iso_string = now.isoformat()

print(iso_string)


"""
ISO 8601 is a common standard for representing
dates and times.

Example:

2026-10-02T17:30:00
"""


# ============================================================
# 35. Parsing ISO 8601
# ============================================================

iso_string = "2026-10-02T17:30:00"

parsed_datetime = datetime.fromisoformat(
    iso_string
)

print(parsed_datetime)


# ============================================================
# 36. Date to ISO String
# ============================================================

today = date.today()

iso_date = today.isoformat()

print(iso_date)


# ============================================================
# 37. Time to ISO String
# ============================================================

current_time = datetime.now().time()

iso_time = current_time.isoformat()

print(iso_time)


# ============================================================
# 38. Checking Whether a Date Has Passed
# ============================================================

today = date.today()

expiration_date = date(
    2026,
    12,
    31
)

if expiration_date < today:
    print("Expired.")
else:
    print("Still valid.")


# ============================================================
# 39. Checking an Expiration Time
# ============================================================

now = datetime.now()

expiration = now + timedelta(
    hours=2
)

if datetime.now() >= expiration:
    print("Expired.")
else:
    print("Still valid.")


# ============================================================
# 40. Practical Example: Account Creation
# ============================================================

created_at = datetime.now()

print(
    f"Account created at: "
    f"{created_at.strftime('%Y-%m-%d %H:%M:%S')}"
)


# ============================================================
# 41. Practical Example: Order Creation
# ============================================================

order = {
    "id": 1001,
    "customer": "Mohsen",
    "created_at": datetime.now().isoformat()
}

print(order)


"""
When sending datetime information through JSON,
an ISO-formatted string is commonly used.
"""


# ============================================================
# 42. Practical Example: Token Expiration
# ============================================================

issued_at = datetime.now()

expires_at = issued_at + timedelta(
    minutes=30
)

print(
    f"Issued: {issued_at}"
)

print(
    f"Expires: {expires_at}"
)


# ============================================================
# 43. Practical Example: Subscription Expiration
# ============================================================

subscription_start = date.today()

subscription_end = (
    subscription_start
    + timedelta(days=30)
)

print(
    f"Start: {subscription_start}"
)

print(
    f"End: {subscription_end}"
)


# ============================================================
# 44. Practical Example: Age Calculation
# ============================================================

birth_date = date(
    2001,
    5,
    15
)

today = date.today()

age = today.year - birth_date.year

if (
    today.month,
    today.day
) < (
    birth_date.month,
    birth_date.day
):
    age -= 1

print(
    f"Age: {age}"
)


# ============================================================
# 45. Practical Example: Working Days
# ============================================================

start_date = date(
    2026,
    10,
    1
)

end_date = date(
    2026,
    10,
    8
)

current_date = start_date

while current_date <= end_date:

    if current_date.weekday() < 5:
        print(
            f"Working day: {current_date}"
        )

    current_date += timedelta(
        days=1
    )


"""
weekday():

Monday    -> 0
Tuesday   -> 1
Wednesday -> 2
Thursday  -> 3
Friday    -> 4
Saturday  -> 5
Sunday    -> 6
"""


# ============================================================
# 46. Checking Weekend
# ============================================================

today = date.today()

if today.weekday() >= 5:
    print("Weekend.")
else:
    print("Weekday.")


# ============================================================
# 47. Getting the Weekday Name
# ============================================================

today = date.today()

weekday_name = today.strftime(
    "%A"
)

print(weekday_name)


# ============================================================
# 48. Getting the Month Name
# ============================================================

today = date.today()

month_name = today.strftime(
    "%B"
)

print(month_name)


# ============================================================
# 49. Time Comparison
# ============================================================

current_time = datetime.now().time()

start_time = time(
    9,
    0
)

end_time = time(
    17,
    0
)

if start_time <= current_time <= end_time:
    print("Business hours.")
else:
    print("Outside business hours.")


# ============================================================
# 50. datetime Resolution
# ============================================================

now = datetime.now()

print(
    now.microsecond
)


"""
datetime supports microsecond precision.

This can be useful for measuring or recording
high-resolution timestamps, although application
requirements determine the appropriate precision.
"""


# ============================================================
# 51. Naive Datetime
# ============================================================

now = datetime.now()

print(now)


"""
This datetime does not contain explicit timezone
information.

Such datetime objects are commonly called naive datetimes.
"""


# ============================================================
# 52. Timezone-Aware Datetime
# ============================================================

from datetime import timezone


now_utc = datetime.now(
    timezone.utc
)

print(now_utc)


"""
This datetime is timezone-aware and explicitly represents
UTC time.
"""


# ============================================================
# 53. UTC
# ============================================================

utc_now = datetime.now(
    timezone.utc
)

print(utc_now)


"""
UTC is commonly used as a reference timezone
in backend systems.
"""


# ============================================================
# 54. Converting a Timezone-Aware Datetime
# ============================================================

from zoneinfo import ZoneInfo


utc_now = datetime.now(
    timezone.utc
)

paris_time = utc_now.astimezone(
    ZoneInfo("Europe/Paris")
)

print(
    f"UTC: {utc_now}"
)

print(
    f"Paris: {paris_time}"
)


"""
zoneinfo is included in modern Python versions.

It provides IANA timezone support.
"""


# ============================================================
# 55. Creating a Datetime in a Specific Timezone
# ============================================================

tehran_time = datetime.now(
    ZoneInfo("Asia/Tehran")
)

print(tehran_time)


# ============================================================
# 56. Comparing Timezone-Aware Datetimes
# ============================================================

utc_now = datetime.now(
    timezone.utc
)

tehran_now = datetime.now(
    ZoneInfo("Asia/Tehran")
)

if utc_now < tehran_now:
    print("The comparison is valid.")


"""
Timezone-aware datetimes can be compared safely
when both represent actual points in time.
"""


# ============================================================
# 57. Converting Between Timezones
# ============================================================

utc_now = datetime.now(
    timezone.utc
)

new_york_time = utc_now.astimezone(
    ZoneInfo("America/New_York")
)

tokyo_time = utc_now.astimezone(
    ZoneInfo("Asia/Tokyo")
)

print(
    f"UTC: {utc_now}"
)

print(
    f"New York: {new_york_time}"
)

print(
    f"Tokyo: {tokyo_time}"
)


# ============================================================
# 58. Practical Backend Timestamp
# ============================================================

created_at = datetime.now(
    timezone.utc
)

user = {
    "id": 1,
    "created_at": created_at.isoformat()
}

print(user)


"""
Using UTC timestamps is a common backend practice.

The client can convert the timestamp to the user's
local timezone when displaying it.
"""


# ============================================================
# 59. Parsing a Timezone-Aware ISO String
# ============================================================

iso_string = (
    "2026-10-02T14:30:00+00:00"
)

parsed = datetime.fromisoformat(
    iso_string
)

print(parsed)

print(
    parsed.tzinfo
)


# ============================================================
# 60. Practical Example: Password Reset Token
# ============================================================

issued_at = datetime.now(
    timezone.utc
)

expires_at = issued_at + timedelta(
    minutes=15
)

token_data = {
    "token": "example-token",
    "issued_at": issued_at.isoformat(),
    "expires_at": expires_at.isoformat()
}

print(token_data)


# ============================================================
# 61. Practical Example: Checking Token Expiration
# ============================================================

current_time = datetime.now(
    timezone.utc
)

if current_time >= expires_at:
    print("Token expired.")
else:
    print("Token is valid.")


# ============================================================
# 62. Date Arithmetic
# ============================================================

project_start = date(
    2026,
    10,
    1
)

project_deadline = project_start + timedelta(
    days=14
)

print(
    f"Project starts: {project_start}"
)

print(
    f"Project deadline: {project_deadline}"
)


# ============================================================
# 63. Remaining Days
# ============================================================

today = date.today()

deadline = date(
    2026,
    12,
    31
)

remaining = deadline - today

if remaining.days >= 0:
    print(
        f"{remaining.days} days remaining."
    )
else:
    print("Deadline passed.")


# ============================================================
# 64. Practical Example: Scheduled Task
# ============================================================

scheduled_at = datetime.now(
    timezone.utc
) + timedelta(
    hours=2
)

print(
    f"Task scheduled at: {scheduled_at}"
)


# ============================================================
# 65. Practical Example: Login Record
# ============================================================

login_record = {
    "user_id": 42,
    "login_at": datetime.now(
        timezone.utc
    ).isoformat()
}

print(login_record)


# ============================================================
# 66. Practical Example: API Response
# ============================================================

api_response = {
    "status": "success",
    "data": {
        "created_at": datetime.now(
            timezone.utc
        ).isoformat()
    }
}

print(api_response)


"""
ISO 8601 strings are commonly suitable for
transporting datetime values through APIs.
"""


# ============================================================
# 67. Common Mistake: String Comparison
# ============================================================

date_1 = "2026-10-02"
date_2 = "2026-12-01"

print(
    date_1 < date_2
)


"""
ISO-formatted dates can sometimes be compared
lexicographically when they use the same format.

However, for actual date calculations and business logic,
use date/datetime objects instead of relying on strings.
"""


# ============================================================
# 68. Common Mistake: Mixing Naive and Aware Datetimes
# ============================================================

"""
Avoid mixing:

datetime.now()

with:

datetime.now(timezone.utc)

in calculations or comparisons without understanding
their timezone information.

Prefer a consistent timezone strategy.
"""


# ============================================================
# 69. Backend Time Strategy
# ============================================================

"""
A common backend strategy is:

1. Store timestamps in UTC.
2. Use timezone-aware datetime objects.
3. Send timestamps in ISO 8601 format.
4. Convert to the user's timezone for display.

Example:

Database:
    2026-10-02T14:30:00+00:00

Frontend:
    Convert to the user's local timezone
    before displaying it.
"""


# ============================================================
# 70. Best Practices
# ============================================================

"""
Best practices:

1. Use date for date-only values.
2. Use time for time-only values.
3. Use datetime for date + time.
4. Use timedelta for durations.
5. Use strftime() for formatting.
6. Use strptime() for parsing known formats.
7. Use ISO 8601 for data exchange.
8. Prefer timezone-aware datetimes for backend systems.
9. Use UTC as a consistent backend reference.
10. Avoid mixing naive and timezone-aware datetimes.
11. Store timestamps consistently.
12. Convert timestamps to local time mainly for presentation.
13. Validate user-provided date strings.
14. Be careful with daylight-saving-time transitions.
"""


# ============================================================
# 71. Summary
# ============================================================

"""
Important classes:

date
    Represents a calendar date.

time
    Represents a time of day.

datetime
    Represents date + time.

timedelta
    Represents a duration.

timezone
    Provides timezone information.

ZoneInfo
    Provides IANA timezone support.


Important methods:

datetime.now()
    Current local datetime.

date.today()
    Current local date.

strftime()
    datetime -> string

strptime()
    string -> datetime

isoformat()
    datetime/date/time -> ISO string

fromisoformat()
    ISO string -> datetime/date/time

astimezone()
    Converts an aware datetime to another timezone.


For backend development, remember:

UTC
+
timezone-aware datetime
+
ISO 8601
=
A strong foundation for handling timestamps.
"""