from cliffg_example import cli

class Sub1Create(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(Sub1Create, self).get_parser(prog_name)
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Create body')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)


class Sub1Show(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(Sub1Show, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            help='Show Resource by name')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)


class Sub1List(cli.Lister):
    def get_parser(self, prog_name):
        parser = super(Sub1List, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)


class Sub1Delete(cli.Command):
    def get_parser(self, prog_name):
        parser = super(Sub1Delete, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Delete resource by name')
        return parser

    def take_action(self, parsed_args):
        return 'deleted'

