import matplotlib.patches as mpatch
import matplotlib.pyplot as plt
from pylab import *

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="- >")

oneDepth = 0.2

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    draw.ax1.annotate(nodeTxt, xy=parentPt, \
    xycoords = 'axes fraction', \
    xytext=centerPt, textcoords='axes fraction', \
    va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def plotTree(subTree, parentPos, depth, leftPoint, rightPoint):
    if parentPos == None:
        leaf = subTree.keys()[0]
        print leaf
        selfPt = (rightPoint / 2.0, depth * oneDepth)
        plotNode(leaf, selfPt, selfPt, leafNode)
        plotSubTree(subTree[leaf], selfPt, depth, leftPoint, rightPoint)
    else:
        num = len(subTree)
        x_seq = (rightPoint - leftPoint) * 1.0 / num / 2
        i = 0
        for leaf in subTree.keys():
            i += 1
            pos = (leftPoint + x_seq * (i * 2 - 1), depth * 0.2)
            plotNode(leaf, pos, parentPos ,leafNode)
            son = subTree[leaf]
            plotSubTree(son, pos, depth, pos[0] - x_seq, pos[0] + x_seq)

def plotSubTree(subTree, pos, depth, leftPoint, rightPoint):
    if type(subTree).__name__ == 'dict':
        plotTree(subTree, pos, depth + 1, leftPoint, rightPoint)
    else:
        plotNode(subTree, (pos[0], pos[1] + oneDepth), pos, leafNode)

def draw(tree):
    fig = plt.figure(30, facecolor='white')
    fig.clf()
    draw.ax1 = plt.subplot(111, frameon=False)
    # xlim(0, 12)
    # ylim(0, 6)
    plotTree(tree, None, 0, 0, 1)
    plt.show()

# tree = {'a11111111111111':{'b2':'c3', 'd2':{'e3':'f4', 'g3':'h4'}}}
# tree = {'d': 'c'}
# draw(tree)
# def listGragh():
#     styles = mpatch.BoxStyle.get_styles()
#     spacing = 1.2
#
#     figheight = (spacing * len(styles) + .5)
#     fig1 = plt.figure(1, (4 / 1.5, figheight / 1.5))
#     fontsize = 0.3 * 72
#
#     for i, stylename in enumerate(sorted(styles.keys())):
#         fig1.text(0.5, (spacing * (float(len(styles)) - i) - 0.5) / figheight, stylename,
#                   ha="center",
#                   size=fontsize,
#                   transform=fig1.transFigure,
#                   bbox=dict(boxstyle=stylename, fc="w", ec="k"))
#     plt.draw()
#     plt.show()
#
# listGragh()