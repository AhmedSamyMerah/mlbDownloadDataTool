import pandas as pd 
import numpy as np
import json
import click

@click.command()
@click.argument('sport')
@click.argument('date')
def main(sport, date):
    try:
        url = 'https://statsapi.mlb.com/api/v1/schedule?sportId=%s&date=%s&hydrate=linescore' %(sport, date)
        df = pd.read_json(url)
        df1 = pd.json_normalize(df['dates'])
        df2 = pd.json_normalize(np.hstack(df1['games']))
        df2.to_csv('gameDay_%s.csv' %(date))
        print('File successfully saved in the current directory!')
    except:
        print('-------------')
        print('Please make sure your arguments follow the following convention: mlbSingleDayToCsv.py 1 2020-07-27')
        print('First argument is sportId and the second argument is the date that follows YYYY-MM-DD including the dashes')
        print('-------------')
        
if __name__ == '__main__':
    main()