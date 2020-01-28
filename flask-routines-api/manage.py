import os
import sys
from argparse import ArgumentParser

from routines.models import Routine


def run_command(opts):
    from routines import app
    app.run(debug=True)


def create_tables_command(opts):
    if not Routine.exists():
        print('Creating routine table...')
        Routine.create_table(
            read_capacity_units=4,
            write_capacity_units=2,
            wait=True
        )
        print('Done.')


def delete_tables_command(opts):
    if Routine.exists():
        print('Delete routine table...')
        Routine.delete_table()
        print('Done.')


def create_parser(prog_name):
    parser = ArgumentParser(prog=prog_name, description='Flask app dev CLI')

    sp = parser.add_subparsers(title='commands')
    run = sp.add_parser('run', help='Run the application')
    run.set_defaults(func=run_command)

    create_tables = sp.add_parser('create-tables', help='Create DynamoDB table schemas')
    create_tables.set_defaults(func=create_tables_command)

    delete_tables = sp.add_parser('delete-tables', help='Delete DynamoDB table schemas')
    delete_tables.set_defaults(func=delete_tables_command)

    return parser


def main():
    parser = create_parser(sys.argv[0])
    parser.add_argument('--prefix', metavar='NAME', default=None,
                        help='Set DynamoDB table prefix')
    parser.add_argument('--region', metavar='REGION', default=None,
                        help='Set DynamoDB region')
    opts = parser.parse_args(sys.argv[1:])

    if opts.prefix:
        os.environ['DYNAMO_PREFIX'] = opts.prefix
    if opts.region:
        os.environ['DYNAMO_REGION'] = opts.region
    if not hasattr(opts, 'func'):
        parser.print_help(sys.stderr)
        return 1
    opts.func(opts)


if __name__ == '__main__':
    main()
