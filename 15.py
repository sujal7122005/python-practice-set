'''
Write all file content into new file byskipping line 5 from following file.
'''
with open('6.py', 'r') as source_file:
    lines = source_file.readlines()
with open('15_new.py', 'w') as target_file:
    for i, line in enumerate(lines):
        if i != 4:  # Skip line 5 (index 4)
            target_file.write(line)