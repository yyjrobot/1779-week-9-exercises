import json
import datetime
from collections.abc import Mapping


def setDateResult(option=None):
    today = datetime.datetime.today()
    one_day = datetime.timedelta(days=1)

    if option == "yesterday":
        today = today - one_day
    elif option == "tomorrow":
        today = today + one_day

    mo = today.month
    da = today.day
    y = today.year

    result = {
        "month": mo,
        "day": da,
        "year": y
    }

    return result


def lambda_handler(event, context):
    try:
        if 'queryStringParameters' in event and event['queryStringParameters'] != None:
            event = event["queryStringParameters"]
        else:
            if isinstance(event["body"], Mapping):
                event = event["body"]
            else:
                event = json.loads(event["body"])

        sc = None  # Status code
        result = ""  # Response payload

        if "option" in event and event["option"] == "date":
            if "period" in event and event["period"] == "yesterday":
                result = setDateResult("yesterday")
                sc = 200;
            elif "period" in event and event["period"] == "today":
                result = setDateResult()
                sc = 200
            elif "period" in event and event["period"] == "tomorrow":
                result = setDateResult("tomorrow")
                sc = 200
            else:
                result = {"error": "Must specify 'yesterday', 'today', or 'tomorrow'."}
                sc = 400;
        elif "option" in event and event["option"] == "time":
            d = datetime.datetime.now()
            h = d.hour
            mi = d.minute
            s = d.second

            result = {
                "hour": h,
                "minute": mi,
                "second": s
            }
            sc = 200;
        else:
            result = {"error": "Must specify 'date' or 'time'."}
            sc = 400;

        response = {
            'statusCode': sc,
            'headers': {"Content-type": "application/json"},
            'body': json.dumps(result, separators=(',', ':'))
        }

        return response
    except Exception as e:
        return "Error:" + e
