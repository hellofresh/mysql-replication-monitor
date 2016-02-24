import yaml
import logging
import datetime

from checkers.replication import ReplicationChecker
from notifiers.slack import SlackNotifier


if __name__ == '__main__':
    logging.basicConfig(filename='replication.log', level=logging.DEBUG)
    logging.info('Checker started at: ' + datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S'))
    config = yaml.load((open('config.yml', 'r').read()))

    notifier = SlackNotifier(webhook_url=config['webhook_url'])
    checker = ReplicationChecker(
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        host=config['mysql']['host'],
        port=config['mysql']['port']
    )
    checker.add_notifier(notifier)

    checker.check()
    logging.info('Checker ended at: ' + datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S'))
