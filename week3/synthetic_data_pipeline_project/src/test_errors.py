from data_generator import DataGenerator, DataGenerationError, InvalidFilePathError

def demonstrate_error_handling():
    """Demonstrate exception handling in action."""
    print("🧪 Exception Handling Demonstration\n")
    
    generator = DataGenerator()
    
    print("=" * 50)
    print("TEST 1: Invalid n_samples (string instead of int)")
    print("=" * 50)
    try:
        generator.generate_dataset("500")  # This will fail
    except DataGenerationError as e:
        print(f"✅ Successfully caught error: {e}")
    
    print("\n" + "=" * 50)
    print("TEST 2: Invalid n_samples (negative number)")  
    print("=" * 50)
    try:
        generator.generate_dataset(-100)  # This will fail
    except DataGenerationError as e:
        print(f"✅ Successfully caught error: {e}")
    
    print("\n" + "=" * 50)
    print("TEST 3: Invalid file path (wrong extension)")
    print("=" * 50)
    try:
        data = generator.generate_dataset(50)
        generator.save_dataset(data, "data.txt")  # This will fail
    except InvalidFilePathError as e:
        print(f"✅ Successfully caught error: {e}")
    
    print("\n" + "=" * 50)
    print("TEST 4: Invalid file path (special characters)")
    print("=" * 50)
    try:
        data = generator.generate_dataset(50)
        generator.save_dataset(data, "bad<file>name.csv")  # This will fail
    except InvalidFilePathError as e:
        print(f"✅ Successfully caught error: {e}")
    
    print("\n🎯 All exception handling tests completed!")
    print("📝 Check ../logs/errors.txt for logged errors!")

if __name__ == "__main__":
    demonstrate_error_handling()
