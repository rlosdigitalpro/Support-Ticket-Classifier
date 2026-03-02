
---

## 🧠 ticket_classifier.py

```python
def classify_ticket(text):
    text = text.lower()

    if any(word in text for word in ["not connecting", "no signal", "offline", "network"]):
        return "Connectivity", "High", "Run network diagnostics"

    elif any(word in text for word in ["sim", "provision", "activation"]):
        return "SIM Provisioning", "Medium", "Check SIM status and provisioning"

    elif any(word in text for word in ["invoice", "billing", "charge", "payment"]):
        return "Billing", "Medium", "Forward to billing department"

    elif any(word in text for word in ["configuration", "setup", "apn"]):
        return "Device Configuration", "Low", "Guide customer through setup steps"

    else:
        return "Unclassified", "Escalate", "Requires manual review"


def main():
    print("\n--- Support Ticket Classification Tool ---\n")
    ticket = input("Enter ticket description: ")

    category, priority, action = classify_ticket(ticket)

    print("\n--- Ticket Analysis ---")
    print(f"Category: {category}")
    print(f"Priority: {priority}")
    print(f"Suggested Action: {action}\n")


if __name__ == "__main__":
    main()
