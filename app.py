#!/usr/bin/env python
import click
import datetime

@click.command()
@click.option("--date")
def date_to_day(date):
    day = datetime.datetime.strptime(date, '%m-%d-%Y').strftime('%A')
    click.echo(f'Day of the week for {date}: {day}')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    date_to_day()