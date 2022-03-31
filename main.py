#!/usr/bin/python3

import sys
import getopt
import os
from movie import MovieTheater

def main(argv):

    inputfile = ""
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv, "hti:", ["ifile="])
    except getopt.GetoptError:
        print('./'+os.path.basename(__file__)+' -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('./'+os.path.basename(__file__)+' -i <inputfile>')
            sys.exit()
        elif opt in ("-t"):
            reservatonList = MovieTheater()
            while True:
                n = input("Enter reservation size or q to quit: ")
                if n == 'q':
                    sys.exit()
                if n.isnumeric():
                    print(reservatonList.greedy_add_reservation(int(n)))
                else:
                    print("try again D:")

        elif opt in ("-i", "--ifile"):
            inputfile = arg
            # Create a file with the same path but with the .out extension
            outputfile = os.path.splitext(arg)[0] + ".out"
            print("output file:", outputfile)


    try:
        with open(inputfile, "r") as f:
            with open(outputfile, "w") as out:

                # read all the lines from the fine and save in a list
                lines = f.readlines() 
                reservatonList = MovieTheater(lines) 

                # call to the seat assignment method
                reservatonList.theater_seat_assignment()
                print(reservatonList)
                out.write(reservatonList.output())
    except OSError:
        print("Could not open/read file:", inputfile)
        sys.exit()
        

        


if __name__ == "__main__":
    main(sys.argv[1:])