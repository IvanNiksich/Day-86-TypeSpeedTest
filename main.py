import tkinter as tk
from tkinter import ttk, font
import datetime as dt
import random


TEXT_TO_DISPLAY = [
    "the", "and", "for", "not", "are", "from", "your", "all", "have", "new", "more", "was", "will", "home",
    "about", "page", "has", "search", "free", "our", "one", "other", "information", "time", "they", "site",
    "may", "what", "which", "their", "news", "out", "use", "any", "there", "see", "only", "his", "when",
    "contact", "here", "business", "who", "also", "help", "get", "view", "online", "first", "been", "would",
    "how", "were", "services", "some", "these", "click", "its", "like", "service", "than", "find", "price",
    "date", "back", "top", "people", "had", "list", "name", "just", "over", "state", "year", "day", "into",
    "email", "two", "health", "world", "next", "used", "work", "last", "most", "products", "music", "buy",
    "data", "make", "them", "should", "product", "system", "post", "her", "city", "add", "policy", "number",
    "such", "please", "available", "copyright", "support", "message", "after", "best", "software", "then",
    "good", "video", "well", "where", "info", "rights", "public", "books", "high", "school", "through",
    "each", "links", "review", "years", "order", "very", "privacy", "book", "items", "company", "read",
    "group", "need", "many", "user", "said", "does", "set", "under", "general", "research", "university",
    "mail", "full", "map", "reviews", "program", "life", "know", "games", "days", "management", "part",
    "could", "great", "united", "hotel", "real", "item", "international", "center", "must", "store", "travel",
    "comments", "made", "development", "report", "member", "details", "line", "terms", "before", "hotels",
    "send", "right", "type", "because", "local", "those", "using", "results", "office", "education",
    "national", "design", "take", "posted", "internet", "address", "community", "within", "states", "area",
    "want", "phone", "shipping", "reserved", "subject", "between", "forum", "family", "long", "based",
    "show", "even", "black", "check", "special", "prices", "website", "index", "being", "women", "much",
    "sign", "file", "link", "open", "today", "technology", "south", "case", "project", "same", "pages",
    "version", "section", "found", "sports", "house", "related", "security", "both", "county", "american",
    "photo", "game", "members", "power", "while", "care", "network", "down", "computer", "systems", "three",
    "total", "place", "following", "download", "without", "access", "think", "north", "resources", "current",
    "posts", "media", "control", "water", "history", "pictures", "size", "personal", "since", "including",
    "guide", "shop", "directory", "board", "location", "change", "white", "text", "small", "rating", "rate",
    "government", "children", "during", "return", "students", "shopping", "account", "times", "sites",
    "level", "digital", "profile", "previous", "form", "events", "love", "main", "call", "hours", "image",
    "department", "title", "description", "shall", "property", "class", "still", "money", "quality",
    "every", "listing", "content", "country", "private", "little", "visit", "save", "tools", "reply",
    "customer", "december", "compare", "movies", "include", "college", "value", "article", "card", "jobs",
    "provide", "food", "source", "different", "press", "learn", "sale", "around", "print", "course", "job",
    "process", "teen", "room", "stock", "training", "join", "science", "categories", "advanced", "west",
    "sales", "look", "english", "left", "team", "estate", "conditions", "select", "windows", "photos",
    "thread", "week", "category", "live", "large", "gallery", "table", "register", "however", "june",
    "october", "november", "market", "library", "really", "action", "start", "series", "model", "features",
    "industry", "plan", "human", "provided", "required", "second", "accessories", "cost", "movie", "forums",
    "march", "better", "questions", "july", "going", "medical", "test", "friend", "server", "study",
    "application", "cart", "staff", "articles", "feedback", "again", "play", "looking", "issues", "april",
    "never", "users", "complete", "street", "topic", "comment", "financial", "things", "working", "against",
    "standard", "person", "mobile", "less", "blog", "party", "payment", "equipment", "login", "student",
    "programs", "offers", "legal", "above", "recent", "stores", "side", "problem", "red", "give", "memory",
    "performance", "social", "quote", "language", "story", "sell", "options", "experience", "rates",
    "create", "body", "young", "important", "field", "east", "paper", "single", "age", "activities", "club",
    "example", "girls", "additional", "latest", "something", "road", "gift", "question", "changes", "night",
    "hard", "pay", "four", "status", "browse", "issue", "range", "building", "seller", "court", "always",
    "result", "audio", "light", "write", "war", "offer", "blue", "groups", "easy", "given", "files",
    "event", "release", "analysis", "request", "china", "making", "picture", "needs", "possible",
    "professional", "month", "major", "star", "areas", "future", "space", "committee", "hand", "sun",
    "cards", "problems", "london", "meeting", "become", "interest", "child", "keep", "enter", "california",
    "share", "similar", "garden", "schools", "million", "added", "reference", "companies", "listed",
    "learning", "energy", "run", "delivery", "popular", "term", "film", "stories", "computers", "journal",
    "reports", "central", "images", "president", "notice", "original", "head", "radio", "until", "color",
    "self", "council", "away", "includes", "track", "australia", "discussion", "archive", "others",
    "entertainment", "agreement", "format", "least", "society", "months", "safety", "trade", "edition",
    "cars", "messages", "marketing", "further", "updated", "association", "able", "having", "provides",
    "david", "already", "green", "studies", "close", "common", "drive", "specific", "several", "feb",
    "living", "collection", "called", "short", "arts", "display", "limited", "powered", "solutions",
    "director", "daily", "beach", "natural", "whether", "due", "five", "upon", "period", "planning",
    "database", "says", "official", "weather", "technical", "window", "region", "record", "direct",
    "microsoft", "conference", "environment", "records", "district", "calendar", "costs", "style", "front",
    "statement", "update", "parts", "august", "ever", "downloads", "early", "miles", "sound", "resource",
    "present", "applications", "either", "ago", "document", "works", "material", "written", "federal",
    "hosting", "rules", "final", "adult", "tickets", "thing", "centre", "requirements", "case", "under",
    "purchase", "seen", "home", "student", "photo"
]



class MyApp(tk.Tk):
    def __init__(self):  # Runs when an instance of MyApp is created
        super().__init__()  # Initializes the parent class (tk.Tk) to inherit all the properties and methods

        # Main window configurations
        self.title("Type Speed Test - Day 86 of a 100 Days of Code Python Bootcamp")

        # Center the window and define geometry
        self.center_window()

        # Initialize the layout
        self.create_widgets()

        # Start and Stop times vars used to calculate word per minute
        self.start_time = None
        self.stop_time = None

        self.text_to_show = ""

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
        # Randomly choose 40 words
        self.text_to_show = random.sample(TEXT_TO_DISPLAY, 40)

        # Define a font with a larger size
        text_font = font.Font(family="Arial", size=14)  # Change "Arial" and 14 as needed

        self.fixed_text_area.config(state="normal")  # Allow editing to update
        self.fixed_text_area.delete(1.0, tk.END)  # Clear the current text
        self.fixed_text_area.insert(tk.END, self.text_to_show)  # Insert new text

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

        # Get the words and check if the words are written correctly and count only valid words
        text_input = self.long_input_area.get("1.0", tk.END)  # Get all text from the Text widget
        print(text_input)

        words = text_input.split()
        correct_words = self.text_to_show
        numer_of_correct_words = 0

        # Checks word by word if they are correctly typed
        for i in range(len(correct_words)):
            try:
                if correct_words[i] == words[i]:
                    numer_of_correct_words += 1
            except IndexError:
                pass
        print(numer_of_correct_words)

        # Calculate words per minute
        words_per_minute = int((numer_of_correct_words / type_time) * 60000)
        print(words_per_minute)

        # TODO show new window at stop to show correct words and wpm


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
