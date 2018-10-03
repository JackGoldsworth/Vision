class CommandInfo:
    definition = None
    usage = None
    parser_info = None

    def __init__(self, definition, usage, parser_info):
        self.definition = definition
        self.usage = usage
        self.parser_info = parser_info
