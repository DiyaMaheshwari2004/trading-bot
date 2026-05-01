# Binance Trading Bot

A Python CLI trading bot using Binance Spot Testnet API.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Input validation
- Logging system
- Error handling
- CLI interface using Typer
- Binance Testnet integration

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── bot.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/DiyaMaheshwari2004/trading-bot.git
```

## Move Into Project Folder

```bash
cd trading_bot
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root and add:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

# Run MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

---

# Run LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 90000
```

---

# Logs

Logs are stored inside:

```text
logs/bot.log
```

---

# Validation Included

- BUY/SELL validation
- MARKET/LIMIT validation
- Quantity validation
- LIMIT order price validation

---

# Error Handling

The project handles:

- Invalid input
- API issues
- Invalid quantity
- Missing price
- Binance request failures

---

# Technologies Used

- Python
- Typer
- python-binance
- python-dotenv
- Logging module

---

# Binance Testnet

This project uses Binance Spot Testnet API for testing purposes.

Official Testnet:

https://testnet.binance.vision/

---

# Important

Do not share your `.env` file or API keys publicly.

## Note

Due to regional restrictions on Binance Futures Testnet access,
Binance Spot Testnet API was used to demonstrate
authentication, order placement, logging, validation,
and error handling.
