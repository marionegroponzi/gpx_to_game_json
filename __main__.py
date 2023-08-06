import click
import gpxpy
import json
import sys

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--type', type=click.Choice(['Explorer','Pirate'], case_sensitive=False), prompt="Game type", help="The type of the game to create")
@click.option('--title', prompt="Game title", help="The title of the game to create")
def gpx_to_game_json(filename, type, title):
    click.echo(f'Reading: {filename}')

    game={}
    game['title'] = title
    game['type'] = type
    game['waypoints'] = []

    gpx_file = open(filename, 'r')

    gpx = gpxpy.parse(gpx_file)

    index = 0
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat = round(point.latitude, 4)
                lng = round(point.longitude, 4)
                # print(f'Point at ({lat},{lng}) -> {point.elevation}')
                
                waypoint = {}
                waypoint['title'] = str(index)
                index = index + 1
                waypoint['latitude'] = lat
                waypoint['longitude'] = lng

                game['waypoints'].append(waypoint)

    s = json.dumps(game)
    print(s)


if __name__ == '__main__':
    print(f"Mario says: {str(sys.argv)}")
    gpx_to_game_json()
