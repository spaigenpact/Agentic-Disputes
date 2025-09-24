import pandas as pd
from datetime import datetime
import json

# --------------------------------------------------------------------
# Agentic CX Dispute System
# --------------------------------------------------------------------
# This system simulates the handling of a transaction dispute case
# end-to-end, including provisional credit, chargeback, settlement,
# and merchant fee assessment. It maintains an event ledger for audit.
# --------------------------------------------------------------------

class Account:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = float(balance)
    def adjust(self, amount):
        self.balance += float(amount)

# Ledger for recording all steps
ledger = []
def log(event_type, from_entity, to_entity, amount, note=""):
    ledger.append({
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "from": from_entity,
        "to": to_entity,
        "amount": round(float(amount),2),
        "note": note
    })

# Initialize actors
customer = Account("Customer: Alice", balance=0.0)
issuer = Account("Issuer Bank", balance=0.0)
network = Account("Card Network", balance=0.0)
acquirer = Account("Acquirer Bank", balance=0.0)
merchant = Account("Merchant - The Bistro", balance=10000.00)

# Transaction details
original_charge = 594.38   # incorrect posted amount
correct_total   = 237.98   # actual bill + tip
overcharge      = round(original_charge_
