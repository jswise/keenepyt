"""Define the HelloInput class."""

from keenepyt.core.pyttool import PYTTool

class HelloInput(PYTTool):
    """Gets input, then says hello."""

    def init_parameter_info(self):
        """Set the parameters for the tool."""

        self.add_param(
            'name',
            'Your name',
            datatype='GPString',
            defaultValue='Rumpelstiltskin'
        )

    def execute(self, parameters, messages):
        """Say hello."""

        params = self.get_param_val_dict(parameters)
        name = params['name']
        self.info('Hello, {}!'.format(name))
