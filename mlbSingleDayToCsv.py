import pandas as pd 
import numpy as np
import json
import click

@click.command()
@click.argument('sport')
@click.argument('date')
def main(sport, date):
    print(sport, date)
    try:
        url = 'https://statsapi.mlb.com/api/v1/schedule?sportId=%s&date=%s&hydrate=linescore' %(sport, date)
        df = pd.read_json(url)
        print(df.head())
    except:
        print('Did not work bihhh')

if __name__ == '__main__':
    main()