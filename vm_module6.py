class Page:
    def __init__(self, process_id=None, page_number=None):
        self.process_id = process_id
        self.page_number = page_number

        # Virtual Memory Flags
        self.is_valid = False
        self.is_dirty = False

        # Used for LRU replacement
        self.last_used = -1

    def __str__(self):
        return (
            f"PID={self.process_id}, "
            f"Page={self.page_number}, "
            f"Valid={self.is_valid}, "
            f"Dirty={self.is_dirty}, "
            f"LastUsed={self.last_used}"
        )


# -----------------------------
# CONFIGURATION
# -----------------------------

PHYSICAL_MEMORY_SIZE = 4
VIRTUAL_MEMORY_SIZE = 8

# Simulated clock for LRU
time_counter = 0

# Statistics
page_faults = 0
disk_reads = 0
disk_writes = 0

# -----------------------------
# MEMORY TABLES
# -----------------------------

# RAM frames
physical_memory = [None] * PHYSICAL_MEMORY_SIZE

# Virtual memory pages
virtual_memory = [
    Page(process_id=1, page_number=i)
    for i in range(VIRTUAL_MEMORY_SIZE)
]


# -----------------------------
# LOAD INITIAL PAGES INTO RAM
# -----------------------------

def initialize_memory():
    global disk_reads

    for i in range(PHYSICAL_MEMORY_SIZE):
        page = virtual_memory[i]

        page.is_valid = True
        page.is_dirty = False
        page.last_used = 0

        physical_memory[i] = page

        disk_reads += 1


# -----------------------------
# FIND LRU PAGE
# -----------------------------

def find_lru_page():
    lru_page = physical_memory[0]

    for page in physical_memory:
        if page.last_used < lru_page.last_used:
            lru_page = page

    return lru_page


# -----------------------------
# PAGE FAULT HANDLER
# -----------------------------

def handle_page_fault(page_number):
    global page_faults
    global disk_reads
    global disk_writes
    global time_counter

    page_faults += 1

    print(f"\nPAGE FAULT: Page {page_number} not in RAM")

    # Find least recently used page
    lru_page = find_lru_page()

    print(f"Removing Page {lru_page.page_number}")

    # If dirty, write to disk
    if lru_page.is_dirty:
        print(f"Writing dirty page {lru_page.page_number} to disk")
        disk_writes += 1

    # Remove old page from RAM
    lru_page.is_valid = False

    # Load requested page
    new_page = virtual_memory[page_number]

    new_page.is_valid = True
    new_page.last_used = time_counter

    disk_reads += 1

    # Replace in physical memory
    index = physical_memory.index(lru_page)
    physical_memory[index] = new_page

    print(f"Loaded Page {page_number} into RAM")


# -----------------------------
# ACCESS MEMORY
# -----------------------------

def access_memory(page_number, write=False):
    global time_counter

    page = virtual_memory[page_number]

    # PAGE IS IN RAM
    if page.is_valid:
        print(f"\nAccessing Page {page_number}")

    # PAGE FAULT
    else:
        handle_page_fault(page_number)

    # Update usage time
    page.last_used = time_counter
    time_counter += 1

    # If write operation
    if write:
        page.is_dirty = True
        print(f"Page {page_number} marked DIRTY")


# -----------------------------
# DISPLAY MEMORY
# -----------------------------

def display_memory():
    print("\n========== PHYSICAL MEMORY ==========")

    for i, page in enumerate(physical_memory):
        print(f"Frame {i}: {page}")

    print("\n========== VIRTUAL MEMORY ==========")

    for i, page in enumerate(virtual_memory):
        print(f"Virtual Page {i}: {page}")


# -----------------------------
# DISPLAY STATISTICS
# -----------------------------

def display_stats():
    print("\n========== STATISTICS ==========")
    print(f"Page Faults : {page_faults}")
    print(f"Disk Reads  : {disk_reads}")
    print(f"Disk Writes : {disk_writes}")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():
    initialize_memory()

    display_memory()

    # Simulated memory accesses
    access_memory(0)
    access_memory(1, write=True)
    access_memory(5)
    access_memory(6)
    access_memory(1)
    access_memory(7, write=True)
    access_memory(2)

    display_memory()

    display_stats()


# Run Program
main()
