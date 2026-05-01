import typer

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

from bot.logging_config import logger

app = typer.Typer()


@app.command()
def main(
    symbol: str = typer.Option(..., "--symbol"),
    side: str = typer.Option(..., "--side"),
    order_type: str = typer.Option(..., "--order-type"),
    quantity: float = typer.Option(..., "--quantity"),
    price: float = typer.Option(None, "--price"),
):

    try:

        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        validate_price(price, order_type)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if price:
            print(f"Price       : {price}")

        print("===================================\n")

        if order_type == "MARKET":

            response = place_market_order(
                symbol,
                side,
                quantity,
            )

        else:

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price,
            )

        print("✅ ORDER PLACED SUCCESSFULLY\n")

        print("========== RESPONSE ==========")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Price         : {response.get('price')}")
        print("==============================")

        logger.info("Order completed successfully")

    except Exception as e:

        logger.error(f"CLI Error: {e}")

        print(f"❌ ERROR: {e}")


if __name__ == "__main__":
    app()