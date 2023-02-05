<h2> Option 2: Java Support Task </h2>

<p> In this task, we will simulate a typical interaction that you might have with
a student during a mentor support call.
The student asks you the following question:
"I am trying to do Task 6 and the JOptionPane.ShowDialog() does not work.
For some reason it does not store the input to the string variable it is
assigned to, so my do-while loop ends up in an infinite loop. Can you please
help me?"
Please describe the process that you would follow to help the student. </p>

---

<h2> Answer</h2>

Firstly I would check whether the imports are there and that they are correct. If the string is not storing
the input then there could either be a missing scanner, or the input is not being set to the string in a
proper way.

Another thing that I would check is whether the JOptionPane is placed inside the loop or on the outside of
loop. The reason it could not be working could be because the JOptionPane is outside the loop and is in turn
not being called. So I would make sure the JOptionPane is inside the loop and that the loop completes once
the input is received.