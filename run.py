import yaml
from checkers.replication import ReplicationChecker
from notifiers.slack import SlackNotifier

if __name__ == '__main__':
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
