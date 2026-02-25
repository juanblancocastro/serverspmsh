# SPMSH Server - Energy Consumption Monitoring System

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-4.0+-green)
![Flask](https://img.shields.io/badge/Flask-2.0+-orange)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)

A comprehensive server system for monitoring energy consumption in elderly people's homes using Arduino IoT devices. The system includes a REST API for data collection, a MongoDB database for storage, and a Telegram bot for alerts and information retrieval.

## Overview

SPMSH (Sistema de Prevención de Muerte en Soledad en Hogares) is designed to prevent unexpected health incidents in elderly individuals living alone by monitoring their household energy consumption patterns. Abnormal consumption patterns can indicate potential emergencies or health issues.

### Architecture

```
Arduino Devices
      ↓
   REST API (Flask)
      ↓
  MongoDB Database
      ↓
  Telegram Bot
```

## Features

- **IoT Data Collection**: Arduino devices send real-time energy consumption data via HTTP requests
- **REST API**: Scalable Flask-based API for receiving, validating, and storing consumption data
- **Data Storage**: MongoDB integration for flexible, scalable data persistence
- **Smart Alerts**: Telegram bot analyzes consumption patterns and alerts on anomalies
- **Device Management**: Retrieve information about registered devices and their status
- **User-Friendly Interface**: Simple Telegram commands for non-technical users
- **Anomaly Detection**: Automatically identify unusual consumption patterns that may indicate emergencies

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: MongoDB
- **Bot**: Python Telegram Bot
- **Hardware**: Arduino microcontroller
- **Communication**: HTTP/REST API

## Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB 4.0 or higher
- Arduino devices with WiFi capability
- Telegram Bot Token (obtain from [@BotFather](https://t.me/botfather))

### API Endpoints

#### Submit Energy Data
```bash
POST /api/data
Content-Type: application/json

{
  "device_id": "device_001",
  "consumption": 1250.5,
  "timestamp": "2024-02-24T10:30:00Z"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Data stored successfully"
}
```

#### Retrieve Device Information
```bash
GET /api/device/<device_id>
```

**Response:**
```json
{
  "device_id": "device_001",
  "last_update": "2024-02-24T10:30:00Z",
  "current_consumption": 1250.5,
  "average_consumption": 1180.3,
  "status": "active"
}
```

#### Get All Devices
```bash
GET /api/devices
```

### Telegram Bot Commands

The Telegram bot provides simple commands for monitoring and managing devices:

- `/start` - Display welcome message and available commands
- `/device <device_id>` - Get current status and information for a specific device
- `/consumption <device_id>` - Get consumption history for a device
- `/alert <device_id> <threshold>` - Set custom alert threshold for a device
- `/status` - Get overall system status
- `/help` - Display available commands

### Example Bot Interaction

```
User: /device device_001
Bot: 📊 Device device_001
    Status: Active
    Current Consumption: 1250.5 W
    Average: 1180.3 W
    Last Update: 2 minutes ago
    ⚠️ Consumption is 5% above average
```

## Database Schema

### Collections

#### `devices`
```json
{
  "_id": ObjectId,
  "device_id": "string",
  "location": "string",
  "registered_at": ISODate,
  "active": boolean
}
```

#### `consumption_data`
```json
{
  "_id": ObjectId,
  "device_id": "string",
  "consumption": float,
  "timestamp": ISODate,
  "anomaly_detected": boolean
}
```

#### `alerts`
```json
{
  "_id": ObjectId,
  "device_id": "string",
  "alert_type": "string",
  "message": "string",
  "created_at": ISODate,
  "sent": boolean
}
```

## Deployment

### Using the Deployment Script

```bash
chmod +x deploy.sh
./deploy.sh
```

The deployment script handles:
- Installing dependencies
- Configuring MongoDB
- Setting up systemd services for API and bot
- Starting both services

### Manual Deployment

1. Set up a systemd service for the API:
   ```bash
   sudo nano /etc/systemd/system/spmsh-api.service
   ```

2. Set up a systemd service for the bot:
   ```bash
   sudo nano /etc/systemd/system/spmsh-bot.service
   ```

3. Start services:
   ```bash
   sudo systemctl start spmsh-api
   sudo systemctl start spmsh-bot
   ```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MONGO_URI` | MongoDB connection string | Yes |
| `MONGO_DB` | Database name | Yes |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token from @BotFather | Yes |
| `TELEGRAM_CHAT_ID` | Default chat ID for alerts | No |
| `API_HOST` | API server host address | No (default: 0.0.0.0) |
| `API_PORT` | API server port | No (default: 5000) |
| `API_SECRET_KEY` | Secret key for authentication | Yes |
| `FLASK_ENV` | Flask environment (development/production) | No (default: production) |


## Project Structure

```
serverspmsh/
├── src/                    # Source code modules
├── api.py                 # Flask API server
├── bot.py                 # Telegram bot
├── deploy.sh              # Deployment script
├── .env.spmsh             # Example environment configuration
├── Pipfile                # Python dependencies
├── Pipfile.lock           # Locked dependency versions
└── README.md              # This file
```


## Acknowledgments

- Built with Flask and Python
- MongoDB for reliable data storage
- Python Telegram Bot library
- Arduino community for IoT solutions
