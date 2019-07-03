## EX01-HelloWorld

### Overview

The goal of this project is to familiarize your self with the programming assignment work flow. 
That is, the individual steps taken to start, complete and turn in for a grade a programming 
assignment for this class. All subsequent programming assignments will follow the same exact 
works flow. 

In addition, the secondary goal of this project is to write your first Python program. As has 
been a tradition for decades, the first program you write in most new languages is called Hello
World, which challenges the programmer to print those simple words to the display.

### Starting the project

Go to the LazyGrader website and login. On your home screen you should see all the assignments
for this class, and any other of my classes your are enrolled in. Next to the assignment called
**EX01-HelloWorld**, you should see a _Start_ button. Click that button to start the assignment.
This action will create the build on Jenkins and in GitHub. Once it's done you should see a 
_Build_ and _Grade_ button. Now you can clone the project locally in PyCharm. 

Click the link to your project in GitHub and press the _Clone_ button. Then click the clipboard
icon next to your repository URL, or select the URL and copy it to the clipboard. Once you've 
copied it, go to PyCharm and select **VCS -> Checkout from Version Control -> Git**. Paste the
URL into the URL field of the dialog box that appears. Next, click the _Clone_ button. After
PyCharm downloads your code, you are reading to start writing code.

### Creating `hello_world.py`

In PyCharm, right click on **EX01-HelloWorld** and then select **New -> Python File**. In the 
dialog that open, type the file name `hello_world`. PyCharm will add the .py extension, which
will be the extension for every program in this course.

### Writing the code

As we've learned in class, we can display a string in the conosle or 
terminal by using the `print` function. For this assignment, you're 
going to do the time honored program which prints `Hello, World!` to 
the console. In the file, hello_world.py, which you created above,
add the code that prints `Hello, World!` to the console. It should 
look something like:

```python
print('Hello, World!')
```

### Running your code

As with all programming assignments, there are two ways to run the program. The first way is for
testing and debugging your program. It runs your program directly and then you as the programmer
read the output and determine if the program is behaving as you would expect. For example, in 
the case of this assignment, you would ensure that the words `Hello, World!` appears in the
terminal output. To run your program directly choose 'hello_world' above, and to the right, and then
press the play button next to it.

The second way to run your programmer is through the grader. The grader is my way off automating
and ensuring consistent grading across all students. It runs a series of tests to make sure your
program does what it's supposed to do. Think of it as program that runs a program to see if it
works. To run the grader select 'grader' above and to the right, and then press the play button
next to it.

For both actions, your output will be at the bottom of the screen in the 'Run' tab. Try both and
observe the difference in the output.

For the `hello_world` target you should see output similar to the following:

```sh
6e08395c0915:python -u /opt/project/hello_world.py
Hello, World!

Process finished with exit code 0
```

For the `grader` target you should see output similar to the following:

```sh
924bd053b468:python -u /opt/project/grader.py
.
----------------------------------------------------------------------
Ran 1 test in 0.031s

OK
Command output :  b'Hello, World!\n'
Command exit status/return code :  0

Process finished with exit code 0
```

### Pushing your code to GitHub

Now you need to turn in your code by sending, or pushing, your code to GitHub. You created a 
GitHub repository when you started the assignment. Now you need to take your local code changes
and send them to GitHub so that you can turn it in and have it graded in the next step in the
work flow.

The first step is to commit your code locally. This tell git what files you want to turn in. In 
this case you only need to turn in the contents of `hello_world.py`. In the Project view, right-
click **EX01-HelloWord** and then select **Git -> Commit Directory...**. In the dialog box that
pops up, be sure only `hello_world.py` is selected and that there is some text in the _Commit 
Message_ box. A good commit message would be something like `Committing code to get a good grade`.

Once the commit is finished, which is a purely local action, you need to send that commit to 
GitHub. This is called the push phase of the process. Again right-click on **EX01-HelloWorld**.
Then select **Git -> Repository -> Push**. In the dialog box that pops up, push the **Push** button
and that should be it. You should see a message that says the push was successful. In the next
step you'll confirm that your code is working and then submit it for a grade.

### Turning in and Grading your code

Go back to LazyGrader and login again, if needed. Press the _Build_ button next to 
**EX01-HelloWorld** for this course. This will send a command to Jenkins to download your code
from GitHub and test it. If all goes well and all the tests pass, the ball next to the _Build_
will turn blue. If some of the tests don't pass the ball will be yellow. If the ball is grey,
that means you have not run the tests before and your project is not ready for grading.

Once the Jenkins status is blue or yellow, press the _Grade_ button for **EX01-HelloWorld**.
This will read the results from Jenkins and send your grade to Canvas. Once the notification in 
LazyGrader says the grade has been posted, you should see your grade on Canvas.

That's it, once you've submitted your grade, you are done. I will add points later, after I
inspect your code. For example, most projects will be out of a total of 25 points, but after 
pressing the _Grade_ button, Canvas will show 20 points. I will add up to 5 points after I have
looked at your code and am conviced it is original (Not so much for this assignment. There's
no such thing as a plagiarized Hello World program).