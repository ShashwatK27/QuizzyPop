import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizzypop.settings')
django.setup()

from quiz.models import Question

# A dictionary mapping the exact question text to a detailed, educational explanation
explanations_map = {
    # Machine Learning
    "What type of learning uses labeled data?": "Supervised learning uses labeled datasets to train algorithms to classify data or predict outcomes accurately.",
    "Which problem is classification?": "Spam detection is a classification problem because it sorts data into discrete categories (e.g., 'spam' or 'not spam').",
    "Overfitting means:": "Overfitting occurs when a model learns the training data too perfectly, capturing random noise and failing to generalize to new data.",
    "Underfitting occurs when:": "Underfitting happens when a model is too simple to capture the underlying structure of the data, performing poorly on both training and test sets.",
    "Logistic regression is used for:": "Despite the word 'regression' in its name, Logistic Regression is actually a statistical model used for binary classification tasks.",
    "Gradient descent is used to:": "Gradient descent is an optimization algorithm used to minimize the loss function by iteratively moving in the direction of steepest descent.",
    "Learning rate controls:": "The learning rate is a hyperparameter that determines the step size at each iteration while moving toward a minimum of a loss function.",
    "Confusion matrix is for:": "A confusion matrix is a table used to evaluate the performance of a classification model, showing true positives, false positives, etc.",
    "Precision measures:": "Precision is TP/(TP+FP). It measures the accuracy of positive predictions (i.e., of all predicted positives, how many were actually positive).",
    "Recall measures:": "Recall is TP/(TP+FN). It measures the ability of a model to find all the relevant cases within a dataset.",
    "F1-score is:": "The F1-score is the harmonic mean of precision and recall, providing a single metric that balances both concerns, especially for imbalanced datasets.",
    "KNN stands for:": "KNN stands for K-Nearest Neighbors, a simple, instance-based learning algorithm where a new data point is classified based on its closest neighbors.",
    "K-means is:": "K-means is an unsupervised clustering algorithm that partitions unlabeled data into K distinct, non-overlapping subgroups.",
    "PCA is used for:": "Principal Component Analysis (PCA) is a dimensionality reduction technique used to simplify data while retaining the most important variance.",
    "Random forest is:": "Random Forest is an ensemble learning method that constructs multiple decision trees and merges them together to get a more accurate and stable prediction.",
    "Bias refers to:": "Bias refers to the error introduced by approximating a real-world problem with a simplified model (wrong assumptions).",
    "Variance refers to:": "Variance refers to the model's sensitivity to small fluctuations in the training set, often leading to overfitting if too high.",
    "Regularization helps:": "Regularization techniques (like L1 and L2) add a penalty to the loss function to reduce overfitting and improve model generalization.",
    "L1 is called:": "L1 regularization is also known as Lasso Regression. It can shrink some model coefficients to exactly zero, performing feature selection.",
    "Clustering is:": "Clustering is an unsupervised learning task that involves grouping a set of objects so that objects in the same group are more similar to each other.",
    "ROC curve plots:": "An ROC curve plots the True Positive Rate (TPR) against the False Positive Rate (FPR) at various threshold settings.",
    "Feature scaling needed for:": "Feature scaling (like normalization) is crucial for distance-based algorithms like KNN to ensure all features contribute equally to the distance.",
    "Cross-validation is for:": "Cross-validation is a resampling procedure used to evaluate machine learning models on a limited data sample, testing their reliability and generalization.",
    "Logistic output is:": "The output of a logistic regression model is a probability value between 0 and 1, obtained using the sigmoid function.",
    "Imbalanced metric:": "For imbalanced datasets, accuracy can be misleading. The F1-score is a much better metric as it balances precision and recall.",

    # Operating Systems
    "OS is:": "An Operating System acts as an interface between the user and the computer hardware, managing resources and providing common services.",
    "Process is:": "A process is a program in execution, representing the fundamental unit of work in a modern time-sharing system.",
    "PCB stands for:": "Process Control Block (PCB) is a data structure used by the OS to store all the information about a specific process.",
    "CPU scheduling decides:": "CPU scheduling determines which process in the ready queue gets to use the CPU next, maximizing CPU utilization.",
    "FCFS means:": "First Come First Serve (FCFS) is the simplest scheduling algorithm that executes processes in the exact order they arrive.",
    "Round Robin uses:": "Round Robin scheduling assigns a fixed time quantum to each process in equal portions and in circular order, ensuring fairness.",
    "Deadlock is:": "A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.",
    "Semaphore used for:": "Semaphores are synchronization tools (integer variables) used to control access to common resources by multiple processes in a concurrent system.",
    "Paging avoids:": "Paging is a memory management scheme that eliminates external fragmentation by dividing physical memory into fixed-sized blocks called frames.",
    "Thrashing is:": "Thrashing occurs when a system spends more time paging (swapping data between RAM and disk) than executing actual processes.",
    "Virtual memory uses:": "Virtual memory uses secondary storage (disk) as an extension of main memory (RAM), allowing programs larger than physical memory to run.",
    "Preemptive:": "Round Robin (RR) is a preemptive algorithm because it forcefully interrupts a process when its time quantum expires.",
    "Critical section deals with:": "The critical section is a segment of code where shared resources are accessed. It requires synchronization to prevent race conditions.",
    "Starvation:": "Starvation is a problem where a process is perpetually denied necessary resources (like CPU time) to process its work.",
    "Banker algo avoids:": "The Banker's Algorithm is a resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation of predetermined maximum possible amounts of all resources.",
    "Context switch:": "A context switch is the process of storing the state of an active process and restoring the state of another, allowing multiple processes to share a single CPU.",
    "Kernel is:": "The kernel is the core component of an OS that has complete control over everything in the system, managing hardware and software interactions.",
    "Multithreading improves:": "Multithreading allows multiple threads within a single process to execute concurrently, greatly improving CPU utilization and application responsiveness.",
    "Internal frag in:": "Internal fragmentation occurs in paging when memory is allocated in fixed-size blocks, and the allocated block is slightly larger than the requested memory.",
    "External frag in:": "External fragmentation happens in segmentation when free memory space is broken into little pieces, making it hard to allocate contiguous memory for a new process.",
    "Mutual exclusion:": "Mutual exclusion is a property of concurrency control preventing race conditions by ensuring only one process accesses a critical section at a time.",
    "I/O bound:": "An I/O bound process spends more of its time doing I/O operations than doing computational work.",
    "CPU bound:": "A CPU bound process spends the majority of its time performing computations rather than waiting for I/O operations.",
    "FIFO is:": "First-In-First-Out (FIFO) is a scheduling algorithm (or page replacement algorithm) that processes items in the exact order they arrived.",
    "Dispatcher does:": "The dispatcher is the module that actually gives control of the CPU to the process selected by the short-term scheduler.",

    # DBMS
    "DBMS stands for:": "Database Management System (DBMS) is software designed to store, retrieve, define, and manage data in a database.",
    "SQL is:": "Structured Query Language (SQL) is the standard programming language specifically designed for managing and manipulating relational databases.",
    "Primary key:": "A primary key is a specific choice of a minimal set of attributes that uniquely identifies a record in a database table.",
    "Foreign key:": "A foreign key is a column or group of columns in a relational database table that provides a link between data in two tables.",
    "Normalization reduces:": "Normalization is the process of organizing data to minimize redundancy and improve data integrity.",
    "1NF removes:": "First Normal Form (1NF) eliminates repeating groups by requiring that every column in a table holds only atomic (indivisible) values.",
    "2NF removes:": "Second Normal Form (2NF) removes partial dependencies, meaning all non-key attributes must depend on the entire primary key.",
    "3NF removes:": "Third Normal Form (3NF) removes transitive dependencies, ensuring that non-key attributes depend only on the primary key, not on other non-key attributes.",
    "Join is used for:": "A JOIN clause is used to combine rows from two or more tables, based on a related column between them.",
    "Index improves:": "Indexes are special lookup tables that the database search engine can use to speed up data retrieval significantly.",
    "ACID stands for:": "ACID stands for Atomicity, Consistency, Isolation, and Durability—the four key properties that guarantee database transactions are processed reliably.",
    "Transaction is:": "A transaction is a single logical unit of work that performs one or more operations on a database, which must succeed or fail completely.",
    "Deadlock in DB:": "A deadlock in a database occurs when two or more transactions are waiting indefinitely for one another to give up locks.",
    "ER model:": "The Entity-Relationship (ER) model is a high-level conceptual data model diagram used to define the data elements and relationships for a specified system.",
    "Entity:": "In an ER model, an Entity is a real-world object or concept (like a Person or Product) that exists independently and has data stored about it.",
    "Attribute:": "An attribute is a property, trait, or characteristic of an entity, relationship, or another attribute in a database.",
    "Candidate key:": "A candidate key is a specific set of attributes that can uniquely identify a database record without any extraneous data.",
    "Super key:": "A super key is a set of one or more attributes that, taken collectively, allow us to identify uniquely a tuple in a relation.",
    "DDL includes:": "Data Definition Language (DDL) includes commands like CREATE, ALTER, and DROP that are used to define the database structure.",
    "DML includes:": "Data Manipulation Language (DML) includes commands like INSERT, UPDATE, and DELETE used for managing data within schema objects.",
    "View is:": "A View is a virtual table based on the result-set of an SQL statement. It doesn't store data itself but displays data from underlying tables.",
    "Trigger is:": "A trigger is a special type of stored procedure that automatically executes (or fires) when a specific event occurs in the database.",
    "Stored procedure:": "A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.",
    "Concurrency control:": "Concurrency control ensures that multiple transactions are executed simultaneously without violating the data consistency of a database.",
    "Locking ensures:": "Locking is a mechanism used in DBMS to ensure transaction isolation, preventing multiple transactions from modifying the same data simultaneously.",

    # Software Engineering
    "SDLC is:": "The Software Development Life Cycle (SDLC) is a framework defining tasks performed at each step in the software development process.",
    "Waterfall is:": "The Waterfall model is a sequential, linear design approach where progress flows downwards through phases like Conception, Initiation, Analysis, etc.",
    "Agile is:": "Agile is an iterative and flexible approach to software development that emphasizes continuous delivery, team collaboration, and adaptability.",
    "Scrum uses:": "Scrum is an Agile framework that breaks work into short, time-boxed iterations called Sprints.",
    "Unit testing:": "Unit testing isolates a section of code (a module or function) and verifies its correctness independently.",
    "Integration testing:": "Integration testing is the phase where individual software modules are combined and tested as a group to expose faults in the interaction between them.",
    "System testing:": "System testing is testing conducted on a complete, integrated system to evaluate the system's compliance with its specified requirements.",
    "Black box:": "Black Box testing focuses on the functional specifications of the software, ignoring the internal mechanism or code structure.",
    "White box:": "White Box testing involves testing the internal structures, logic, and workings of an application, requiring knowledge of the source code.",
    "Requirement is:": "A requirement is a specific need or condition that a software product must meet or possess to satisfy a contract or standard.",
    "Feasibility:": "A feasibility study analyzes whether a project is technically possible, financially viable, and profitable before development begins.",
    "Risk mgmt:": "Risk management is the process of identifying, analyzing, and mitigating potential issues that could negatively impact a software project.",
    "UML is:": "Unified Modeling Language (UML) is a standardized visual modeling language used in software engineering to design and document system architectures.",
    "Use case:": "A use case is a description of how a system interacts with its environment (users or other systems) by illustrating specific scenarios.",
    "Version control:": "Version control systems track and manage changes to software code over time, allowing multiple developers to collaborate without overwriting work.",
    "Git is:": "Git is the most popular distributed Version Control System (VCS), used for tracking changes in source code during software development.",
    "CI/CD:": "Continuous Integration and Continuous Deployment (CI/CD) automates the building, testing, and deployment of applications.",
    "Bug:": "A bug is an error, flaw, or fault in a computer program that causes it to produce an incorrect or unexpected result.",
    "Debugging:": "Debugging is the systematic process of finding and fixing the bugs or defects within a software program.",
    "Maintenance:": "Software maintenance is the process of modifying a software product after delivery to correct faults, improve performance, or adapt to a changed environment.",
    "Prototyping:": "Prototyping involves creating an incomplete, early model of the software to visualize requirements and gather user feedback.",
    "Spiral model:": "The Spiral model is a risk-driven process model that combines the iterative nature of prototyping with the systematic aspects of the Waterfall model.",
    "Verification:": "Verification asks 'Are we building the product right?' It ensures the software conforms to its specifications without actually executing the final product.",
    "Validation:": "Validation asks 'Are we building the right product?' It involves executing the software and testing if it actually fulfills the user's needs.",
    "Deployment:": "Deployment encompasses all the processes involved in getting new software or hardware up and running in its target environment (release).",

    # DAA
    "DAA is:": "Design and Analysis of Algorithms (DAA) is the study of creating efficient algorithms and analyzing their time and space complexity.",
    "Time complexity:": "Time complexity quantifies the amount of time taken by an algorithm to run as a function of the length of the input.",
    "Binary search:": "Binary search operates in O(log n) time by repeatedly dividing a sorted array in half, making it highly efficient.",
    "Linear search:": "Linear search has an O(n) time complexity because it sequentially checks each element of the list until a match is found.",
    "Merge sort:": "Merge Sort uses a divide-and-conquer strategy, guaranteeing an O(n log n) time complexity in all cases.",
    "Quick sort avg:": "On average, Quick Sort has an O(n log n) time complexity, making it one of the fastest sorting algorithms in practice.",
    "Worst quick sort:": "The worst-case time complexity for Quick Sort is O(n^2), which occurs when the pivot element is always the largest or smallest item.",
    "Greedy uses:": "A greedy algorithm builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate local optimal benefit.",
    "DP uses:": "Dynamic Programming (DP) solves complex problems by breaking them down into simpler overlapping subproblems and storing their results.",
    "Recursion is:": "Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem, typically implemented via a self-calling function.",
    "Stack used in:": "The call stack is the underlying data structure that tracks active subroutines in recursion.",
    "Heap is:": "A Heap is a specialized tree-based data structure that satisfies the heap property (e.g., in a max heap, the parent is always greater than its children).",
    "Graph is:": "A Graph is a non-linear data structure consisting of nodes (vertices) and the edges that connect them.",
    "BFS uses:": "Breadth-First Search (BFS) algorithm uses a Queue data structure to explore a graph level by level.",
    "DFS uses:": "Depth-First Search (DFS) uses a Stack data structure (or recursion) to explore as far as possible along each branch before backtracking.",
    "Dijkstra finds:": "Dijkstra's Algorithm is used for finding the shortest paths between nodes in a graph, which may represent, for example, road networks.",
    "Prim algo:": "Prim's algorithm is a greedy algorithm that finds a Minimum Spanning Tree (MST) for a weighted undirected graph.",
    "Kruskal:": "Kruskal's algorithm finds a Minimum Spanning Tree (MST) by sorting edges and adding them to the growing forest if they don't form a cycle.",
    "NP complete:": "NP-Complete problems are the hardest problems in NP; if a polynomial-time algorithm exists for one, it exists for all.",
    "Big O:": "Big O notation describes the worst-case scenario or the upper bound of an algorithm's time complexity.",
    "Big Omega:": "Big Omega (Ω) describes the best-case scenario or the lower bound of an algorithm's time complexity.",
    "Big Theta:": "Big Theta (Θ) bounds a function from above and below, representing a tight, exact bound on the time complexity.",
    "Divide conquer:": "Divide and Conquer is an algorithm design paradigm that recursively breaks down a problem into two or more sub-problems of the same or related type.",
    "Backtracking:": "Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, removing those solutions that fail to satisfy the constraints.",
    "Branch bound:": "Branch and Bound is an algorithm design paradigm generally used for solving combinatorial optimization problems, keeping track of the best solution found so far."
}

count = 0
for q in Question.objects.all():
    q_text = q.question.strip()
    if q_text in explanations_map:
        q.explanation = explanations_map[q_text]
        q.save()
        count += 1
    else:
        # Fallback if text doesn't exactly match
        for key, text in explanations_map.items():
            if key in q_text:
                q.explanation = text
                q.save()
                count += 1
                break

print(f"Updated {count} questions with highly specific, educational explanations!")
