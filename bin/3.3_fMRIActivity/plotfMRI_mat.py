"""
Created on 10/08/2017

@author: Niklas Pallast
Neuroimaging & Neuroengineering
Department of Neurology
University Hospital Cologne



"""

import matplotlib.pyplot as plt
import os, sys
import numpy as np
import scipy.io as sio

np.seterr(divide='ignore', invalid='ignore')
import seaborn as sns


def matrixMaker(matData):
    unCorrmatrix = matData['matrix']
    labels = matData['label']

    # Adapt labels to pyplot
    labels = [s.replace('\t', '-') for s in labels]
    labels = [s.replace('\n', ' ') for s in labels]
    labels = [s.replace(' ', '') for s in labels]
    labels = [s.replace('_', '') for s in labels]

    # Calculcate correlation of time series
    corrMatrix = np.corrcoef(unCorrmatrix, rowvar=False)
    corrMatrix = corrMatrix - np.eye(np.size(corrMatrix, 1))
    corrMatrix = np.nan_to_num(corrMatrix)

    fig, ax = plt.subplots()

    sns.heatmap(corrMatrix)
    ax.axis('tight')

    # Set labels
    ax.set(xticks=np.arange(len(labels)), xticklabels=labels,
           yticks=np.arange(len(labels)), yticklabels=labels)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    ax.set_title("rsfMRI Correlation between ARA regions")
    plt.show()

    return corrMatrix


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Visulize mat file of fMRI ')
    parser.add_argument('-i', '--inputMat', help='file name:fMRI mat-File')

    args = parser.parse_args()

    inputPath = None
    if args.inputMat is not None and args.inputMat is not None:
        inputPath = args.inputMat
    if not os.path.exists(inputPath):
        sys.exit("Error: %s path is not an existing directory." % (args.inputPath,))

    inputPath = args.inputMat
    matData = sio.loadmat(inputPath)

    # generate Matrix
    matrixMaker(matData)
