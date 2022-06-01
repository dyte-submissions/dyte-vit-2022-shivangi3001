import click
import part1


@click.command()
@click.option('-i', '-n', help="Enter your pathfile",
              required=True, prompt="your pathfile?")
@click.argument('depend')
def supercli(i, depend):
    '''
        this is a docstring which tells about
        working of supercli library
    '''
    filepath = i
    dependency = depend
    z = dependency.split("@")
    # print(z[1])

    part1.wel(filepath, z[1])
