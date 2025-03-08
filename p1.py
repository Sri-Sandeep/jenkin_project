def list_operations(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    print(f"Sum: {total}")
    print(f"Max: {maximum}")
    print(f"Min: {minimum}")

if __name__ == "__main__":
    sample_list = [10, 20, 5, 40, 25]
    list_operations(sample_list)
