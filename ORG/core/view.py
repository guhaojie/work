class View:
    def show_level_1_title(title):
        print(f"\n{'='*30}\n{title}\n{'='*30}\n")

    def show_level_2_title(title):
        print(f"\n{'-'*30}\n{title}\n{'-'*30}\n")

    def show_message(message):
        print(f"{message}")

    def get_message(prompt):
        return input(f"{prompt} ").strip()