import time

class TelephoneSystem:
    def __init__(self):
        self.current_call = None
        self.call_status = "Idle"

    def make_call(self, number):
        if self.call_status == "Idle":
            self.current_call = number
            self.call_status = "Dialing"
            print(f"Dialing {number}...")
            time.sleep(2)  # Simulate dialing delay
            self.call_status = "Connected"
            print(f"Call connected with {number}.")
        else:
            print(f"Cannot make a call. Current status: {self.call_status}")

    def receive_call(self, number):
        if self.call_status == "Idle":
            print(f"Incoming call from {number}.")
            choice = input("Do you want to answer the call? (yes/no): ").strip().lower()
            if choice == "yes":
                self.current_call = number
                self.call_status = "Connected"
                print(f"Call connected with {number}.")
            else:
                print("Call declined.")
        else:
            print(f"Cannot receive a call. Current status: {self.call_status}")

    def hold_call(self):
        if self.call_status == "Connected":
            self.call_status = "On Hold"
            print(f"Call with {self.current_call} is now on hold.")
        else:
            print(f"Cannot hold call. Current status: {self.call_status}")

    def resume_call(self):
        if self.call_status == "On Hold":
            self.call_status = "Connected"
            print(f"Resumed call with {self.current_call}.")
        else:
            print(f"Cannot resume call. Current status: {self.call_status}")

    def end_call(self):
        if self.call_status in ["Connected", "On Hold"]:
            print(f"Ending call with {self.current_call}.")
            self.current_call = None
            self.call_status = "Idle"
        else:
            print(f"Cannot end call. Current status: {self.call_status}")

def main():
    system = TelephoneSystem()
    while True:
        print("\nTelephone System Menu:")
        print("1. Make a Call")
        print("2. Receive a Call")
        print("3. Hold Current Call")
        print("4. Resume Current Call")
        print("5. End Current Call")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            number = input("Enter the phone number to call: ").strip()
            system.make_call(number)
        elif choice == "2":
            number = input("Enter the incoming call number: ").strip()
            system.receive_call(number)
        elif choice == "3":
            system.hold_call()
        elif choice == "4":
            system.resume_call()
        elif choice == "5":
            system.end_call()
        elif choice == "6":
            print("Exiting Telephone System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
