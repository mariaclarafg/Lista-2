def reverse_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as f_input:
            with open(output_file, 'w') as f_output:
                lines = f_input.readlines()
                reversed_lines = [line.strip()[::-1] + '\n' for line in lines]
                f_output.writelines(reversed_lines)
        print("Reversed content saved to", output_file)
    except FileNotFoundError:
        print("File not found.")

input_file = input("Enter the name of the input text file: ")
output_file = input("Enter the name of the output text file: ")

reverse_lines(input_file, output_file)