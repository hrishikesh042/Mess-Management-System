Canteen => Project
food => App
Accounts => App

==================================================================================

E-Mail Light Weight Server
Command:
    python -m smtpd -n -c DebuggingServer localhost:1025

===================================================================================

Given Twelve Points to executie in the Program
=> [1] Date and Time >> Done

=> [2] User Authentication >> Done
            -> SignIn >> Done
            -> SignOut >> Done
            -> Registration >> Done
            -> Forget/Reset PassWord >> Done

=> [3] Report

=> [4] Graph

=> [5] Data Table
    -> Sort >> Done
    -> Search >> Done
    -> CURD Operations
        -> Create / Add
        -> UpDate >> Done
        -> Read >> Default >> Done
        -> Delete >> Done
    -> [6] Import/Export Data
        -> Import Data
        -> Export Data
    -> [7] PDF

=> [8] Function Based Views >> Done

=> [9] Class Base View >> Done
            -> Eg:    path('about/', TemplateView.as_view(template_name="about.html")),
            -> https://docs.djangoproject.com/en/4.0/topics/class-based-views/

=> [10] Uploading Images >> Done

=> [11] Front End >> Done

=> [12] 

Task Given => 12
Completed => 6                                                           [[[    12 :: 6     ]]]


========================================================================================================

Analysis of DashBoard

    >> Normal Nav Bar
    >> Grid of 4 >> for Data Analysis
            -> Orders Recived
            -> Home Delivery
            -> Pendings
            -> Payments Completions
    >> ADD Dish >> Buttopn - Add New Dish in Data Base
    >> View Dishes >> Button - Data Table of Dishes
    >> Customer >> List/DataTable
    >> Orders >> List/DataTable
