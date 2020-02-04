from typing import Dict, List, NamedTuple, DefaultDict
from collections import defaultdict
from pprint import pprint
import glob
import csv


Senator =NamedTuple('Senator', [('name', str) , ('party', str), ('state', str)])
VoteValue = int
vote_value: Dict[str, VoteValue] = {'Yea': 1, 'Not Voting': 0, 'Nay': -1}
accumulated_votes: DefaultDict[Senator, List[VoteValue]] = defaultdict(list)

for filename in glob.glob('congress_data\*.csv'):
    with open(filename, encoding='utf-8') as f:
        
        reader = csv.reader(f)
        session_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_votes[senator].append(vote_value[vote])

pprint(accumulated_votes, width=500)

