import tkinter as tk
from tkinter import messagebox

def decode_bits(raw: str) -> str:
    """Convert a string of 8-bit binary groups into text."""
    bits = "".join(raw.split()) # drop spaces and newlines
    if not bits:
        raise ValueError("Please enter some binary first.")
    if set(bits) - {"0", "1"}:
        raise ValueError("Input can only contain 0s and 1s.")
    if len(bits) % 8 != 0:
        raise ValueError(f"Got {len(bits)} bits. The total must be a multiple of 8.")
    chunks = [bits[i:i + 8] for i in range(0, len(bits), 8)]
    return "".join(chr(int(chunk, 2)) for chunk in chunks)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binary Decoder")
        self.geometry("480x420")
        self.minsize(360, 340)

        tk.Label(self, text="Enter binary (8-bit groups):").pack(anchor="w", padx=12, pady=(12, 0))
        self.input_box = tk.Text(self, height=8, wrap="word", font=("Consolas", 11))
        self.input_box.pack(fill="both", expand=True, padx=12, pady=6)

        buttons = tk.Frame(self)
        buttons.pack(fill="x", padx=12)
        tk.Button(buttons, text="Decode", command=self.on_decode).pack(side="left")
        tk.Button(buttons, text="Copy output", command=self.on_copy).pack(side="left", padx=6)
        tk.Button(buttons, text="Clear", command=self.on_clear).pack(side="left")

        tk.Label(self, text="Output:").pack(anchor="w", padx=12, pady=(12, 0))
        self.output_box = tk.Text(self, height=5, wrap="word", font=("Consolas", 11), state="disabled")
        self.output_box.pack(fill="both", expand=True, padx=12, pady=(6, 12))

    def set_output(self, text: str):
        self.output_box.config(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", text)
        self.output_box.config(state="disabled")

    def on_decode(self):
        raw = self.input_box.get("1.0", "end")
        try:
            self.set_output((decode_bits(raw)))
        except ValueError as err:
            messagebox.showerror("Invalid input", str(err))

    def on_copy(self):
        text = self.output_box.get("1.0", "end").strip()
        self.clipboard_clear()
        self.clipboard_append(text)

    def on_clear(self):
        self.input_box.delete("1.0", "end")
        self.set_output("")

if __name__ == "__main__":
    App().mainloop()