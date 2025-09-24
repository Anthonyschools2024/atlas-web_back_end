0x03. Pagination

Description 📖

This project is focused on understanding and implementing pagination, a crucial technique for handling large datasets in web development and APIs. We will explore several methods for dividing data into discrete pages, starting from a simple offset-based approach and moving towards more advanced and robust solutions like HATEOAS (Hypermedia as the Engine of Application State) and deletion-resilient pagination.

Learning Objectives 🎯

By the end of this project, you will be able to explain and implement the following:

    How to paginate a dataset using simple page and page_size parameters.

    How to create a more discoverable API using hypermedia pagination (HATEOAS).

    How to implement a deletion-resilient pagination strategy to ensure data consistency.

Requirements 🔧

    Environment: All files will be interpreted/compiled on Ubuntu 20.04 LTS.

    Python Version: python3 (version 3.9).

    Coding Style: All code must adhere to the pycodestyle style (version 2.5.*).

    Documentation: Every module, function, and class must be thoroughly documented and type-annotated.

    Executable Files: The first line of all your files must be #!/usr/bin/env python3.

Setup & Data 📊

All tasks will use the following data file. Please ensure it is in your project directory.

    Popular_Baby_Names.csv

Tasks 📂

0. Simple helper function

    0-simple_helper_function.py: Contains a function index_range that takes page and page_size as arguments and returns a tuple with the start and end index for a particular page.

1. Simple pagination

    1-simple_pagination.py: Implements a Server class with a get_page method that uses the index_range function to return the correct page of a dataset.

2. Hypermedia pagination

    2-hypermedia_pagination.py: Extends the Server class with a get_hyper method that returns a dictionary containing pagination details like page, page_size, data, next_page, prev_page, and total_pages.

3. Deletion-resilient hypermedia pagination

    3-hypermedia_del_pagination.py: Implements a get_hyper_index method that ensures the pagination is resilient to data deletions that may occur between requests.