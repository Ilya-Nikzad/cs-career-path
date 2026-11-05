# Iteration (Looping)

Iteration means repeating a set of instructions multiple times.  
Instead of writing the same code again and again, we use loops to repeat actions automatically.

---

## For loop concept

A for loop repeats a block of code a fixed number of times.  
We use a variable (like i) that changes value each time.

for i from 2 to 10 do  
x ← x + i  
end for

---

## While loop concept

A while loop repeats code as long as a condition is true.  
Unlike a for loop, we don’t know exactly how many times it will run.

x ← 1  
y ← 0  

while x < 11 do  
y ← y + x  
x ← x + 1  
end while

---

## Using loops inside functions

A function is a reusable block of code that:  
- takes input  
- processes it  
- returns output  

Loops are often used inside functions to solve problems step by step.

function isInteger(n)  
y ← false  

for i from 1 to n do  
if i * i = n then  
y ← true  
end if  
end for  

return y  
end function  

Key idea  
Loop tries values  
Function checks condition  
Return gives final answer

---

## Controlling loops

Sometimes we don’t want a loop to run fully.  
We use:

- break → stop the loop completely  
- continue → skip current step and go next  

function isInteger(n)  
y ← false  

for i from 1 to n do  
if i * i = n then  
y ← true  
break  
end if  
end for  

return y  
end function  

What break does  
Immediately exits the loop  
No more iterations happen  

for i from 1 to 10 do  
if i = 5 then  
continue  
end if  

print(i)  
end for  

What continue does  
Skips current iteration  
Goes directly to next loop step  

---

## Key idea

| Command  | Effect |
|----------|--------|
| break    | stop loop completely |
| continue | skip current step |