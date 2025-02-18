#!/usr/bin/python3
import os
#function to print current working directory
def print_current_directory():
	pwd=os.getcwd()
	print(f"Current Directory: {pwd}")

def change_current_dir(new_path):
	if new_path:
		os.chdir(new_path)
	else:
		pwd=os.chdir('../')

def create_a_file(file_name):
	clean_name=file_name.strip()
	new_file=open(clean_name,'x')
	print(f"File '{clean_name}' created successfully.")

def write_content_file(file_name, file_content):
	with open(file_name,'w')as f:
		f.write(file_content)
	print(f"Content written to '{file_name}' successfully.")

def delete_file(file_name):
	clean_name = file_name.strip()  # Clean file name by removing leading/trailing spaces
	current_dir = os.getcwd()  # Get the current working directory
	full_path = os.path.join(current_dir, clean_name)  # Construct the full path to the file
	os.remove(full_path)
	print(f"File deleted: {full_path}")

gameover=False
while not gameover:
	print("\n ******************************************************************************************")
	cmd=input("shell>> ")
	if cmd == "exit":
		print("[+]Good Bye!!")
		gameover=True
	elif cmd=="pwd":
		print_current_directory()
	elif "cd" in cmd:
		#print(cmd[3:] or None)
		change_current_dir(cmd[3:])
		print_current_directory()
	elif "touch" in cmd:
		#print(cmd[5:])
		create_a_file(cmd[5:])
	elif "echo" in cmd:
		parts = cmd.split(">", 1)  # Split at '>' to separate file name and content
		if len(parts) == 2:
			file_content = parts[0].replace("echo", "").strip().strip('"') 
			'''.replace("echo", "") → Removes the "echo" keyword from the string. 
			   .strip() → Removes leading and trailing spaces to clean the extracted content.'''
			file_name = parts[1].strip()
			write_content_file(file_name, file_content)
	elif "rm" in cmd:
		#print(cmd[3:])
		delete_file(cmd[3:])
	else:
		os.system(cmd)
