# Ashmeet Kaur
# CompB10 Fall2025
# Lincoln vs Swift
# program uses average word length, total character, and num of words with len>7
# to determine text with higher level intelligence

strLinc = """Fellow countrymen: at this second appearing to take the oath of the presidential office there is less occasion for an extended address than there was at the first. Then a statement somewhat in detail of a course to be pursued seemed fitting and proper. Now, at the expiration of four years during which public declarations have been constantly called forth on every point and phase of the great contest which still absorbs the attention and engrosses the energies of the nation little that is new could be presented. The progress of our arms, upon which all else chiefly depends is as well known to the public as to myself and it is I trust reasonably satisfactory and encouraging to all. With high hope for the future no prediction in regard to it is ventured.
On the occasion corresponding to this four years ago all thoughts were anxiously directed to an impending civil war. All dreaded it ~ all sought to avert it. While the inaugural address was being delivered from this place devoted altogether to saving the Union without war insurgent agents were in the city seeking to destroy it without war ~ seeking to dissolve the Union and divide effects by negotiation. Both parties deprecated war but one of them would make war rather than let the nation survive, and the other would accept war rather than let it perish. And the war came.
One eighth of the whole population were colored slaves not distributed generally over the union but localized in the southern part of it. These slaves constituted a peculiar and powerful interest. All knew that this interest was somehow the cause of the war. To strengthen perpetuate and extend this interest was the object for which the insurgents would rend the Union even by war while the government claimed no right to do more than to restrict the territorial enlargement of it. Neither party expected for the war the magnitude or the duration which it has already attained. Neither anticipated that the cause of the conflict might cease with or even before the conflict itself should cease. Each looked for an easier triumph and a result less fundamental and astounding. Both read the same Bible and pray to the same God and each invokes His aid against the other. It may seem strange that any men should dare to ask a just God's assistance in wringing their bread from the sweat of other men's faces but let us judge not that we be not judged. The prayers of both could not be answered ~ that of neither has been answered fully. The Almighty has His own purposes. "Woe unto the world because of offenses for it must needs be that offenses come but woe to that man by whom the offense cometh." If we shall suppose that American slavery is one of those offenses which in the providence of God must needs come but which having continued through His appointed time He now wills to remove and that He gives to both North and South this terrible war as the woe due to those by whom the offense came shall we discern therein any departure from those divine attributes which the believers in a living God always ascribe to Him. Fondly do we hope ~ fervently do we pray ~ that this mighty scourge of war may speedily pass away. Yet, if God wills that it continue until all the wealth piled by the bondsman's two hundred and fifty years of unrequited toil shall be sunk and until every drop of blood drawn with the lash shall be paid by another drawn with the sword as was said three thousand years ago so still it must be said 'the judgments of the Lord are true and righteous altogether.'
With malice toward none with charity for all with firmness in the right as God gives us to see the right let us strive on to finish the work we are in to bind up the nation's wounds, to care for him who shall have borne the battle and for his widow and his orphan ~ to do all which may achieve and cherish a just and lasting peace among ourselves and with all nations."""

strSwift = """I have this thing where I get older but just never wiser
Midnights become my afternoons
When my depression works the graveyard shift
All of the people I've ghosted stand there in the room
I should not be left to my own devices
They come with prices and vices
I end up in crisis (tale as old as time)
I wake up screaming from dreaming
One day I'll watch as you're leaving
'Cause you got tired of my scheming
(For the last time)
It's me, hi, I'm the problem, it's me
At tea time, everybody agrees
I'll stare directly at the sun but never in the mirror
It must be exhausting always rooting for the anti-hero
Sometimes I feel like everybody is a sexy baby
And I'm a monster on the hill
Too big to hang out, slowly lurching toward your favorite city
Pierced through the heart, but never killed
Did you hear my covert narcissism I disguise as altruism
Like some kind of congressman? (Tale as old as time)
I wake up screaming from dreaming
One day I'll watch as you're leaving
And life will lose all its meaning
(For the last time)
It's me, hi, I'm the problem, it's me (I'm the problem, it's me)
At tea time, everybody agrees
I'll stare directly at the sun but never in the mirror
It must be exhausting always rooting for the anti-hero
I have this dream my daughter in-law kills me for the money
She thinks I left them in the will
The family gathers 'round and reads it and then someone screams out
"She's laughing up at us from hell"
It's me, hi, I'm the problem, it's me
It's me, hi, I'm the problem, it's me
It's me, hi, everybody agrees, everybody agrees
It's me, hi (hi), I'm the problem, it's me (I'm the problem, it's me)
At tea (tea) time (time), everybody agrees (everybody agrees)
I'll stare directly at the sun but never in the mirror
It must be exhausting always rooting for the anti-hero"""

# the function cleans the text, replaces any delimiter with space
def cleanText(strText):
    strText = strText.replace("\n", " ")
    strText = strText.replace("~", "")
    strText = strText.replace("(", " ")
    strText = strText.replace(")", " ")
    strText = strText.replace("   ", " ")
    strText = strText.replace("  ", " ")
    return strText


# the functions return a tuple with sorted list of unique words in text
def uniqueWords(strText):
    liWords = strText.split()
    arNew = []
    for strWord in liWords:
        if (strWord not in arNew):
            arNew.append(strWord)
    return (len(arNew),sorted(arNew, key=len, reverse=True))


# the function returns length and prints list of words with length > 7
def longWords(strText):
    liWords = []
    resultTuple = uniqueWords(strText)
    intLen = resultTuple[0]
    liWords = resultTuple[1]

    # in list of unique words ; remove (using list.pop( ))any words that
    # have a length of less than 7. (len(strWord) < 7).
    for index in range(len(liWords) - 1, -1, -1):  # from last → first
        if len(liWords[index]) < 7:
            liWords.pop(index)

    print(f"{len(liWords)} words with length > 7:")
    print(liWords)
    return(len(liWords))


# main code begins

# starts Linc's section
print("For Lincoln's Text:")
#  This is where we call the function to clean out the text.
strLinc = cleanText(strLinc)
# Here we have a few different operations done on the Lincoln text.
intLincTotChars = len(strLinc)
liLincWords = strLinc.split(" ")
intLincNumWords = len(liLincWords)
flLincAvgWordLength = intLincTotChars / intLincNumWords
intLincNumUnique = uniqueWords(strLinc)[0]
liLincUniqueWords = uniqueWords(strLinc)[1]
# Here is some output to get you started,using the Lincoln Text.
print(f"The Lincoln text has {intLincTotChars} characters.")
print(f"The Lincoln text has an average word length of {flLincAvgWordLength:.4f} characters.")
intLincLongWordLen = longWords(strLinc)  # stores length of list with words > 7


# starts Swift's section
print("")
print("-"*500)
print("For Swift's Text:")
#  This is where we call the function to clean out the text.
strSwift = cleanText(strSwift)
# Here we have a few different operations done on the Swift text.
intSwiftTotChars = len(strSwift)
liSwiftWords = strSwift.split(" ")
intSwiftNumWords = len(liSwiftWords)
flSwiftAvgWordLength = intSwiftTotChars / intSwiftNumWords
intSwiftNumUnique = uniqueWords(strSwift)[0]
liSwiftUniqueWords = uniqueWords(strSwift)[1]
# Here is some output to get you started,using the Swift Text.
print(f"The Swift text has {intSwiftTotChars} characters.")
print(f"The Swift text has an average word length of {flSwiftAvgWordLength:.4f} characters.")
intSwiftLongWordLen = longWords(strSwift)   # stores length of list with words > 7


# comparison of values to determine intelligence level
# whoever gets a value higher, gets their score increased by 1
# their scores are stored in lincScore and swiftScore
print("")
print("*" * 60)
print("")
lincScore = 0
swiftScore = 0
print("Results:")
if(intLincTotChars > intSwiftTotChars):
    lincScore += 1
    print("1. LincText has more characters than SwiftText.")
else:
    swiftScore += 1
    print("1. SwiftText has more characters than LincText.")

if(flLincAvgWordLength > flSwiftAvgWordLength):
    lincScore += 1
    print("2. LincText has more average word length than SwiftText.")
else:
    swiftScore += 1
    print("2. SwiftText has more average word length than LincText.")

if(intLincLongWordLen > intSwiftLongWordLen):
    lincScore += 1
    print("3. LincText has more more words greater than length 7 than SwiftText.")
else:
    swiftScore += 1
    print("3. SwiftText has more more words greater than length 7 than LincText.")


# the following compares who 'Linc or Swift' has score greater than the other
# and prints the final result
print("")
print("*" * 60)
print("")
if(lincScore > swiftScore):
    print("Lincoln's Text demonstrates higher level of Intelligence!")
else:
    print("Swift's Text demonstrates higher level of Intelligence!")
print("")
print("*" * 60)