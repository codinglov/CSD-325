def beer_song(number_of_bottles):
    while number_of_bottles > 0:
        if number_of_bottles > 1:
            print(f"{number_of_bottles} bottles of beer on the wall, {number_of_bottles} bottles of beer.")
            print(f"Take one down, pass it around, {number_of_bottles - 1} bottles of beer on the wall.\n")
        else:
            print(f"{number_of_bottles} bottle of beer on the wall, {number_of_bottles} bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.\n")
        number_of_bottles -= 1

def main():
    try:
        bottles = int(input("Enter number of bottles on the wall? "))
        if bottles <= 0:
            print("Please enter a positive number.")
        else:
            beer_song(bottles)
            print("Time to buy more beer!")
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit(1)

if __name__ == "__main__":
    main()