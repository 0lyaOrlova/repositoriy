import json
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('server', type=str)
parser.add_argument('host', type=str)
parser.add_argument('seatse', type=str, nargs='+')
parser.add_argument('--mult', type=int, default=2, required=True)
parser.add_argument('--not_mult', action='store_true', default=False)
args = parser.parse_args()
server = f'{args.server}:{args.post}'
response = requests.get(server).json()
for i in args.seatse:
    for j in response[i]:
        for w in range(len(j)):
            if j[w] % 5 == 0:
                j[w] = j[w] // args.mult
            elif args.not_mult:
                j[w] = j[w] % args.mult
unswer = []
for i in response:
    unswer.append({'plase': i, 'rests': sum([i % 5 for i in response[i]]), 'smallest': min(response[i])})

with open('box.json', 'w') as f:
    f.write(json.dumps(sorted(unswer, key=lambda x: x['place'])))
