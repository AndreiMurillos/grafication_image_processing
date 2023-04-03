import numpy as np
import cv2


def calcMassCenter(image, height, width, onePixels):
    # Cálculo del centro Y
    pixelsAbove = 0
    pixelsBelow = onePixels
    for i in range(1, height):
        oldSolution = [pixelsBelow, pixelsAbove]
        pixelsAbove = pixelsAbove + sum(image[i])
        pixelsBelow = pixelsBelow - sum(image[i])
        newSolution = [pixelsBelow, pixelsAbove]
        if pixelsAbove > pixelsBelow:
            break
    if (abs(oldSolution[0] - oldSolution[1])) < (abs(newSolution[0] - newSolution[1])):
        y_sol = oldSolution
        i = i - 1
    else:
        y_sol = newSolution
    y = i

    # Cálculo del centro X
    pixelsLeft = 0
    pixelsRight = onePixels
    for i in range(1, width):
        oldSolution = [pixelsLeft, pixelsRight]
        sumPixels = 0
        for j in range(height):
            sumPixels = sumPixels + image[j][i]
        pixelsLeft = pixelsLeft + sumPixels
        pixelsRight = pixelsRight - sumPixels
        newSolution = [pixelsLeft, pixelsRight]
        if pixelsLeft > pixelsRight:
            break
    if (abs(oldSolution[0] - oldSolution[1])) < (abs(newSolution[0] - newSolution[1])):
        x_sol = oldSolution
        i = i - 1
    else:
        x_sol = newSolution
    x = i

    return x, y, x_sol, y_sol


def calcPixels(image, height, width):
    onePixels = 0
    zeroPixels = 0
    for i in range(height):
        for j in range(width):
            if image[i][j] == 1:
                onePixels = onePixels + 1
            if image[i][j] == 0:
                zeroPixels = zeroPixels + 1
    return onePixels, zeroPixels


def transform_data(image, height, width):
    newImage = []
    for i in range(height):
        newImage.append([])
        for j in range(width):
            if list(image[i, j]) == [0, 0, 0]:
                newImage[i].append(1)
            if list(image[i, j]) == [255, 255, 255]:
                newImage[i].append(0)
    return newImage


def getDimensions(image):
    return len(image), len(image[0])


def calcCentralMoment(image, height, width, x, y, p, q):
    m = 0
    for i in range(height):
        for j in range(width):
            m = m + (image[i][j] * ((x**p) * (y**q)))  # Momento estándar
            m = m + (
                image[i][j] * ((abs(j + 1 - x) ** p) * (abs(i + 1 - y) ** q))
            )  # Momento central
    return m
