def calculate_directory_size(directory):
    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict): 
            total_size += calculate_directory_size(value)  
        else:  
            total_size += value
    return total_size

sample_directory = {
    "file1.txt": 100,  
    "file2.txt": 200,
    "subdir1": {
        "file3.txt": 300,
        "file4.txt": 400,
        "subsubdir1": {
            "file5.txt": 500
        }
    },
    "subdir2": {
        "file6.txt": 600,
        "file7.txt": 700
    }
}

result = calculate_directory_size(sample_directory)
print(f"Total directory size: {result} KB")
