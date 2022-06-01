import click


@click.command()
@click.option('--name', '-n', help="Enter your name",
              required=True, prompt="your name?")
@click.argument('number')
def supercli(name, number):
    '''
        this is a docstring which tells about
        working of supercli library
    '''
    print("hello superrrr ")
    for _ in range(int(number)):
        print("hello smart " + name)
