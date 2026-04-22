from payment_adapter import PaymentAdapter
from legacy_pay import LegacyPay


def main() -> None:
    legacy = LegacyPay()
    adapter = PaymentAdapter(legacy)


    adapter.pay(100.0)


if __name__ == "__main__":
    main()
