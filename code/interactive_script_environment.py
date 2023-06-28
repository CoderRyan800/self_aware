# interactive_script.py

from environment import Environment

def main():
    num_agents = 5
    recursive_limit = 10
    env = Environment(num_agents, recursive_limit)

    user_input = input("Enter your message (type 'exit' to end): ")

    env.send_message(user_input, 0)

if __name__ == "__main__":
    main()
