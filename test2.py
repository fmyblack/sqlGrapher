# coding: utf-8
#!/usr/bin/env python
import matplotlib.patches as mpatch
import matplotlib.pyplot as plt

# 部分代码是对绘制图形的一些定义，主要定义了文本框和剪头的格式
nonLeafNodes = dict(boxstyle = "sawtooth", fc = "0.8")
leafNodes = dict(boxstyle = "round4", fc = "0.8")
line = dict(arrowstyle = "<-")

# 使用递归计算树的叶子节点数目
def getLeafNum(tree):
    num = 0
    firstKey = tree.keys()[0]
    secondDict = tree[firstKey]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            num += getLeafNum(secondDict[key])
        else:
            num += 1
    return num

# 同叶子节点计算函数，使用递归计算决策树的深度
def getTreeDepth(tree):
    maxDepth = 0
    firstKey = tree.keys()[0]
    secondDict = tree[firstKey]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            depth = getTreeDepth(secondDict[key]) + 1
        else:
            depth = 1
        if depth > maxDepth:
            maxDepth = depth
    return maxDepth

# 在前面例子已实现的函数，用于注释形式绘制节点和箭头
def plotNode(nodeName, targetPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeName, xy = parentPt, xycoords = \
                            'axes fraction', xytext = targetPt, \
                            textcoords = 'axes fraction', va = \
                            "center", ha = "center", bbox = nodeType, \
                            arrowprops = line)

# 用于绘制剪头线上的标注，涉及坐标计算，其实就是两个点坐标的中心处添加标注
def insertText(targetPt, parentPt, info):
    xCoord = (parentPt[0] - targetPt[0]) / 2.0 + targetPt[0]
    yCoord = (parentPt[1] - targetPt[1]) / 2.0 + targetPt[1]
    createPlot.ax1.text(xCoord, yCoord, info)

# 实现整个树的绘制逻辑和坐标运算，使用的递归，重要的函数
# 其中两个全局变量plotTree.xOff和plotTree.yOff
# 用于追踪已绘制的节点位置，并放置下个节点的恰当位置
def plotTree(tree, parentPt, info):
    # 分别调用两个函数算出树的叶子节点数目和树的深度
    leafNum = getLeafNum(tree)
    treeDepth = getTreeDepth(tree)
    firstKey = tree.keys()[0] # the text label for this node
    firstPt = (plotTree.xOff + (1.0 + float(leafNum)) / 2.0/plotTree.totalW,\
                plotTree.yOff)
    insertText(firstPt, parentPt, info)
    plotNode(firstKey, firstPt, parentPt, nonLeafNodes)
    secondDict = tree[firstKey]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], firstPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), \
                    firstPt, leafNodes)
            insertText((plotTree.xOff, plotTree.yOff), firstPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD

# 以下函数执行真正的绘图操作，plotTree()函数只是树的一些逻辑和坐标运算
def createPlot(inTree):
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon = False) #, **axprops)
    # 全局变量plotTree.totalW和plotTree.totalD
    # 用于存储树的宽度和树的深度
    plotTree.totalW = float(getLeafNum(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), ' ')
    plt.show()

# 一个小的测试集
def retrieveTree(i):
    listOfTrees = [{'no surfacing':{0: 'no', 1:{'flippers':{0:'no', 1:'yes'}}}},\
                    {'no surfacing':{0: 'no', 1:{'flippers':{0:{'head':{0:'no', \
                    1:'yes'}}, 1:'no'}}}}]
    return listOfTrees[i]

# createPlot(retrieveTree(1)) # 调用测试集中一棵树进行绘制