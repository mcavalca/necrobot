import datetime
from dateutil import parser
import pytz
from .exception import ParseException


class CustomParserInfo(parser.parserinfo):
    WEEKDAYS = [
        ('Mon', 'Monday'),
        ('Tue', 'Tues', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thurs', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    ]


def parse_datetime(parse_str, timezone=pytz.utc):
    if parse_str.lower() == 'now':
        return pytz.utc.localize(datetime.datetime.utcnow() + datetime.timedelta(minutes=1))

    try:
        dateutil_parse = parser.parse(
            parse_str,
            fuzzy=True,
            dayfirst=False,
            yearfirst=False)
        if 'tomorrow' in parse_str:
            return timezone.localize(dateutil_parse + datetime.timedelta(days=1)).astimezone(pytz.utc)
        else:
            return timezone.localize(dateutil_parse).astimezone(pytz.utc)
    except ValueError:
        raise ParseException('Couldn\'t parse {0} as a time.'.format(parse_str))
