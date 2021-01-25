import pandas as pd 
import numpy as np
import json
import click

@click.command()
@click.argument('sport')
@click.argument('date')
def main(sport, date):
    print(sport, date)

if __name__ == '__main__':
    main()