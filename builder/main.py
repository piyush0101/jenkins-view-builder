import logging
import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class JenkinsViewBuilder(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(JenkinsViewBuilder, self).__init__(
            description="Jenkins View Builder",
            version=0.1,
            command_manager=CommandManager('builder.commands'),
        )

    def initialize_app(self, argv):
        self.log.debug("Initialize app")

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    jenkins_view_builder = JenkinsViewBuilder()
    return jenkins_view_builder.run(argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
