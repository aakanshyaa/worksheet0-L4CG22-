def generate_permutations(s):
    if len(s) <= 1:
        return [s]
    
    permutations = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in generate_permutations(remaining):
            permutations.append(char + perm)
 
    return list(set(permutations))

print(generate_permutations("abc"))  
print(generate_permutations("aab"))  
