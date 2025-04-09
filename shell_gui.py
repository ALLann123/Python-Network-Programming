import tkinter as tk
import subprocess
import threading

class ShellGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Shell")

        # Output Text Area
        self.output_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        # Scrollbar for Output
        scrollbar = tk.Scrollbar(self.output_text, command=self.output_text.yview)
        self.output_text.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Input Field
        self.input_entry = tk.Entry(root)
        self.input_entry.pack(fill=tk.X, padx=5, pady=5)
        self.input_entry.bind("<Return>", self.execute_command)

    def execute_command(self, event=None):
        """Execute the command entered in the input field."""
        command = self.input_entry.get().strip()
        if not command:
            return
        
        # Display the command in the output area
        self.append_output(f"> {command}\n")

        # Run the command in a separate thread to avoid GUI freezing
        thread = threading.Thread(target=self.run_command, args=(command,))
        thread.start()

        # Clear the input field
        self.input_entry.delete(0, tk.END)

    def run_command(self, command):
        """Runs shell command in a separate thread and captures output."""
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Read output line by line
            for line in process.stdout:
                self.append_output(line)

            for line in process.stderr:
                self.append_output(f"Error: {line}")

        except Exception as e:
            self.append_output(f"An error occurred: {str(e)}\n")

    def append_output(self, text):
        """Append text to the output area in a thread-safe manner."""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)  # Auto-scroll to the bottom

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    shell_gui = ShellGUI(root)
    root.mainloop()
