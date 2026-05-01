from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):

    logger.info(
        f"MARKET ORDER | Symbol={symbol} Side={side} Quantity={quantity}"
    )

    response = client.create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity,
    )

    logger.info(f"Market Order Response: {response}")

    return response


def place_limit_order(symbol, side, quantity, price):

    logger.info(
        f"LIMIT ORDER | Symbol={symbol} Side={side} Quantity={quantity} Price={price}"
    )

    response = client.create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        timeInForce="GTC",
        quantity=quantity,
        price=price,
    )

    logger.info(f"Limit Order Response: {response}")

    return response