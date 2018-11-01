beer = 99
# prints out the entiretey of "bottles of beer on the wall"
for wall in range (99, 0, -1):
    lyrics = ("{0} bottles of beer on the wall {0} bottles of beer. \n Take one down, pass it around {1} bottles of beer on the wall...".format(wall, wall-1) )
    print(lyrics)
    print("Beer Left: ",beer)
    if beer == 0:
        print("\nNo more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, 99 bottles of beer on the wall... ")
