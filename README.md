## Python: Understanding Return Statements

### Background Information

- Watch this brief video about [return statements](https://youtu.be/ZnBQfF5JFDM?feature=shared) in Python

### Coding

Objective: To learn how to define and use a `return` statement with a Python function.

- Complete the practice projects outlined below
- Start with the first project, which is easier, and end with the last project, which is more challenging
- Use comments to label each project in your script

#### Project 1: Destination Europe

- Write a function `describe_vacation()` that takes three parameters:
  - destination
  - activity
  - season
- Assign the `season` parameter a default value of *summer*
- **First function call**: Return to a variable named `description1` an f-string that includes:
  - your destination
  - the season
  - your activity (what you will do while on vacation)
  - Example: I am going to **Rome** for a **summer** vacation.  I will **explore ancient ruins** there.
  - Use only two arguments when you call your function -- one for your destination, the other for your activity
- **Second function call**: Return to a variable named `description2` an f-string that includes the same placeholders you used in your first function call
  - Use THREE arguments when you call your function -- one for your destination, another for your activity, a third for the season (spring or fall, for example)
  - Example: I am going to **Paris** for a **fall** vacation.  I will **enjoy sampling French pastries** there.
 
#### Project 2: Student Major

At the university, students eventually must choose a **major**, i.e., the subject or field they want to earn a degree in.  Some students, for example, choose to major in English, while those interested in science may decide to major in Biology or Chemistry.

- Write a function `show_major()` that takes three parameters:
  - `first_name`
  - `university`
  - `major`
- Assign a default value of **Sports Medicine** to the parameter `major`
- Return an f-string that includes the student's first name, university, and his/her major
- Example 1: **Carli** attends the **University of Georgia** and is majoring in **Computer Science**.
- Example 2: **Mark** attends the **University of Hawaii** and is majoring in **Marine Biology**.
