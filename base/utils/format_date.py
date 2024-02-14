from datetime import datetime

def get_formatted_date(date_obj):
        # Access the created_at field from the object
        datetime_string = date_obj

        datetime_object = datetime.fromisoformat(str(datetime_string))

        # # Extract only the date part
        date_only = datetime_object.date()

        # Return the formatted date
        return date_only.strftime('%Y-%m-%d')