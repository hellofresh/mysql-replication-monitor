import requests


class SlackNotifier(object):
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    @staticmethod
    def construct_message(
            status, short_message, long_message, time_string):
        message = '''
            {
                "text": "%s",
                "attachments": [
                    {
                        "pretext":"",
                        "color": "%s",
                        "fields": [
                            {
                                "title": "Message",
                                "value": "%s",
                                "short": true
                            },
                            {
                                "title": "Time",
                                "value": "%s",
                                "short": true
                            }
                        ]
                    }
                ]
            }
        ''' % (long_message, status, short_message, time_string)

        return message

    def notify(self, status, short_message, long_message, time_string):
        message = self.construct_message(
            status, short_message, long_message, time_string)

        request = requests.post(self.webhook_url, data=message)

        if request.status_code != 200:
            raise Exception('%s %s' % (request.status_code, request.reason))
