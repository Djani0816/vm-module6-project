Introduction

In this assignment, I created a Virtual Memory simulation program using Python. The purpose of this project was to understand how operating systems manage memory when the amount of memory needed by processes is larger than the available physical RAM.

Normally, physical memory (RAM) can only store a limited number of pages at one time. Because of this limitation, operating systems use virtual memory to temporarily move pages between RAM and disk storage. This process is called swapping.

The main goal of this project was to simulate how virtual memory works internally. The program keeps track of which pages are currently loaded into physical memory and which pages exist only in virtual memory. The program also handles page faults, page replacement, dirty pages, and memory statistics.

While working on this assignment, I learned how operating systems:

Manage physical and virtual memory
Detect page faults
Replace pages using page replacement algorithms
Track modified pages using dirty bits
Improve performance by avoiding unnecessary disk writes

I implemented the entire project in Python because Python makes it easier to create classes and simulate memory structures using lists and objects.

Objectives

The objectives of this project are:

Create a virtual memory table and physical memory table.
Implement valid and dirty bits for pages.
Simulate loading pages into memory.
Detect page faults.
Replace pages using the Least Recently Used (LRU) algorithm.
Simulate swapping pages between RAM and disk.
Track memory statistics such as page faults and disk operations.
Programming Language

The program was implemented using Python.

Python was chosen because:

It simplifies class creation and data structures.
Lists can easily simulate memory frames.
The code is easier to read and test.
Python supports object-oriented programming which helps organize the memory simulation.
Program Design

I divided the program into several sections so that each part of the memory system could be implemented separately and tested step-by-step.

The major sections of the program are:

Page class creation
Physical memory setup
Virtual memory setup
Memory initialization
Memory access simulation
Page fault handling
LRU page replacement
Statistics tracking

I first created the data structures before implementing the swapping logic. This helped me test the memory tables first and then gradually add more functionality.

Page Class

The first thing I created in the program was the Page class.

The purpose of this class is to represent a single memory page in the virtual memory system. Instead of using simple variables, I used a class so that each page could store all information related to memory management.

The page class contains the following variables:

Variable	Purpose
process_id	Stores which process owns the page
page_number	Stores the page number
is_valid	Checks whether the page is currently in RAM
is_dirty	Checks whether the page has been modified
last_used	Stores the last time the page was accessed

I added the is_valid flag because the assignment required the program to determine whether a page is currently loaded into physical memory.

I added the is_dirty flag to track whether a page has been modified after being loaded into memory. Dirty pages must be written back to disk before removal.

The last_used variable was necessary for implementing the Least Recently Used (LRU) page replacement algorithm.

Using a class made the code easier to organize and allowed the memory tables to store complete page objects.

---|---| | process_id | Stores the process owner | | page_number | Stores the virtual page number | | is_valid | Determines whether the page is currently in RAM | | is_dirty | Determines whether the page has been modified | | last_used | Stores the last access time for LRU replacement |

The Page class is used to represent both physical and virtual memory pages.

Physical Memory

Physical memory simulates RAM.

The program creates:

physical_memory = [None] * PHYSICAL_MEMORY_SIZE

This stores the pages currently loaded into memory.

The physical memory size in this simulation is:

PHYSICAL_MEMORY_SIZE = 4

This means RAM can only hold 4 pages at one time.

Virtual Memory

Virtual memory stores all pages whether they are currently in RAM or not.

The program creates:

virtual_memory = [
Page(process_id=1, page_number=i)
for i in range(VIRTUAL_MEMORY_SIZE)
]

The virtual memory size is:

VIRTUAL_MEMORY_SIZE = 8

This means the system contains 8 virtual pages.

Memory Initialization

The initialize_memory() function loads the first four pages into physical memory.

Each loaded page is marked:

page.is_valid = True
page.is_dirty = False

This indicates:

The page is currently in RAM.
The page has not been modified.

The remaining pages stay invalid until they are needed.

Memory Access

After setting up the memory tables, I implemented the access_memory() function.

This function simulates how a process accesses memory during program execution.

Whenever a page is accessed, the program first checks whether the page is currently valid.

If the page is valid:

The page is already in RAM.
The access is completed normally.
The page usage time is updated.
If the operation is a write operation, the page is marked dirty.

If the page is invalid:

The program generates a page fault.
The page fault handler function is called.
The needed page is loaded into RAM.

The function also updates the last_used value every time a page is accessed. This is important because the LRU algorithm depends on tracking recent memory usage.

I tested the function using different page accesses and write operations to make sure that dirty pages and valid bits were updating correctly.

Example:

access_memory(1, write=True)

This statement accesses page 1 and marks it dirty because the operation simulates writing to memory.

Page Fault Handling

One of the most important parts of the project was implementing page fault handling.

A page fault occurs when a process tries to access a page that is not currently loaded into physical memory.

When this happens, the program calls the handle_page_fault() function.

The page fault handler performs several steps:

Finds the least recently used page in RAM.
Removes that page from physical memory.
Checks whether the page is dirty.
If dirty, the page is written to disk.
Loads the requested page into RAM.
Updates the page tables and memory statistics.

This process simulates how an actual operating system swaps pages between RAM and disk.

I used print statements throughout the program so that the memory changes could be clearly seen during execution. This made debugging easier and helped verify that pages were being replaced correctly.

Example output:

PAGE FAULT: Page 5 not in RAM
Removing Page 0
Loaded Page 5 into RAM

This output shows that the program correctly detected a missing page and replaced the least recently used page.

Least Recently Used (LRU) Algorithm

The project uses the Least Recently Used (LRU) page replacement algorithm.

LRU removes the page that has not been used for the longest amount of time.

The program tracks page usage using:

last_used

The function:

find_lru_page()

searches physical memory and returns the least recently used page.

This helps reduce unnecessary swapping and improves performance.

Dirty Page Optimization

The project also implements dirty page optimization.

If a page is dirty:

is_dirty = True

then the page must be written to disk before removal.

If the page is clean:

is_dirty = False

then the page can simply be removed without writing to disk.

This improves performance because unnecessary disk writes are avoided.

Statistics Tracking

The program tracks the following statistics:

Statistic	Description
Page Faults	Number of invalid page accesses
Disk Reads	Number of pages loaded into RAM
Disk Writes	Number of dirty pages written to disk

The statistics are displayed at the end of the program execution.

Challenges Faced

Some challenges during the implementation included:

Understanding the difference between virtual and physical memory.
Correctly updating valid and dirty bits.
Implementing the LRU replacement algorithm.
Tracking page usage times.
Updating memory tables after page replacement.

These challenges were solved by testing the program step-by-step and verifying memory changes after every operation.

Conclusion

Overall, this project helped me better understand how virtual memory works inside an operating system.

Before completing this assignment, I only understood the basic theory of virtual memory. After implementing the simulation, I was able to understand how the operating system keeps track of pages, handles page faults, swaps pages between RAM and disk, and improves performance using page replacement algorithms.

The most important concepts I learned from this assignment were:

The difference between physical and virtual memory
How valid and dirty bits are used
How page faults occur
How LRU page replacement works
Why operating systems try to minimize disk operations

I also learned how memory management can become more complicated when physical memory is limited.

