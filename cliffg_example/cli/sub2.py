from cliffg_example import cli

class Sub2Create(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(Sub2Create, self).get_parser(prog_name)
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Create body')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class Sub2Update(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(Sub2Update, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Update resource by name')
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Update body')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class Sub2Show(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(Sub2Show, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            help='Show Resource by name')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)
