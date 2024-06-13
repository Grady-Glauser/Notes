import datetime

def convert_to_unix_timestamp(date_string, time_string):
    # Combine the date and time strings into a single datetime string
    datetime_string = f"{date_string} {time_string}"
    
    # Specify the format of the input date and time
    datetime_format = "%Y-%m-%d %H:%M:%S"
    
    # Parse the datetime string into a datetime object
    dt = datetime.datetime.strptime(datetime_string, datetime_format)
    
    # Convert the datetime object to a Unix timestamp (seconds since epoch)
    unix_timestamp = int(dt.timestamp() * 1000)  # Convert to milliseconds
    
    return unix_timestamp

# Example usage
date_string = "2023-06-01"  # Example date
time_string = "14:30:00"    # Example time

unix_timestamp = convert_to_unix_timestamp(date_string, time_string)
print("Unix timestamp in milliseconds:", unix_timestamp)
