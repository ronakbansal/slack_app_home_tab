from django.db import models

def get_app_home_block():
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":newspaper:  *ronakbansal Team Summary*  :newspaper:"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "text": "*November 07, 2019*  |  AttendanceBot Announcements",
                    "type": "mrkdwn"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\nHi :wave:, I am AttendanceBot, your friendly PTO/Time tracking bot.\nType `profile` to view and edit your profile.\n\n"
            }
        },

        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":calendar: |   *PENDING LEAVE REQUESTS*  | :calendar: "
            }
        },

        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*You have a new leave request for approval.*"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Leave Type:*\nVacation"
                },
                {
                    "type": "mrkdwn",
                    "text": "*When:*\nSubmitted Nov 10"
                },
                {
                    "type": "mrkdwn",
                    "text": "*Applied By:*\nGregg"
                },
                {
                    "type": "mrkdwn",
                    "text": "*Reason:*\nDon't wish to tell."
                },
            ]
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Approve"
                    },
                    "style": "primary",
                    "value": "click_me_123"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Deny"
                    },
                    "style": "danger",
                    "value": "click_me_123"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":calendar: |   *YOUR TEAM TODAY*  | :calendar: "
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<@U1Y4FG6PP>, <@U9ZM6J67P> are on leave today."
            },

        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*FOR YOUR INFORMATION*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "➕ Got questions, suggestions or feature requests? Type `dialm` to open a support ticket."
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "👀 Check out your <https://www.attendancebot.com/accounts/leave/commands/|team's cheat sheet>\n❓Get help any time by typing *help* in a DM with me"
                }
            ]
        }
        ]
    return blocks
