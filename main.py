import tkinter as tk
from tkinter import ttk, font
import datetime as dt


class MyApp(tk.Tk):
    def __init__(self):  # Runs when an instance of MyApp is created
        super().__init__()  # Initializes the parent class (tk.Tk) to inherit all the properties and methods

        # Main window configurations
        self.title("Type Speed Test - Day 86 of a 100 Days of Code Python Bootcamp")

        # Center the window and define geometry
        self.center_window()

        # Initialize the layout
        self.create_widgets()

        # Times
        self.start_time = None
        self.stop_time = None

    def center_window(self):    # This is called by the __init__
        """Centers the window on the screen."""
        # Define window size
        window_width = 600
        window_height = 500

        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates for the Tk root window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the geometry with position
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_widgets(self):  # This is called by the __init__
        """Set up all widgets in the main application window."""

        # Configure grid columns to allow for proper centering
        self.grid_columnconfigure(0, weight=1)  # Give column 0 a weight
        self.grid_columnconfigure(1, weight=1)  # Give column 1 a weight
        self.grid_columnconfigure(2, weight=1)  # Give column 2 a weight

        # Configure grid rows to allow for proper vertical distribution
        self.grid_rowconfigure(0, weight=1)  # Fixed text area row
        self.grid_rowconfigure(1, weight=1)  # Username row
        self.grid_rowconfigure(2, weight=1)  # Password row
        self.grid_rowconfigure(3, weight=1)  # Submit button row

        # Define a font with a larger size
        text_font = font.Font(family="Arial", size=14)  # Change "Arial" and 14 as needed

        # Read-only text area for fixed text
        self.fixed_text_area = tk.Text(self, height=10, width=50, wrap="word", state="normal")
        self.fixed_text_area.grid(row=0, column=0, columnspan=3, pady=10)

        # Insert fixed text
        fixed_text = "Press start button to begin when you are ready. After 3 seconds the text to write will show, when you finish typing it press Stop."
        self.fixed_text_area.insert(tk.END, fixed_text)

        # Apply the font to the entire text
        self.fixed_text_area.tag_configure("large_font", font=text_font)
        self.fixed_text_area.tag_add("large_font", "1.0", "end")

        # Make the text area read-only
        self.fixed_text_area.config(state="disabled")  # Disable editing

        # Define the font for user input area
        input_font = ("Arial", 14)  # Change to your preferred font and size

        # Long input text area for user input
        self.long_input_area = tk.Text(self, height=10, width=37, wrap="word", font=input_font)
        self.long_input_area.grid(row=1, column=0, columnspan=3, pady=10)

        input_frame = ttk.Frame(self)
        input_frame.grid(row=1, column=0, columnspan=3, pady=20)

        # Star button at the bottom left
        self.submit_button = ttk.Button(self, text="Start", command=self.on_start)
        self.submit_button.grid(row=3, column=2, sticky="s", padx=10, pady=20)

        # Stop button at the bottom left
        self.submit_button = ttk.Button(self, text="Stop", command=self.on_stop)
        self.submit_button.grid(row=3, column=2, sticky="se", padx=10, pady=20)

    def on_start(self):
        """Handle the start button click event."""
        text_to_show = ("happy sad love friend family home go come see look play run big small fast slow help think"
                        " work eat drink want need find yes no maybe thank sorry tell speak listen read write make do"
                        " beautiful smart funny kind brave interesting loud")

        # Define a font with a larger size
        text_font = font.Font(family="Arial", size=14)  # Change "Arial" and 14 as needed

        self.fixed_text_area.config(state="normal")  # Allow editing to update
        self.fixed_text_area.delete(1.0, tk.END)  # Clear the current text
        self.fixed_text_area.insert(tk.END, text_to_show)  # Insert new text

        # Apply the font to the entire text
        self.fixed_text_area.tag_configure("large_font", font=text_font)
        self.fixed_text_area.tag_add("large_font", "1.0", "end")

        self.fixed_text_area.config(state="disabled")  # Disable editing again

        self.long_input_area.focus_set()  # Change focus to the input text area

        # Optionally, clear the long input area for the user to type
        self.long_input_area.delete(1.0, tk.END)

        long_input = self.long_input_area.get("1.0", tk.END)  # Get all text from the Text widget
        print(long_input)

        # Get current datetime
        self.start_time = dt.datetime.now()

        # Format the time to include hours, minutes, seconds, and milliseconds
        formatted_time = self.start_time.strftime("%H:%M:%S.%f")[:-3]  # The [:-3] removes the last three digits of microseconds
        print("start time:", formatted_time)

    def on_stop(self):
        """Handle the stop button click event."""
        # Get current datetime
        self.stop_time = dt.datetime.now()
        # Format the time to include hours, minutes, seconds, and milliseconds
        formatted_time = self.stop_time.strftime("%H:%M:%S.%f")[:-3]  # The [:-3] removes the last three digits of microseconds
        print("stop time:", formatted_time)

        # Delta time
        type_time = self.stop_time - self.start_time
        type_time = (type_time.total_seconds() * 1000)
        print(f"Your time: {type_time:.0f}")

        text_input = self.long_input_area.get("1.0", tk.END)  # Get all text from the Text widget
        print(text_input)

        words = text_input.split()
        number_of_words = len(words)
        print(number_of_words)

        words_per_minute = int((number_of_words / type_time) * 60000)
        print(words_per_minute)

        # TODO check if the words are written correctly and count only valid words
        # TODO add a long ass list of words to choose 40 random words for the textbox


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
