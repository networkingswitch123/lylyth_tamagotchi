import random
import datetime


class GothGirlTamagotchi:
    def __init__(self):
        self.hunger = 5  # 0 = full, 10 = starving
        self.mood = "brooding"
        self.last_fed = None
        self.favorite_activities = [
            "listening to Sisters of Mercy",
            "listening to The Cure",
            "listening to Siouxsie and the Banshees",
            "listening to Slipknot",
            "listening to Korn",
            "watching horror movies",
            "reading dark poetry",
            "writing in her journal",
            "drawing in her sketchbook", 
            "coding",
            "gaming",
            "making art",
            "writing poetry",
            "reading gothic novels"
        ]
        self.favorite_foods = [
            "Mole",
            "Birria",
            "Tamales",
            "Pozole",
            "Tacos de Canasta",
            "Taquitos",
            "Udon",
            "Ramen",
            "Sushi",
            "Sashimi",
            "Katsu",
            "Karaage",
            "Soba",
            "Soba noodles",
            "Japanese Curry",
            "Soba soup",
            "Breakfast with Yakizakana",
            "Black coffee"
        ]
        self.mood_level = 5  # 0 = gloomy, 10 = delighted

    def get_time_period(self):
        now = datetime.datetime.now(datetime.timezone(-datetime.timedelta(hours=5)))  # EST timezone (UTC-5)
        hour = now.hour
        if 6 <= hour < 12:
            return "asleep"
        elif 16 <= hour < 24:
            return "working"
        else:  # 0 <= hour < 6
            return random.choice(self.favorite_activities)

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            self.last_fed = datetime.datetime.now()
            food = random.choice(self.favorite_foods)
            print(f"You gave her some {food}. She nods in appreciation.")
        else:
            print("She's not hungry right now.")

    def massage(self):
        if self.mood_level < 10:
            self.mood_level += 2
            print("You give her a gentle massage. She relaxes and her mood improves.")
        else:
            print("She's already in a great mood!")

    def clean_apartment(self):
        if self.mood_level < 10:
            self.mood_level += 1
            print("You clean her apartment. Wearing your little maid outfit. She appreciates your effort and her mood lifts a little.")
        else:
            print("Her apartment is spotless and she's already happy!")

    def status(self):
        activity = self.get_time_period()
        print(f"Miss Lylyth is currently {activity}.")
        print(f"Hunger level: {self.hunger}/10")
        print(f"Mood level: {self.mood_level}/10")
        
        # Handle different activities
        if activity == "asleep":
            sleep_states = [
                "She is peacefully asleep, dreaming of moonlit cemeteries.",
                "She's sleeping soundly, her dark lipstick still perfectly applied.",
                "She's wrapped in her velvet blanket, dead to the world.",
                "She's sleeping like a vampire in daylight, completely still.",
                "She's muttering about darkness and poetry in her sleep."
            ]
            print(random.choice(sleep_states))
        elif activity == "working":
            print("She's focused on her work, occasionally glancing your way.")
            # Still check mood and hunger while working
            self._check_mood_and_hunger()
        else:  # She's doing one of her favorite activities
            print(f"She seems to be enjoying {activity}.")
            # Check mood and hunger during activities
            self._check_mood_and_hunger()
    
    def _check_mood_and_hunger(self):
        # Handle hunger states
        if self.hunger >= 8:
            print("She looks pale and hangry. Maybe feed her?")
        elif self.hunger <= 2:
            print("She seems content, sipping her coffee.")
        else:
            print("She sighs and stares out the window.")
        
        # Handle mood states
        if self.mood_level <= 3:
            print("She seems extra gloomy. Maybe do something nice for her?")
        elif self.mood_level >= 8:
            print("She actually smiles a little. Well done!")
        
        # Handle spicy tasks - fixed the condition to make it more likely to occur
        if self.mood_level > 6 and random.random() < 0.3:  # 30% chance when mood > 6
            spicy_tasks = [
                    "She's feeling a little sadistic, she asks you to tie up your member and slap it 10 times.",
                    "She pulls your pants down and puts a chastity cage on you. She tells you to thank her for it.",
                    "She tells you spank yourself while she watches.",
                    "She wants you to pose dramatically while she sketches you.",
                    "She in the mood, she sits and pats her lap, asking you to kneel before her. She disrobes you and tells you to worship her.",
                    "You see she's wearing her strap on, she tells you to get on your knees and beg for it.",
                    "Before you know it, she's got you on all fours, telling you to crawl to her.",
                    "She hands you a whip and tells you to spank yourself while she watches.",
                    "She tells you to put on a collar and kneel before her, she wants to see you submit.",
                    "Without even seeing her, she snatches you up and before you know it, your bent over her lap, she tells you to count the spanks and thank her for each one."
                ]
            print(f"She's in a commanding mood. {random.choice(spicy_tasks)}")

def main():
    pet = GothGirlTamagotchi()
    print("Welcome to Miss Lylyth Tamagotchi!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed her")
        print("2. Check on her")
        print("3. Massage her")
        print("4. Clean her apartment")
        print("5. Quit")
        choice = input("> ")
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.status()
        elif choice == "3":
            pet.massage()
        elif choice == "4":
            pet.clean_apartment()
        elif choice == "5":
            print("Goodbye. She waves 'bye slut!'")
            break
        else:
            print("She raises an eyebrow. Try again. Don't make her mad!")

if __name__ == "__main__":
    main()
