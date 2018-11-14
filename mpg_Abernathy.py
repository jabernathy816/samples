import csv

FILENAME = "trips.csv"


def write_trips(trips):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)


def main():
    print("Miles Per Gallon Program\n")

    trips = []

    while True:
        miles = int(input("Enter Miles Driven: "))
        gallons = int(input("Enter Gallons of Gas Used: "))

        mpg = miles / gallons
        mpg = round(mpg, 2)

        trip = [miles, gallons, mpg]

        trips.append(trip)

        print("Miles Per Gallon: " + str(mpg) + "\n")

        print("Distance Gallons\tMPG")

        for trip in trips:
            print(str(trip[0]), "\t\t", str(trip[1]), "\t   ", str(trip[2]), "\t\t")

        response = input("\nMore entries? (y or n): ")

        if response.lower == "y":
            print()
            continue
        if response.lower() == "n":
            write_trips(trips)
            break

    print("\nGoodbye!")


if __name__ == "__main__":
    main()
