import requests
from colorama import Fore, Style, init

init(autoreset=True)

def fetch_player_stats(username):
    api_url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors

        lines = response.text.split("\n")
        skills = [line.split(",") for line in lines]

        # Filter out empty lines or lines without enough elements
        skills = [skill for skill in skills if len(skill) == 3]

        # Create a dictionary mapping skill names to levels
        skill_names = ['Overall', 'Attack', 'Defence', 'Strength', 'Hitpoints', 'Ranged', 'Prayer', 'Magic',
                       'Cooking', 'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing',
                       'Mining', 'Herblore', 'Agility', 'Thieving', 'Slayer', 'Farming', 'Runecraft', 'Hunter',
                       'Construction']
        
        stats = {skill_names[i]: int(skill[1]) for i, skill in enumerate(skills)}
        return stats

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching player stats: {e}{Style.RESET_ALL}")
        return None

def display_player_stats(username, stats):
    if stats:
        print(f"{Fore.GREEN}\nStats for {Fore.YELLOW}{username}:{Style.RESET_ALL}\n")
        for skill, level in stats.items():
            print(f"{Fore.GREEN}{skill.capitalize()}:{Fore.RESET} {level}")

def main():
        while True:
            try:
                player_username = input(f"{Fore.YELLOW}Enter the OSRS player's username: {Style.RESET_ALL}")
                player_stats = fetch_player_stats(player_username)

                if player_stats:
                    display_player_stats(player_username, player_stats)

                search_again = input(f"{Fore.YELLOW}Do you want to search for another player? (yes/no): {Style.RESET_ALL}").lower()
                if search_again == 'no':
                    print(f"{Fore.YELLOW}Exiting the program.{Style.RESET_ALL}")
                    break
                elif search_again == 'yes':
                    continue

            except Exception as e:
                print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()