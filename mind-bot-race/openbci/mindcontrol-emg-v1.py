import argparse
import time
from pprint import pprint
from micromelon import *

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

distance = 2
threshold = 400

def main():

    board_id = BoardIds.CYTON_BOARD
    
    BoardShim.enable_dev_board_logger()

    params = BrainFlowInputParams()
    params.serial_port = "/dev/ttyUSB3"

    pprint(BoardShim.get_board_descr(board_id))

    board = BoardShim(BoardIds.CYTON_BOARD, params)
    board.prepare_session()
    board.start_stream()

    first_run = True

    rc = RoverController()

    rc.connectBLE(98)
    rc.startRover()

    initial_max = 0

    iter = 0

    while True:
        iter = iter + 1
        time.sleep(0.1)
        # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
        data = board.get_board_data()  # get all data and remove it from internal buffer

        if first_run:
            first_run = False
            print("Number of Channels:", len(data))
            initial_max = max(data[1])

        if iter == 15:
            initial_max = max(data[1])

        current = max(data[1])
        print("------------------")
        # print("Channel 0:", data[0])
        print("iter:", iter)
        print("Channel 1:", current)
        print("initial:", initial_max)
        print("threshold:", threshold)

        # print("Channel 2:", data[2])
        # print("Channel 3:", data[3])
        # print("Channel 4:", data[4])
        # print("Channel 5:", data[5])
        # print("Channel 6:", data[6])
        # print("Channel 7:", data[7])
        # print("Channel 8:", data[8])
        # print("Channel 9:", data[9])
        # print("Channel 10:", data[10])
        # print("Channel 11:", data[11])
        # print("Channel 12:", data[12])
        # print("Channel 13:", data[13])
        # print("Channel 14:", data[14])
        # print("Channel 15:", data[15])
        # print("Channel 16:", data[16])
        # print("Channel 17:", data[17])
        # print("Channel 18:", data[18])
        # print("Channel 19:", data[19])
        # print("Channel 20:", data[20])
        # print("Channel 21:", data[21])
        # print("Channel 22:", data[22])
        # print("Channel 23:", data[23])

        if current > initial_max + threshold:
            Motors.moveDistance(int(distance))



    board.stop_stream()
    board.release_session()



if __name__ == "__main__":
    main()