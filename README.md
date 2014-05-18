

<div class="section" id="cosc1092-1093-python-assignment">
<div class="section" id="overview">


## Overview
<p>You have been commissioned by Pacific Megaversity, a new
Australian university, to write a system for managing
enrolments for tutorial classes. The system is to be written
in Python and will ultimately include programs for use by
students, tutors and administrative staff. You will be
writing the core of it; a Python module which stores,
queries and modifies tutorial enrolment data, as well as a
few small programs which access it.</p>
<p>You may use any sample data in this assignment specification
as test data for your program.</p>
</div>
<div class="section" id="how-data-is-stored">
    
## How data is stored
<p>Since this system is to be used by the university’s
Basket-Weaving Department, which traditionally has modest
enrolments, it is not expected to need to deal with huge
numbers of students; as such, it stores its data in simple
files in a directory.</p>
<p>Assume any codes (subject, class, venue) are case-sensitive.</p>
<p>All data for the system is stored in text files in one
data directory. The files contain one or more columns
of data (columns separated by colons ”:”) with optional
comment lines preceded by hash marks `"#"`.</p>
<p>The directory contains:</p>
</div>
<div class="section" id="a-list-of-subjects-in-the-system">
    
## A list of subjects in the system
<p>This is stored in a file named SUBJECTS. Each
line in the file contains information about one subject.
This information consists of the subject code and the
subject’s full name, separated by colons (‘:’). An example
SUBJECTS file might look like:</p>
<div class="highlight-python"><pre>bw101:Introductory Basketweaving 1
bw110:Introductory Basketweaving 2
bw330:Underwater Basketweaving</pre>
</div>
</div>
<div class="section" id="a-list-of-classes-in-the-system">
    
## A list of classes in the syste
<p>This is stored in a file named CLASSES. Each
line in this file describes one class, and consists of
fields separated by colons. The fields are the code for that
class, the subject code the class is for, the class time,
the venue the class is in, and the name of the tutor taking
the class. An example CLASSES file may look
like:</p>
<div class="highlight-python"><pre>bw101.1:bw101:Mon 9.30:2.5.10:Alice Chiswick
bw101.2:bw101:Wed 14.30:2.6.1:Bob Turnham
bw330A:bw330:Tue 15.30:23.5.32:Carlos Stamford</pre>
</div>
</div>
<div class="section" id="a-list-of-class-venues">
    
## A list of class venues
<p>This is stored in a file named VENUES, and
lists the places where classes can be held. Each line gives
the venue name and the maximum number of students that can
be enrolled in that venue. An example VENUES file
may look like:</p>
<div class="highlight-python"><pre>2.5.10:18
2.5.11:18
2.6.1:22
23.5.32:50</pre>
</div>
</div>
<div class="section" id="a-list-of-students-enrolled-in-each-class">
    
## A list of students enrolled in each class
<p>There is one such file for each class; it is named
classname.roll, where classname is
the name of the class. Each line of the file is the ID
number of one student. For example, the first Introductory
Basketweaving 1 class in the example above would be kept in
a file named bw101.1.roll; if it contained 4
students, its contents might look like:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="mi">1124395</span>
<span class="mi">1125622</span>
<span class="mi">1109202</span>
<span class="mi">1136607</span>
</pre></div>
</div>
<p>In any of the above files, any line starting with a ‘#’
(hash character) is considered a comment and ignored.</p>
</div>
<div class="section" id="your-task">
    
## Your task
<p>In this subject, you will be writing a Python module
named enrol. This will contain various utility
functions used to make your job easier, as well as an object
class which encapsulates the database and through which all
interactions with it are performed. You will also write a
small program which uses your module. Another client program
which uses your module will be made available online for you
to test your module against.</p>
<p>The function and class names and specifications in your
module must be identical to those in this sheet. Part of the
marking process will be conducted by an automated Python
program which attempts to use your module. This program will
expect the module to conform to this specification; if
parts of your module don’t conform, they will be considered
not to work.</p>
</div>
<div class="section" id="part-1-utility-functions">
    
## Part 1: Utility functions
<p>In your enrol module, write the following
functions:</p>
<p>readlines(filename)</p>
<blockquote>
<div>Returns a list of all the lines in a file, except for those
starting with a #. filename is a string
containing the name of a file. The lines returned must not
end in new-line characters.</div></blockquote>
<p>readtable(filename)</p>
<blockquote>
<div><p>Reads a file of colon-delimited lines and returns a list of
lists, with each line being represented as a list of
strings, split on colons. For example, if the file
example contains:</p>
<div class="highlight-python"><pre>foo:1:12
bar:2:hello</pre>
</div>
<p>then calling readtable(‘example’) will return the Python list
[[‘foo’,‘1’,‘12’],[‘bar’,‘2’,’hello’]].</p>
</div></blockquote>
<p>writelines(filename,lines)</p>
<blockquote>
<div>This function writes a list of strings safely to the file
filename, replacing any content already there. By “safely”,
it should write the lines to a file with a different name
in the directory, and if successful, deletes the file named
in filename, renames the new file to its name and returns
the value 1. If an error occurs during writing (and an
exception is raised), it deletes the new file and returns 0.</div></blockquote>
</div>
<div class="section" id="part-2-the-enrol-class">
    
## Part 2: The Enrol class
<p>In this part of the assignment, you will be writing a
Python class named Enrol in the enrol module, which encapsulates
the tutorial enrolment database described above. When the
enrol object is created, it will read its data from
the directory whose name is given to it. When the program
using Enrol calls its methods to retrieve data, it
will retrieve the information from its in-memory data
structures. When the user calls methods to change data
(i.e., to add students to classes), it will change both its
data structures and the files on the disk.</p>
<p>The Enrol class has the following methods:</p>
<p>__init__</p>
<blockquote>
<div>The constructor. Accepts one argument: the name of the
directory where the enrolment data is kept. When the object
is constructed, it should read its data from the
directory.</div></blockquote>
<p>subjects</p>
<blockquote>
<div>Returns a list of subject codes handled by the enrolment system.
Accepts no arguments.</div></blockquote>
<p>subjectName</p>
<blockquote>
<div>Accepts one argument: a subject code. Returns the name of
the subject with that code, or None if no subject
matches.</div></blockquote>
<p>classes</p>
<blockquote>
<div>Returns a list of class IDs for a particular subject.
Accepts one argument: the subject code of a subject.
Raise KeyError if the subject does not exist.</div></blockquote>
<p>classInfo</p>
<blockquote>
<div>Returns information about a class. Accepts one argument: a
string containing the class ID. Returns a tuple of the form
(subjcode, time, room, tutor, students). The first
four elements are strings, and contain the information as
described in the CLASSES file specification above.
The last item is a list of the student IDs enrolled in the
class.
Raise KeyError if the class does not exist.</div></blockquote>
<p>checkStudent</p>
<blockquote>
<div>Checks which classes a student is enrolled in. Accepts one
or two arguments. The first (required) argument is the
student ID to check. The second (optional) argument is an
optional subject code. If a subject code is specified,
returns the class code of the class in which the student is
enrolled for that subject; if the student isn’t enrolled in
any class in that subject, it returns None. If no
subject code is specified, it returns a list of zero or more
class codes the student is enrolled in across all possible
subjects.</div></blockquote>
<p>enrol</p>
<blockquote>
<div>Attempts to enrol a student in a class. Accepts two
arguments: a student ID and a class code. It returns 1 if
successful, None if not. Before attempting to enrol
a student in a class, it attempts to check whether the
number of students in the class is less than the capacity of
the class’s venue. If not, then there is no space in the
class and it fails. If there is space, it proceeds. If the
student is enrolled in any other classes in the same subject
as the class, she is removed from those classes and placed
in the new one.
Raise KeyError if the class does not exist.</div></blockquote>
<p>You may also want to write internal methods used by the
above methods, for example when more than one method needs
to perform a certain task. Your internal method names should
start with one underscore (_) character, to
distinguish them from “public” methods.</p>
<p>A possible example of your class in use, showing
arguments accepted and results returned, is below:</p>
<div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">enrol</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span> <span class="o">=</span> <span class="n">enrol</span><span class="o">.</span><span class="n">Enrol</span><span class="p">(</span><span class="s">"/path/to/data"</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span><span class="o">.</span><span class="n">subjects</span><span class="p">()</span>
<span class="go">['bw101', 'bw110', 'bw232', 'bw290', 'bw660']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span><span class="o">.</span><span class="n">subjectName</span><span class="p">(</span><span class="s">'bw110'</span><span class="p">)</span>
<span class="go">"Introductory Basketweaving 1"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span><span class="o">.</span><span class="n">classes</span><span class="p">(</span><span class="s">'bw232'</span><span class="p">)</span>
<span class="go">['bw232.1', 'bw232.2']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span><span class="o">.</span><span class="n">classInfo</span><span class="p">(</span><span class="s">'bw232.1'</span><span class="p">)</span>
<span class="go">('bw232', 'Mon 10.30', '66.3.1', 'Jim Derrida', ['1122345','1954231'])</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span><span class="o">.</span><span class="n">checkStudent</span><span class="p">(</span><span class="s">'1122345'</span><span class="p">,</span><span class="s">'bw232'</span><span class="p">)</span>
<span class="go">"bw232.1"</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span><span class="o">.</span><span class="n">checkStudent</span><span class="p">(</span><span class="s">'1122345'</span><span class="p">)</span>
<span class="go">['bw232.1', 'bw660.group1', 'bw290_A']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">e</span><span class="o">.</span><span class="n">enrol</span><span class="p">(</span><span class="s">'1122345'</span><span class="p">,</span><span class="s">'bw232.2'</span><span class="p">)</span>
<span class="go">1</span>
</pre></div>
</div>
</div>
<div class="section" id="part-3-a-statistics-client">
    
## Part 3: A statistics client
<p>In this part, you will be writing a Python command-line
script named stats, which uses your module to
display statistics about current enrolments.</p>
<p>If run with no arguments, stats will display a
list of subjects, and the total number of students and
classes for each subject, like so:</p>
<div class="highlight-python"><pre>% ./statistics
Subjects are:
bw101     Introductory Basketweaving 1        classes: 2, students: 28
bw232     Poststructuralist basketweaving     classes: 2  students: 19
bw290     Non-Euclidean basketweaving         classes: 2  students: 4</pre>
</div>
<p>If run with --student and a student ID, it
should print a list of all the classes the specified student
is enrolled in, including subject code and name, location
and time:</p>
<div class="highlight-python"><pre>% ./statistics --student 1123445
bw201 (Baskets throughout History), Mon 11.30, in 2.6.10
bw340 (Quantum Basketweaving), Thu 13.30, in 23.5.4</pre>
</div>
<p>stats should look for the name of the data directory in
the environment variable ENROLDIR; if it does not
exist, it should look in the “data” subdirectory of
the current directory. If both fail (i.e., if
ENROLDIR is invalid, or if ENROLDIR is
undefined and the current directory has no data
directory in it), it should print an error message and
exit.</p>
</div>
</div>