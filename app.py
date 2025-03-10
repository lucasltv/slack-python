import os
from slack_sdk.webhook import WebhookClient


url = os.getenv(
    "SLACK_WEBHOOK_URL",
    "https://hooks.slack.com",
)
webhook = WebhookClient(url)
response = webhook.send(
    text="fallback",
    blocks=[
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*",
            },
        }
    ],
)
