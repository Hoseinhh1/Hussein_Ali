# Git / GitHub

## Learn

> ###### What does Git / GitHub mean?

* ### Git:

  * #### Git is a tool designed for **Version Control**, which means it helps you to control the versions of your project or application. Using Git, you can track changes in your codebase, revert to previous states, and collaborate with others without overwriting each other's work.
  * #### Git is distributed, meaning that every developer has a full copy of the project history on their local machine. This allows for powerful features like branching and merging, enabling multiple developers to work on different features simultaneously.
  * #### **Git** هو أداة للتحكم في نسخ الأكواد البرمجية، بمعنى أنه يمكنك من إدارة الإصدارات المختلفة من مشروعك أو تطبيقك. باستخدام Git، يمكنك تتبع التغييرات في قاعدة الكود، العودة إلى الحالات السابقة، والتعاون مع الآخرين دون أن يكتب أحد فوق عمل الآخر.
  * #### Git هو نظام موزع، بمعنى أن كل مطور لديه نسخة كاملة من تاريخ المشروع على جهازه المحلي. هذا يتيح ميزات قوية مثل التفريع (Branching) والدمج (Merging)، مما يسمح لعدة مطورين بالعمل على ميزات مختلفة في نفس الوقت.

---

### Basic Git Commands | الأوامر الأساسية لـ Git

1. **git init**

   - **English:** Initializes a new Git repository in your project directory. It creates a hidden `.git` folder where all the version history is stored.
   - **العربية:** يقوم بتهيئة مستودع Git جديد في دليل مشروعك. ينشئ مجلدًا مخفيًا `.git` حيث يتم تخزين جميع إصدارات المشروع.
   - **Usage | الاستخدام:**
     ```bash
     git init
     ```
2. **git clone**

   - **English:** Clones an existing Git repository from a remote server to your local machine. This creates a copy of the repository on your computer.
   - **العربية:** يقوم بنسخ مستودع Git موجود من خادم بعيد إلى جهازك المحلي. هذا ينشئ نسخة من المستودع على جهاز الكمبيوتر الخاص بك.
   - **Usage | الاستخدام:**
     ```bash
     git clone <repository-url>
     ```
3. **git add**

   - **English:** Stages changes in your working directory for the next commit. You can add specific files or use `git add .` to stage all changes.
   - **العربية:** يقوم بإضافة التغييرات في دليل العمل الخاص بك لتكون جاهزة للإلتزام التالي. يمكنك إضافة ملفات معينة أو استخدام `git add .` لإضافة جميع التغييرات.
   - **Usage | الاستخدام:**
     ```bash
     git add <file-name>
     git add .
     ```
4. **git commit**

   - **English:** Records a snapshot of the staged changes in your repository. This creates a new version in your project history with a message describing the changes.
   - **العربية:** يقوم بتسجيل لقطة من التغييرات التي تم إضافتها في المستودع الخاص بك. هذا ينشئ إصدارًا جديدًا في تاريخ المشروع مع رسالة تصف التغييرات.
   - **Usage | الاستخدام:**
     ```bash
     git commit -m "Your commit message"
     ```
5. **git status**

   - **English:** Shows the status of your working directory and staging area, indicating which files have changes that are staged for commit, unstaged, or untracked.
   - **العربية:** يعرض حالة دليل العمل ومنطقة الانتظار، ويشير إلى الملفات التي تم تعديلها وتجهز للإلتزام، أو لم يتم إضافتها بعد، أو لم يتم تتبعها.
   - **Usage | الاستخدام:**
     ```bash
     git status
     ```
6. **git push**

   - **English:** Uploads your local repository content to a remote repository, such as GitHub. This is how you share your changes with others.
   - **العربية:** يقوم برفع محتوى مستودعك المحلي إلى مستودع بعيد مثل GitHub. هذه هي الطريقة التي تشارك بها التغييرات مع الآخرين.
   - **Usage | الاستخدام:**
     ```bash
     git push origin <branch-name>
     ```
7. **git pull**

   - **English:** Fetches and merges changes from a remote repository into your current branch. This is how you update your local copy with changes from others.
   - **العربية:** يقوم بجلب ودمج التغييرات من مستودع بعيد إلى الفرع الحالي لديك. هذه هي الطريقة التي تحدث بها نسختك المحلية بالتغييرات من الآخرين.
   - **Usage | الاستخدام:**
     ```bash
     git pull
     ```
8. **git branch**

   - **English:** Lists, creates, or deletes branches. Branching allows you to work on different features or bug fixes independently from the main codebase.
   - **العربية:** يقوم بعرض، إنشاء، أو حذف الفروع. التفريع يتيح لك العمل على ميزات أو إصلاحات للأخطاء بشكل مستقل عن قاعدة الكود الرئيسية.
   - **Usage | الاستخدام:**
     ```bash
     git branch
     git branch <branch-name>
     ```
9. **git merge**

   - **English:** Combines changes from different branches into one. After working on a feature branch, you merge it back into the main branch.
   - **العربية:** يقوم بدمج التغييرات من الفروع المختلفة في فرع واحد. بعد العمل على فرع ميزة معين، تقوم بدمجه مرة أخرى في الفرع الرئيسي.
   - **Usage | الاستخدام:**
     ```bash
     git merge <branch-name>
     ```

---

* ### GitHub:

  * #### GitHub is a web-based platform that uses Git for version control and collaboration. It allows developers to host their Git repositories online, making it easy to share code, collaborate with others, and contribute to open-source projects.
  * #### **GitHub** هو منصة على الويب تستخدم Git للتحكم في الإصدارات والتعاون. يتيح GitHub للمطورين استضافة مستودعاتهم البرمجية عبر الإنترنت، مما يسهل مشاركة الأكواد، والتعاون مع الآخرين، والمساهمة في المشاريع مفتوحة المصدر.
  * #### يوفر GitHub ميزات إضافية مثل تتبع المشاكل، طلبات الدمج (Pull Requests)، والتكامل المستمر (Continuous Integration)، مما يجعله أداة قوية لفرق تطوير البرمجيات.

---

### Additional Resources | موارد إضافية

- [Git Official Documentation](https://git-scm.com/doc) | [الوثائق الرسمية لـ Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/) | [دروس GitHub](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) | [ورقة مرجعية لـ Git](https://education.github.com/git-cheat-sheet-education.pdf)
