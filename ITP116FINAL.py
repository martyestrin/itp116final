# NAME: Marty Estrin
# ID: 1737382745
# DATE: 2022-11-29
# DESCRIPTION: This program supports two primary features. The first is for a user to receive information about a
# continent, country or capital city (all of which are derived classes). The second feature is for a user to
# contribute new information about a continent, country or capital city that they can refer to later in the
# "learn" feature

class Continent:
    # Constructor
    def __init__(self, continent: str, countries: []):
        self.continentName = continent
        self.listOfCountries = countries  # List containing countries in a continent
        self.addedInfo = []  # List that will contain the new information users add
        self.sources = []  # List that will contain names of users who contributed information

    def addinfo(self) -> None:
        new_info = input("State your contribution: ")  # Prompt user for information
        self.addedInfo.append(new_info)  # Add the new contribution to the list

    def getsource(self) -> None:
        name = input("What is your name? ")  # Prompt user for information
        self.sources.append(name)  # Save the name into the sources list
        print("Thanks, " + name + " for contributing information about this continent.")


class Country(Continent):
    def __init__(self, continent: str, country: str, countries: []):
        super().__init__(continent, countries)  # Inherit addInfo and getSource functions
        self.countryName = country  # New data member for country objects

    def getsource(self) -> None:  # Override function to have different functionality for this class
        name = input("What is your name? ")
        self.sources.append(name)
        print("Thanks, " + name + " for contributing information about this country.")  # Say that it is a country


class CapitalCity(Country):
    def __init__(self, continent: str, countries: [], country: str, capital: str):
        super().__init__(continent, countries, country)  # Inherit addInfo and getSource functions
        self.capCityName = capital  # Capital city objects need data member to store their name

    def getsource(self) -> None:  # Override inherited function for CapitalCity class
        name = input("What is your name? ")
        self.sources.append(name)
        print("Thanks, " + name + " for contributing information about this capital city.")  # State that it's a capital


def read_file():
    fileptr = open("continentscountries.txt", "r")
    names = fileptr.readline().strip()  # First line contains names of all 7 continents
    continents = names.strip().split(",")  # Create list containing names of all 7 continents

    continent_objects = []  # List of continent objects
    country_objects = []  # List of country objects
    capitals_objects = []  # List of capital city objects

    gdp = {}  # Dictionary with continent objects as keys and their respective share of world GDP as the value

    for i in range(0, 7):
        num = fileptr.readline().strip()
        numCountries = int(num)
        countries = []  # Store strings of countries in current continent
        capitals = []  # Store strings of capitals in current continent

        for j in range(0, numCountries):
            nation = fileptr.readline().strip()
            countries.append(nation)  # Generating list containing all countries in a given continent

        for k in range(0, numCountries):  # Number of capital cities is the same as the number of countries
            capital = fileptr.readline().strip()
            capitals.append(capital)  # Generate list of capital cities in the continent

        continent = Continent(continents[i], countries)  # Create continent object
        continent_objects.append(continent)  # Add object to list of continent objects

        for l in range(0, numCountries):
            continent = continents[i]  # Get string of current continent name
            country = Country(continent, countries[l], countries)  # Create country objects
            country_objects.append(country)  # Add object to list

            capital = CapitalCity(continent, countries, countries[l], capitals[l])  # Create capital city object
            capitals_objects.append(capital)  # Add object to the list

            # Add to dictionary where key is the continent object and value is that continent's share of world GDP
            if i == 0:
                gdp[continents[i]] = 28.3  # Key is north america instance
            elif i == 1:
                gdp[continents[i]] = 2.9  # Key is africa instance
            elif i == 2:
                gdp[continents[i]] = 40.5  # Key is asia instance
            elif i == 3:
                gdp[continents[i]] = 22.7  # Key is europe instance
            elif i == 4:
                gdp[continents[i]] = 1.9  # Key is australia instance
            elif i == 5:
                gdp[continents[i]] = 0.1  # Key is antarctica instance
            elif i == 6:
                gdp[continents[i]] = 3.6  # Key is south america instance

    return continents, continent_objects, country_objects, capitals_objects, gdp


def main_menu() -> int:
    # Message for user
    global user_choice  # Global variable
    print("Choose an option below:")
    print("1. Learn")
    print("2. Contribute")
    print("3. Exit")

    try:
        user_choice = int(input("Enter 1, 2 or 3: "))  # Get input from user
    except ValueError:
        return 0

    return user_choice


def learn(list_of_continents, continents, countries, capitals, c_gdp) -> None:
    global user_country  # Global variable
    print("Please select a continent from the following list:")
    print(list_of_continents)  # Show user list of countries
    user_continent = input("")  # Get user input

    # Check if user enters invalid continent
    while user_continent not in list_of_continents:
        print("Invalid Entry.")
        user_continent = input("Please select a continent from the list: ")

    for i in range(0, len(continents)):
        # Identify the continent
        if continents[i].continentName == user_continent:
            # Only print additional information if it exists
            if len(continents[i].addedInfo) != 0:
                print("")
                print(continents[i].addedInfo)
                print("Information provided by:", continents[i].sources)

            # Use dictionary key (current continent instance) to produce the value (their share of world GDP)
            print('\n' + continents[i].continentName + " accounts for " + str(
                c_gdp[continents[i].continentName]) + "% of "
                                                      "world "
                                                      "GDP.")

            # Prompt user to give country
            print('\n' + "Please select a country in " + user_continent + ":")
            # Show user countries in their selected continent
            print(continents[i].listOfCountries)
            user_country = input("")

            # Check that user provided a valid country
            while user_country not in continents[i].listOfCountries:
                print("Invalid Entry.")
                user_country = input("Please select a continent from the list. ")

            for n in range(0, len(countries)):
                # Identify user-provided country
                if countries[n].countryName == user_country:
                    # State the capital of the country
                    print('\n' + "The capital of", countries[n].countryName, "is", capitals[n].capCityName + '\n')
                    # Provide additional information about country if it exists
                    if len(countries[n].addedInfo) != 0:
                        print("")
                        print(countries[n].addedInfo)
                        print("Information provided by:", countries[n].sources)
                    # Provide additional information about capital city if it exists
                    if len(capitals[n].addedInfo) != 0:
                        print("")
                        print(capitals[n].addedInfo)
                        print("Information provided by:", capitals[n].sources)
                        print("")


def contribute(continents, countries, capitals) -> None:
    # Ask user to state continent, country or capital city
    user_choice = input("For which continent/country/capital city are you contributing information? ")
    valid = False

    # If user entered a continent
    for i in range(0, len(continents)):
        if continents[i].continentName == user_choice:
            continents[i].addinfo()  # Calls addInfo function
            continents[i].getsource()  # Calls getSource function
            print("")
            valid = True

    # If user entered a country
    for i in range(0, len(countries)):
        if countries[i].countryName == user_choice:
            countries[i].addinfo()  # Calls addInfo function
            countries[i].getsource()  # Calls overloaded getSource function
            print("")
            valid = True

    # If user entered a capital city
    for i in range(0, len(capitals)):
        if capitals[i].capCityName == user_choice:
            capitals[i].addinfo()  # Calls addInfo function
            capitals[i].getsource()  # Calls getSource function for capital city class
            print("")
            valid = True

    # This occurs if user input is not a valid continent, country or capital city
    if not valid:
        print("Sorry, you did not enter a valid continent/country/capital city." + '\n')


def main():
    list_of_continents, continents, countries, capitals, continent_gdp = read_file()
    decision = main_menu()  # Print menu and get input from user
    while decision != 3:
        if decision == 1:
            learn(list_of_continents, continents, countries, capitals, continent_gdp)  # Calls "learn" method
            decision = main_menu()
        elif decision == 2:
            contribute(continents, countries, capitals)  # Calls "contribute" method
            decision = main_menu()
        elif decision == 0:  # This is the exception case from the MainMenu function, if user didn't enter an integer
            print("Error: Enter an integer" + '\n')
            decision = main_menu()
        else:
            print("Error: Integer must be between 1 and 3" + '\n')  # If user entered an integer out of range
            decision = main_menu()
    print("Goodbye!")  # When user wants to quit


if __name__ == "__main__":
    main()
