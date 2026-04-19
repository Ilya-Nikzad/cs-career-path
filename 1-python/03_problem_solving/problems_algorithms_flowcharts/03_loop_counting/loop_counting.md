# 📊 Flowchart: Character Counting Algorithm

```mermaid
flowchart TD

Start([Start])
GetWord[Input a word]
InitCount[Set counter = 0]
FirstLetter[Start from first letter]
CheckMore{Are there more letters?}
Count[Increase counter by 1]
NextLetter[Move to next letter]
Display[Show counter value]
End([End])

Start --> GetWord
GetWord --> InitCount
InitCount --> FirstLetter
FirstLetter --> CheckMore

CheckMore -->|Yes| Count
Count --> NextLetter
NextLetter --> CheckMore

CheckMore -->|No| Display
Display --> End