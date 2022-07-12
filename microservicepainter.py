import cv2 as cv
from random import randrange
from tkinter import *
import os
import subprocess
import time
import json
import copy
painting_file = "./microservices/painting.png"

class MicroservicePainter:
    def __init__(self):
        self._painting_history = []

    def mainLoop(self):
        print("Hello.")

        # read keybindings for painter microservices
        with open('./microservices/keybindings1.txt') as file:
            data = file.read()
        keys_to_microservices = json.loads(data)
        print("keys to microservices:", keys_to_microservices)
        print("additional keys: z to undo, s to save, x to exit.")

        # initialize image
        self.invokePainter("initialize.py")

        # handle input
        while True:
            key = input("paint: ")
            # hard-coded inputs
            if key == 'x':
                print("Good-Bye.")
                return
            elif key == 's':
                print("saving...")
                cv.imwrite("./output/" + str(time.time()) + ".png", self._painting_history[-1])
            elif key == 'z':
                self.undoPainting()
            elif key in keys_to_microservices:
                print('painting...')
                self.invokePainter(keys_to_microservices[key])
            else:
                print("not mapped")

    def invokePainter(self, painter_python):
        # invoke
        wd = os.getcwd()
        os.chdir("./microservices/")
        subprocess.call("python " + painter_python, shell=True)
        os.chdir(wd)
        # handle updates
        time.sleep(1)
        self.handlePaintingUpdates()

    def handlePaintingUpdates(self, store_history=True):
        if os.path.exists(painting_file):
            # read, stash, and render
            image = cv.imread(painting_file, cv.IMREAD_COLOR)
            if store_history:
                self._painting_history.append(image.copy())
            cv.imshow('painting', image)
            cv.waitKey(1)

    def undoPainting(self):
        print("history", len(self._painting_history))
        if len(self._painting_history) <= 1:
            return
        # undo
        self._painting_history.pop()
        cv.imwrite(painting_file, self._painting_history[-1])
        # handle updates
        self.handlePaintingUpdates(False)

if __name__ == "__main__":
    program = MicroservicePainter()
    program.mainLoop()
