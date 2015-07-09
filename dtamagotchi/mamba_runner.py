import argparse
from django.test.runner import DiscoverRunner
from mamba import application_factory


class MambaSpecRunner(DiscoverRunner):

    def run_tests(self, test_labels, extra_tests=None):
        self.setup_test_environment()
        old_config = self.setup_databases()

        parser = argparse.ArgumentParser()
        parser.add_argument('--version', '-v', default=False,
                            action='store_true', help='Display the version.')
        parser.add_argument('--slow', '-s', default=0.075, type=float,
                            help='Slow test threshold in seconds (default: %(default)s)')
        parser.add_argument('--enable-coverage', default=False, action='store_true',
                            help='Enable code coverage measurement (default: %(default)s)')
        parser.add_argument('--format', '-f', default='documentation', action='store',
                            choices=['documentation', 'progress'], help='Output format (default: %(default)s)')
        parser.add_argument('specs', default=[
                            'spec', 'specs'], nargs='*', help='Specs or directories with specs to run (default: %(default)s)')
        parser.add_argument('--no-color', default=False, action='store_true',
                            help='Turn off all output coloring (default: %(default)s)')
        parser.add_argument('--watch', '-w', default=False, action='store_true',
                            help='Enable file watching support - not available with python3 (default: %(default)s)')

        arguments = parser.parse_args(['dtamagotchi/spec'])
        factory = application_factory.ApplicationFactory(arguments)
        runner = factory.create_runner()
        runner.run()
        self.teardown_databases(old_config)
        self.teardown_test_environment()
        if runner.has_failed_examples:
            return runner.reporter.failed_count
