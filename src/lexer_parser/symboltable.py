
symbolTable = {}
scopeStack = []
funcTable = {}

# Get the table of current function node
def getTable(node):
    global symbolTable
    global scopeStack
    global funcTable
    funcTable = symbolTable
    for item in scopeStack:
        funcTable = funcTable[item]
    auxNode = "_" + node
    scopeStack.append(auxNode)
    funcTable[auxNode] = {}
    funcTable = funcTable[auxNode]

# Delete the table of current function node
def deleteTable(node):
    global symbolTable
    global scopeStack
    global funcTable
    scopeStack.pop()
    funcTable = symbolTable
    for item in scopeStack:
        funcTable = funcTable[item]
    del funcTable["_" + node]

# Clean all the tables and variables
def clean():
    global symbolTable
    global scopeStack
    global funcTable
    symbolTable = {}
    scopeStack = []
    funcTable = {}
