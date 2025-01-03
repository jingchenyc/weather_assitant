# Weather Assistant - Project of ccClub

A Python-based Line Bot that provides real-time weather updates and clothing recommendations by fetching data from the Central Weather Bureau API. Deployed using Google Cloud Functions for automated and scheduled execution.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How to Run](#how-to-run)
- [Debugging Notes](#debugging-notes)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Introduction

Weather Assistant is a collaborative project aimed at creating a Line Bot that provides users with weather forecasts, rain probability, and clothing suggestions based on the latest meteorological data. The bot fetches data from the Central Weather Bureau's API and is deployed using Google Cloud Functions.

<img width="771" alt="Screenshot 2024-10-01 at 12 09 51 PM" src="https://github.com/user-attachments/assets/67696345-2bae-4202-9922-90e2f797d894">


## Features

- **Real-Time Weather Data**: Fetches current weather observations and 36-hour forecasts.
- **Rain Gear Suggestions**: Advises users on whether to carry rain gear based on rain probability.
- **Clothing Recommendations**: Provides clothing suggestions based on temperature and comfort index.
- **Chinese Character Recognition**: Recognizes both traditional and simplified Chinese characters.
- **Automated Execution**: Deployed on Google Cloud Functions for scheduled tasks.
- **Line Bot Integration**: Users can interact with the bot through the Line messaging app.

## Project Structure

- `linebot_main.py`: The main script for the Line Bot webhook.
- `linebot_get_weather.py`: Contains functions to fetch and process weather data.
- `linebot_requirements.txt`: Lists all the dependencies required for the project.

## Prerequisites

- Python 3.9 or above
- Line Developer Account
- Google Cloud Platform Account
- Libraries listed in `requirements.txt`
- Access to the Central Weather Bureau API

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jingchenyc/weather-assistant.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd linebot_weather-assistant
   ```

3. **Install Required Libraries**

   ```bash
   pip install -r linebot_requirements.txt
   ```

## Usage

### Setting Up the Line Bot

1. **Create a Line Channel**

   - Follow the instructions on [Oxxo Studio's Line Developer Tutorial](https://steam.oxxostudio.tw/category/python/example/line-developer.html).
   - Obtain your `Channel Secret` and `Channel Access Token`.

2. **Enable Webhook**

   - Set up your webhook URL in the Line Developer Console.
   - Use Google Cloud Functions URL as your webhook endpoint.

### Deploying to Google Cloud Functions

1. **Create a New Cloud Function**

   - Go to the [Google Cloud Console](https://console.cloud.google.com/functions).
   - Click on "Create Function".

2. **Configure the Function**

   - **Environment**: 2nd Generation
   - **Runtime**: Python 3.9
   - **Entry Point**: Specify the function name in `linebot_main.py`.
   - **Authentication**: Allow unauthenticated invocations.

3. **Upload Code**

   - Upload `linebot_main.py`, `linebot_get_weather.py`, and `linebot_requirements.txt`.

4. **Set Environment Variables**

   - Add your Line Bot credentials (`CHANNEL_SECRET`, `CHANNEL_ACCESS_TOKEN`).

### Setting Up API Access

- Register for access to the [Central Weather Bureau API](https://opendata.cwb.gov.tw/dist/opendata-swagger.html).
- Update the API endpoints in `get_weather.py` as needed.

## How to Run

1. **Local Testing**

   - Install dependencies:
     ```bash
     pip install -r linebot_requirements.txt
     ```
   - Run the bot locally:
     ```bash
     python linebot_main.py
     ```
   - Use a tool like `ngrok` to expose your local server for webhook testing.

2. **Deploying to Cloud Functions**

   - Use the `gcloud` CLI for deployment:
     ```bash
     gcloud functions deploy weather-assistant \
       --runtime python39 \
       --trigger-http \
       --allow-unauthenticated \
       --entry-point YOUR_ENTRY_POINT \
       --source .
     ```
     Replace `YOUR_ENTRY_POINT` with the actual function name.

3. **Interacting with the Bot**

   - Add the Line Bot to your Line app using the provided QR code.
   - Send messages to receive weather updates and recommendations.

## Debugging Notes

- **Data Structure Differences**

  - Noticed differences in data structures between versions by Danny and Wei.
  - The order of `weatherElement`'s `elementName` varies, affecting data extraction.
  - Ensure consistent data processing by checking the API response structure.

- **Line Bot Message Handling**

  - For replying to address messages, refer to [Oxxo Studio's Line Reply Message Tutorial](https://steam.oxxostudio.tw/category/python/example/line-reply-message.html).

## Contributing

We welcome contributions from the community. Feel free to open issues or submit pull requests.

## Acknowledgments

- **Team Members**: Danny, Wei, and Ruth for their significant contributions.
- **Assistants**: Special thanks to the teaching assistant for guidance on using Cloud Functions and Line Bot integration.
- **References**:
  - [Oxxo Studio Tutorials](https://steam.oxxostudio.tw/)
  - [LearnCodeWithMike Line Notify Tutorial](https://www.learncodewithmike.com/2020/06/python-line-notify.html)
  - [Central Weather Bureau API Documentation](https://opendata.cwb.gov.tw/dist/opendata-swagger.html)
  - [Viggo Chang's Articles](https://ithelp.ithome.com.tw/m/articles/10246301)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
