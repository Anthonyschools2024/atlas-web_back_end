0x01. Caching

This project is a deep dive into caching systems and their underlying algorithms. You will implement several common cache replacement policies in Python, learning the principles behind First-In First-Out (FIFO), Last-In First-Out (LIFO), Least Recently Used (LRU), Most Recently Used (MRU), and Least Frequently Used (LFU).

All caching systems inherit from a provided base class BaseCaching.

Learning Objectives 🧠

At the end of this project, you are expected to be able to explain:

    What a caching system is and its purpose.

    The limitations of a caching system.

    The meaning and implementation of various replacement policies:

        FIFO (First-In, First-Out)

        LIFO (Last-In, First-Out)

        LRU (Least Recently Used)

        MRU (Most Recently Used)

        LFU (Least Frequently Used)

Requirements

Environment

    OS: Ubuntu 20.04 LTS

    Language: Python 3.9

    Style Guide: pycodestyle (version 2.5)

Code Standards

    All files must be executable.

    The first line of all Python files must be #!/usr/bin/env python3.

    All files must end with a new line.

    All modules, classes, and functions must be documented with meaningful docstrings.

    A README.md file at the root of the project folder is mandatory.

File Descriptions 📂

    base_caching.py: The parent class for all caching systems. It provides the cache_data dictionary.

    0-basic_cache.py: Contains the BasicCache class, a simple caching system with no size limit.

    1-fifo_cache.py: Contains the FIFOCache class, which implements the FIFO replacement policy.

    2-lifo_cache.py: Contains the LIFOCache class, which implements the LIFO replacement policy.

    3-lru_cache.py: Contains the LRUCache class, which implements the LRU replacement policy.

    4-mru_cache.py: Contains the MRUCache class, which implements the MRU replacement policy.

    5-lfu_cache.py: Contains the LFUCache class, which implements the LFU replacement policy.

    *-main.py: Test files provided for each task to verify the functionality of the implemented caching systems.