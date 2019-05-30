# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:53:45 2019

@author: benja
"""

import numpy as np
#Defining some variables later being used as iterators
Dummy = 0
ZeroRuns=0
OneRuns=0
TwoRuns=0
ThreeRuns=0
FourRuns=0
FiveRuns=0
SixPlusRuns=0
#input pitcher's outcome rates
GroundballRate=.43
LineDriveRate=.14
FlyBallRate=.15
WalkRate=.09
StrikeoutRate=.19

#This section creates functions for each plate appearance outcome
#Each outcome takes inputs of the base state, runs already scored, and outs
#For a given base/run/out state, it moves the runners to the new appropriate
#bases and iterates runs and outs as necessary

def OneBaseSingle(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,1,0]
    elif VarState == [1,1,0]:
        VarState = [1,1,0]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [1,1,0]
        RunCount+=2
    elif VarState == [0,1,0]:
        VarState = [1,0,0]
        RunCount+=1
    elif VarState == [0,1,1]:
        VarState = [1,0,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [1,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def TwoBaseSingle(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,0,1]
    elif VarState == [1,1,0]:
        VarState == [1,0,1]
        RunCount +=1
    elif VarState == [1,1,1]:
        VarState = [1,0,1]
        RunCount +=2
    elif VarState == [0,1,0]:
        VarState = [1,0,0]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [1,0,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [1,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Double(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,1,0]
    elif VarState == [1,0,0]:
        VarState = [0,1,1]
    elif VarState == [1,1,0]:
        VarState = [0,1,1]
        RunCount +=1
    elif VarState == [1,1,1]:
        VarState = [0,1,1]
        RunCount +=2
    elif VarState == [0,1,0]:
        VarState = [0,1,0]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [0,1,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [0,1,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Triple(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,0,1]
    elif VarState == [1,0,0]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [1,1,0]:
        VarState = [0,0,1]
        RunCount +=2
    elif VarState == [1,1,1]:
        VarState = [0,0,1]
        RunCount +=3
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount+=2
    elif VarState == [0,0,1]:
        VarState = [0,0,1]
        RunCount +=1
    return VarState,RunCount,OutCount

def HomeRun(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,0,0]
        RunCount +=1
    elif VarState == [1,0,0]:
        VarState = [0,0,0]
        RunCount +=2
    elif VarState == [1,1,0]:
        VarState = [0,0,0]
        RunCount +=3
    elif VarState == [1,1,1]:
        VarState = [0,0,0]
        RunCount +=4
    elif VarState == [0,1,0]:
        VarState = [0,0,0]
        RunCount +=2
    elif VarState == [0,1,1]:
        VarState = [0,0,0]
        RunCount +=3
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=2
    return VarState,RunCount,OutCount

def Walk(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,1,0]
    elif VarState == [1,1,0]:
        VarState = [1,1,1]
    elif VarState == [1,1,1]:
        VarState = [1,1,1]
        RunCount+=1
    elif VarState == [0,1,0]:
        VarState = [1,1,0]
    elif VarState == [0,1,1]:
        VarState = [1,1,1]
    elif VarState == [0,0,1]:
        VarState = [1,0,1]
    return VarState,RunCount,OutCount

def Strikeout(VarState,RunCount,OutCount):
    OutCount+=1
    return VarState,RunCount,OutCount

def Groundout(VarState,RunCount,OutCount):
    OutCount+=1
    if OutCount == 3:
        return VarState,RunCount,OutCount
    elif VarState == [0,0,0]:
        VarState = [0,0,0]
    elif VarState == [1,0,0]:
        VarState = [0,1,0]
    elif VarState == [1,1,0]:
        VarState = [0,1,1]
    elif VarState == [1,1,1]:
        VarState = [0,1,1]
        RunCount +=1
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Flyout(VarState,RunCount,OutCount):
    OutCount+=1
    if OutCount == 3:
        return VarState,RunCount,OutCount
    elif VarState == [0,0,0]:
        VarState == [0,0,0]
    elif VarState == [1,0,0]:
        VarState == [1,0,0]
    elif VarState == [1,1,0]:
        VarState = [1,0,1]
    elif VarState == [1,1,1]:
        VarState = [1,0,1]
        RunCount +=1
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount+=1
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Lineout(VarState,RunCount,OutCount):
    OutCount+=1
    return VarState,RunCount,OutCount

#setting a few more iterating variables to 0
Action = 0
TotalRuns=0
TotalInnings=0

#This is the core loop.
#The first line sets the number of simulations to run.
#Inside the loop, numpy generates a random number between 0 and 1.
#Each outcome is assigned a range via the batted ball outcomes of each type
#of batted ball in 2018 multiplied by the pitcher's likelihood of producing
#that outcome.
#It then calls the appropriate plate appearance result function to move bases,
#runs, and outs as appropriate.
#When the inning is over (3 outs are reached),the loop records the number of
#runs scored (both in a running tally and by bucket) and starts over.

while TotalInnings<5000000:
    Outs=0
    Bases= [0,0,0]
    Runs=0
    while Outs <3:
        Action = np.random.random()
        if Action <GroundballRate*.1234522878:
            Dummy= OneBaseSingle(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate*.2469045755:
                if Outs == 2:
                    Dummy= TwoBaseSingle(Bases,Runs,Outs)
                    Bases = Dummy[0]
                    Runs = Dummy[1]
                    Outs = Dummy[2]
                else:
                    Dummy= OneBaseSingle(Bases,Runs,Outs)
                    Bases = Dummy[0]
                    Runs = Dummy[1]
                    Outs = Dummy[2]
        elif Action <GroundballRate*.266633459:
            Dummy=Double(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate*.2681989611:
            Dummy=Triple(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate:
            Dummy=Groundout(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate*.3990178996:
            Dummy=TwoBaseSingle(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate*.5821954697:
            Dummy=Double(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate*.5986377317:
            Dummy=Triple(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate*.6209409156:
            Dummy=HomeRun(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate:
            Dummy=Lineout(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate+FlyBallRate*.03466992157:
            Dummy=TwoBaseSingle(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate+FlyBallRate*.07263803044:
            Dummy=Double(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate+FlyBallRate*.07887082533:
            Dummy=Triple(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate+FlyBallRate*.2056302914:
            Dummy=HomeRun(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate+FlyBallRate:
            Dummy=Flyout(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        elif Action <GroundballRate+LineDriveRate+FlyBallRate+WalkRate:
            Dummy=Walk(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]
        else:
            Dummy=Strikeout(Bases,Runs,Outs)
            Bases = Dummy[0]
            Runs = Dummy[1]
            Outs = Dummy[2]

    #These tallies count likelihood of each run outcome occurring
    if Runs == 0:
        ZeroRuns+=1
    elif Runs ==1:
        OneRuns+=1
    elif Runs==2:
        TwoRuns+=1
    elif Runs==3:
        ThreeRuns+=1
    elif Runs==4:
        FourRuns+=1
    elif Runs==5:
        FiveRuns+=1
    else:
        SixPlusRuns+=1
    TotalRuns+=Runs
    TotalInnings+=1

#This line converts the total runs from the above simulation into RA/9
FinalRA9=0
FinalRA9=9*(TotalRuns/TotalInnings)

#Outputs
print ("RA9 is "+str(round(FinalRA9,8)))
print ("Zero Run Rate is "+str(round(ZeroRuns/TotalInnings,4)))
print ("One Run Rate is "+str(round(OneRuns/TotalInnings,4)))
print ("Two Run Rate is "+str(round(TwoRuns/TotalInnings,4)))
print ("Three Run Rate is "+str(round(ThreeRuns/TotalInnings,4)))
print ("Four Run Rate is "+str(round(FourRuns/TotalInnings,4)))
print ("Five Run Rate is "+str(round(FiveRuns/TotalInnings,4)))
print ("Six Plus Run Rate is "+str(round(SixPlusRuns/TotalInnings,4)))
