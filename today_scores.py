import requests
from datetime import datetime
import dateutil.parser as date_convert
import pytz
# import pprint
# pp = pprint.PrettyPrinter(indent=4)

r = requests.get('http://api.football-data.org/v1/soccerseasons/424/fixtures')

# print r.json()
soccerseasons = r.json()

# pp.pprint(soccerseasons)

print "TODAYS MATCH"

for each_match in soccerseasons['fixtures']:
    match_dt = date_convert.parse(each_match['date'])
    if match_dt <= datetime.now(pytz.utc) and match_dt.date() == datetime.now(pytz.utc).date():
        print "%s vs %s" % (each_match['homeTeamName'], each_match['awayTeamName'])
        result = each_match['result']
        print "score: {} - {}".format(result['goalsHomeTeam'], result['goalsAwayTeam'])
        print "======================="
