# Daily Discord Notification

This project aims to send a daily notification to a Discord channel using a bot. The notification is scheduled to be sent automatically every day at a specific time.

## Technologies Used

- **Python**: Programming language used to create the bot script.
- **Discord.py**: Library for interacting with the Discord API.
- **GitHub Actions**: For automating the sending of messages on a scheduled basis.

## Setup

### Prerequisites

Before running the project, you need to:

1. Have a Discord account.
2. Create a bot on Discord and obtain the authentication token.
3. Add the bot to your server.
4. Create a channel where the notifications will be sent.

### Environment Variables

You should configure the following environment variables in GitHub Actions:

- `DISCORD_BOT_TOKEN`: Token of the Discord bot.
- `DISCORD_CHANNEL_ID`: ID of the Discord channel where the notifications will be sent.

### Installing Dependencies

The required dependencies can be installed using `pip`. Run the following commands:

```bash
pip install discord.py python-dotenv
