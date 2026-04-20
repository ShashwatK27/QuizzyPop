import json

user_payload = {
  "Machine Learning": [
    {"question":"What type of learning uses labeled data?","options":["Unsupervised","Reinforcement","Supervised","Semi-supervised"],"answer":"Supervised"},
    {"question":"Which problem is classification?","options":["House price","Temperature","Spam detection","Stock price"],"answer":"Spam detection"},
    {"question":"Overfitting means:","options":["Good generalization","Fits train not test","Too simple","No data"],"answer":"Fits train not test"},
    {"question":"Underfitting occurs when:","options":["Too complex","Too simple","Too accurate","Overtrained"],"answer":"Too simple"},
    {"question":"Logistic regression is used for:","options":["Regression","Classification","Clustering","PCA"],"answer":"Classification"},
    {"question":"Gradient descent is used to:","options":["Maximize loss","Minimize loss","Normalize","Cluster"],"answer":"Minimize loss"},
    {"question":"Learning rate controls:","options":["Accuracy","Step size","Features","Labels"],"answer":"Step size"},
    {"question":"Confusion matrix is for:","options":["Regression","Clustering","Classification","Scaling"],"answer":"Classification"},
    {"question":"Precision measures:","options":["TP/(TP+FP)","TP/(TP+FN)","TN/(TN+FP)","All"],"answer":"TP/(TP+FP)"},
    {"question":"Recall measures:","options":["TP/(TP+FP)","TP/(TP+FN)","TN/(TN+FP)","Accuracy"],"answer":"TP/(TP+FN)"},
    {"question":"F1-score is:","options":["Mean","Harmonic mean","Sum","Diff"],"answer":"Harmonic mean"},
    {"question":"KNN stands for:","options":["Kernel NN","K Nearest Neighbors","Known NN","Key NN"],"answer":"K Nearest Neighbors"},
    {"question":"K-means is:","options":["Supervised","Unsupervised","Reinforcement","None"],"answer":"Unsupervised"},
    {"question":"PCA is used for:","options":["Clustering","Regression","Dimensionality reduction","Classification"],"answer":"Dimensionality reduction"},
    {"question":"Random forest is:","options":["Single tree","Multiple trees","Linear model","Cluster"],"answer":"Multiple trees"},
    {"question":"Bias refers to:","options":["High variance","Wrong assumptions","Noise","Scaling"],"answer":"Wrong assumptions"},
    {"question":"Variance refers to:","options":["Mean","Sensitivity to data","Bias","Error"],"answer":"Sensitivity to data"},
    {"question":"Regularization helps:","options":["Overfit","Reduce overfit","Increase data","Remove labels"],"answer":"Reduce overfit"},
    {"question":"L1 is called:","options":["Ridge","Lasso","Elastic","None"],"answer":"Lasso"},
    {"question":"Clustering is:","options":["Supervised","Unsupervised","Reinforcement","Semi"],"answer":"Unsupervised"},
    {"question":"ROC curve plots:","options":["TPR vs FPR","Precision vs Recall","Loss vs Epoch","None"],"answer":"TPR vs FPR"},
    {"question":"Feature scaling needed for:","options":["Tree","KNN","Forest","None"],"answer":"KNN"},
    {"question":"Cross-validation is for:","options":["Training","Testing reliability","Scaling","Cleaning"],"answer":"Testing reliability"},
    {"question":"Logistic output is:","options":["Continuous","Probability","Integer","Binary"],"answer":"Probability"},
    {"question":"Imbalanced metric:","options":["Accuracy","F1","Mean","Variance"],"answer":"F1"}
  ],

  "Operating Systems": [
    {"question":"OS is:","options":["Compiler","Interface","App","DB"],"answer":"Interface"},
    {"question":"Process is:","options":["File","Program in execution","Memory","CPU"],"answer":"Program in execution"},
    {"question":"PCB stands for:","options":["Program block","Process control block","Process code","None"],"answer":"Process control block"},
    {"question":"CPU scheduling decides:","options":["Memory","CPU","Disk","File"],"answer":"CPU"},
    {"question":"FCFS means:","options":["Fast","First come first serve","File","None"],"answer":"First come first serve"},
    {"question":"Round Robin uses:","options":["Priority","Time quantum","FIFO","None"],"answer":"Time quantum"},
    {"question":"Deadlock is:","options":["Crash","Wait forever","Fast exec","None"],"answer":"Wait forever"},
    {"question":"Semaphore used for:","options":["Memory","Sync","Disk","CPU"],"answer":"Sync"},
    {"question":"Paging avoids:","options":["Internal","External","Deadlock","None"],"answer":"External"},
    {"question":"Thrashing is:","options":["High CPU","High paging","Low mem","None"],"answer":"High paging"},
    {"question":"Virtual memory uses:","options":["RAM","Disk","Cache","Reg"],"answer":"Disk"},
    {"question":"Preemptive:","options":["FCFS","RR","FIFO","None"],"answer":"RR"},
    {"question":"Critical section deals with:","options":["CPU","Sync","Mem","Disk"],"answer":"Sync"},
    {"question":"Starvation:","options":["Deadlock","No CPU","Loop","Crash"],"answer":"No CPU"},
    {"question":"Banker algo avoids:","options":["Starvation","Deadlock","Paging","None"],"answer":"Deadlock"},
    {"question":"Context switch:","options":["Mem swap","State change","Disk","None"],"answer":"State change"},
    {"question":"Kernel is:","options":["App","Core OS","Compiler","None"],"answer":"Core OS"},
    {"question":"Multithreading improves:","options":["Mem","CPU util","Disk","None"],"answer":"CPU util"},
    {"question":"Internal frag in:","options":["Paging","Segmentation","Both","None"],"answer":"Paging"},
    {"question":"External frag in:","options":["Paging","Segmentation","Both","None"],"answer":"Segmentation"},
    {"question":"Mutual exclusion:","options":["Parallel","Single access","Fast","None"],"answer":"Single access"},
    {"question":"I/O bound:","options":["CPU heavy","IO heavy","None","Idle"],"answer":"IO heavy"},
    {"question":"CPU bound:","options":["CPU heavy","IO heavy","None","Idle"],"answer":"CPU heavy"},
    {"question":"FIFO is:","options":["Scheduling","Memory","Disk","None"],"answer":"Scheduling"},
    {"question":"Dispatcher does:","options":["Assign CPU","Free mem","Disk read","None"],"answer":"Assign CPU"}
  ],

  "DBMS": [
    {"question":"DBMS stands for:","options":["Data base","Database Management System","Data system","None"],"answer":"Database Management System"},
    {"question":"SQL is:","options":["Lang","OS","DB","None"],"answer":"Lang"},
    {"question":"Primary key:","options":["Duplicate","Unique","Null","None"],"answer":"Unique"},
    {"question":"Foreign key:","options":["Unique","Relation","Sort","None"],"answer":"Relation"},
    {"question":"Normalization reduces:","options":["Redundancy","Speed","Security","None"],"answer":"Redundancy"},
    {"question":"1NF removes:","options":["Partial dep","Repeating groups","Transitive","None"],"answer":"Repeating groups"},
    {"question":"2NF removes:","options":["Partial","Transitive","Both","None"],"answer":"Partial"},
    {"question":"3NF removes:","options":["Partial","Transitive","Both","None"],"answer":"Transitive"},
    {"question":"Join is used for:","options":["Insert","Combine tables","Delete","None"],"answer":"Combine tables"},
    {"question":"Index improves:","options":["Insert","Search","Delete","None"],"answer":"Search"},
    {"question":"ACID stands for:","options":["Atomicity etc","None","DB","Lang"],"answer":"Atomicity etc"},
    {"question":"Transaction is:","options":["Single op","Set ops","None","File"],"answer":"Set ops"},
    {"question":"Deadlock in DB:","options":["Crash","Wait","None","Fast"],"answer":"Wait"},
    {"question":"ER model:","options":["Graph","Diagram","Code","None"],"answer":"Diagram"},
    {"question":"Entity:","options":["Object","Key","Rel","None"],"answer":"Object"},
    {"question":"Attribute:","options":["Property","Key","Table","None"],"answer":"Property"},
    {"question":"Candidate key:","options":["Unique","Dup","Null","None"],"answer":"Unique"},
    {"question":"Super key:","options":["Unique set","Dup","Null","None"],"answer":"Unique set"},
    {"question":"DDL includes:","options":["Select","Create","Insert","None"],"answer":"Create"},
    {"question":"DML includes:","options":["Create","Insert","Drop","None"],"answer":"Insert"},
    {"question":"View is:","options":["Table","Virtual table","File","None"],"answer":"Virtual table"},
    {"question":"Trigger is:","options":["Auto action","Manual","None","File"],"answer":"Auto action"},
    {"question":"Stored procedure:","options":["Code","Data","File","None"],"answer":"Code"},
    {"question":"Concurrency control:","options":["Speed","Consistency","None","Size"],"answer":"Consistency"},
    {"question":"Locking ensures:","options":["Speed","Isolation","None","Size"],"answer":"Isolation"}
  ],

  "Software Engineering": [
    {"question":"SDLC is:","options":["Life cycle","Code","DB","None"],"answer":"Life cycle"},
    {"question":"Waterfall is:","options":["Iterative","Sequential","Agile","None"],"answer":"Sequential"},
    {"question":"Agile is:","options":["Rigid","Flexible","None","Slow"],"answer":"Flexible"},
    {"question":"Scrum uses:","options":["Sprint","Waterfall","None","Code"],"answer":"Sprint"},
    {"question":"Unit testing:","options":["Whole","Module","DB","None"],"answer":"Module"},
    {"question":"Integration testing:","options":["Modules together","Single","None","DB"],"answer":"Modules together"},
    {"question":"System testing:","options":["Full system","Unit","None","Code"],"answer":"Full system"},
    {"question":"Black box:","options":["Code","Functionality","None","Mem"],"answer":"Functionality"},
    {"question":"White box:","options":["Code","Function","None","UI"],"answer":"Code"},
    {"question":"Requirement is:","options":["Need","Code","DB","None"],"answer":"Need"},
    {"question":"Feasibility:","options":["Possible","Code","None","File"],"answer":"Possible"},
    {"question":"Risk mgmt:","options":["Avoid issues","Code","None","DB"],"answer":"Avoid issues"},
    {"question":"UML is:","options":["Diagram","Code","None","DB"],"answer":"Diagram"},
    {"question":"Use case:","options":["Scenario","Code","None","File"],"answer":"Scenario"},
    {"question":"Version control:","options":["Track","Delete","None","Run"],"answer":"Track"},
    {"question":"Git is:","options":["VCS","DB","OS","None"],"answer":"VCS"},
    {"question":"CI/CD:","options":["Auto deploy","Manual","None","DB"],"answer":"Auto deploy"},
    {"question":"Bug:","options":["Error","Feature","None","Code"],"answer":"Error"},
    {"question":"Debugging:","options":["Fix","Run","None","Stop"],"answer":"Fix"},
    {"question":"Maintenance:","options":["Update","Delete","None","Code"],"answer":"Update"},
    {"question":"Prototyping:","options":["Model","Code","None","DB"],"answer":"Model"},
    {"question":"Spiral model:","options":["Risk based","Linear","None","Fast"],"answer":"Risk based"},
    {"question":"Verification:","options":["Correct build","Test","None","Run"],"answer":"Correct build"},
    {"question":"Validation:","options":["Right product","Code","None","Run"],"answer":"Right product"},
    {"question":"Deployment:","options":["Release","Delete","None","Stop"],"answer":"Release"}
  ],

  "DAA": [
    {"question":"DAA is:","options":["Algo design","DB","OS","None"],"answer":"Algo design"},
    {"question":"Time complexity:","options":["Time","Mem","Code","None"],"answer":"Time"},
    {"question":"Binary search:","options":["O(n)","O(log n)","O(n2)","O(1)"],"answer":"O(log n)"},
    {"question":"Linear search:","options":["O(n)","O(log n)","O(1)","O(n2)"],"answer":"O(n)"},
    {"question":"Merge sort:","options":["O(n log n)","O(n2)","O(n)","O(log n)"],"answer":"O(n log n)"},
    {"question":"Quick sort avg:","options":["O(n log n)","O(n2)","O(n)","O(1)"],"answer":"O(n log n)"},
    {"question":"Worst quick sort:","options":["O(n log n)","O(n2)","O(n)","O(1)"],"answer":"O(n2)"},
    {"question":"Greedy uses:","options":["Local opt","Global","Random","None"],"answer":"Local opt"},
    {"question":"DP uses:","options":["Overlap","Random","None","Greedy"],"answer":"Overlap"},
    {"question":"Recursion is:","options":["Self call","Loop","None","Code"],"answer":"Self call"},
    {"question":"Stack used in:","options":["Recursion","Loop","None","Sort"],"answer":"Recursion"},
    {"question":"Heap is:","options":["Tree","Graph","Array","None"],"answer":"Tree"},
    {"question":"Graph is:","options":["Nodes+edges","Array","None","Tree"],"answer":"Nodes+edges"},
    {"question":"BFS uses:","options":["Queue","Stack","None","Heap"],"answer":"Queue"},
    {"question":"DFS uses:","options":["Stack","Queue","None","Heap"],"answer":"Stack"},
    {"question":"Dijkstra finds:","options":["Shortest path","Sort","None","Search"],"answer":"Shortest path"},
    {"question":"Prim algo:","options":["MST","Path","None","Sort"],"answer":"MST"},
    {"question":"Kruskal:","options":["MST","Path","None","Sort"],"answer":"MST"},
    {"question":"NP complete:","options":["Hard","Easy","None","Fast"],"answer":"Hard"},
    {"question":"Big O:","options":["Worst","Best","Avg","None"],"answer":"Worst"},
    {"question":"Big Omega:","options":["Best","Worst","Avg","None"],"answer":"Best"},
    {"question":"Big Theta:","options":["Tight","Worst","Best","None"],"answer":"Tight"},
    {"question":"Divide conquer:","options":["Split","Merge","None","Sort"],"answer":"Split"},
    {"question":"Backtracking:","options":["Try all","Greedy","None","Sort"],"answer":"Try all"},
    {"question":"Branch bound:","options":["Optimization","Sort","None","Search"],"answer":"Optimization"}
  ]
}

subject_map = {
    "Machine Learning": "machine_learning",
    "Operating Systems": "operating_systems",
    "DBMS": "dbms",
    "Software Engineering": "software_engineering",
    "DAA": "daa"
}

fixture = []
pk_counter = 1

for subject_name, questions in user_payload.items():
    subject_code = subject_map[subject_name]
    for q in questions:
        options = q["options"]
        if len(options) != 4:
            options = options + ["None"] * (4 - len(options))
            
        try:
            correct_index = options.index(q["answer"])
        except ValueError:
            correct_index = 0

        import random
        difficulties = ['easy', 'medium', 'hard']
        difficulty = random.choice(difficulties)

        fixture.append({
            "model": "quiz.question",
            "pk": pk_counter,
            "fields": {
                "question": q["question"],
                "option_a": options[0],
                "option_b": options[1],
                "option_c": options[2],
                "option_d": options[3],
                "correct_index": correct_index,
                "subject": subject_code,
                "difficulty": difficulty
            }
        })
        pk_counter += 1

with open("quiz/fixtures/subject_questions.json", "w") as f:
    json.dump(fixture, f, indent=2)

print(f"Generated {len(fixture)} questions.")
