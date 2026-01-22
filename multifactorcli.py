# multifactorcli.py'

class MultiFactorAuth:
    def __init__(self):
        # Stored credentials (normally from a DB or file)
        self.username = "admin"
        self.password = "secret"

    def set_multiFactorAuthentication(self, question, answer):
        self.question = question
        self.security_answer = answer.lower()

    def authenticate_user(self):
        print("\n=== Multi-Factor Authentication System ===")

        # Step 1: Username / Password
        user = input("Enter username: ").strip()
        pwd = input("Enter password: ").strip()

        if user != self.username or pwd != self.password:
            print("\n❌ Authentication failed: Invalid username or password.")
            return False

        print("\n✔ Username and password accepted.")

        # Step 2: Security Question
        print("\nSecurity Question:")
        print(self.question)
        answer = input("Answer: ").strip().lower()

        if answer != self.security_answer:
            print("\n❌ Authentication failed: Incorrect security answer.")
            return False

        print("\n✔ Security factor accepted.")
        return True

    def restricted_app(self):
        print("\n==============================")
        print("🎉 Congratulations!")
        print("You have authenticated successfully.")
        print("This is a RESTRICTED application.")
        print("==============================\n")

    def run(self):
        if self.authenticate_user():
            self.restricted_app()
        else:
            print("\nAccess denied.\n")


# Run the program
if __name__ == "__main__":
    app = MultiFactorAuthCLI()
    app.run()
