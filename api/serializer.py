from rest_framework import serializers
from datetime import datetime
from base.models import StockData

class StockDataSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = StockData
        fields = ['id', 'symbol', 'formatted_date', 'high', 'low', 'open', 'close']

    def get_formatted_date(self, obj):
        # Access the created_at field from the object
        # date = obj.date
        print(obj)
        datetime_string = obj['date']

        datetime_object = datetime.fromisoformat(str(datetime_string))

        # # Extract only the date part
        date_only = datetime_object.date()

        # Return the formatted date
        return date_only
