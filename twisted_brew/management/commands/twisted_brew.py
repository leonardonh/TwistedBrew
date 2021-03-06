#!/usr/bin python

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation

from core.utils import coreutils
import core.defaults as defaults
import core.utils.logging as log
from core.master import Master


class Command(BaseCommand):
    help = 'Starts the Twisted Brew master and or workers according to the given config file'
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('config')

    def handle(self, *args, **options):
        from django.conf import settings
        translation.activate(settings.LANGUAGE_CODE)
        if len(options) > 0:
            config_file = options['config']
        else:
            config_file = defaults.DEFAULT_CONFIG
        try:
            self.stdout.write('Starting Twisted Brew (config:{0})'.format(config_file))
            master = None
            config = coreutils.parse_config(config_file)
            if config.master is not None:
                master = Master(config.communication, config.master)
            coreutils.start_workers(config)
            if master is not None:
                master.info()
                master.start()
            else:
                log.set_log_receiver(log.LOG_RECEIVER_STD)
        except Exception as e:
            raise CommandError('Could not start Twisted Brew: {0}'.format(e.__class__.__name__))
        self.stdout.write('Successfully started Twisted Brew')
