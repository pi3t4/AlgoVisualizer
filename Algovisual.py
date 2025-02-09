
import tkinter as tk
from tkinter import ttk
import random

# Constants
WIDTH = 1000
HEIGHT = 600
MIN_VAL = 0
MAX_VAL = 100
NUM_BARS = 50
GRADIENT = ["#FF6B6B", "#FFE66D", "#4ECDC4", "#556270"]  # Gradient colors for bars

# Sorting Algorithms
def bubble_sort(data, draw, ascending=True):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if (data[j] > data[j + 1] and ascending) or (data[j] < data[j + 1] and not ascending):
                data[j], data[j + 1] = data[j + 1], data[j]
                draw(data, {j: "#4ECDC4", j + 1: "#FF6B6B"})
                yield True

def insertion_sort(data, draw, ascending=True):
    for i in range(1, len(data)):
        current = data[i]
        while True:
            ascending_sort = i > 0 and data[i - 1] > current and ascending
            descending_sort = i > 0 and data[i - 1] < current and not ascending
            if not ascending_sort and not descending_sort:
                break
            data[i] = data[i - 1]
            i -= 1
            data[i] = current
            draw(data, {i: "#4ECDC4", i - 1: "#FF6B6B"})
            yield True

def selection_sort(data, draw, ascending=True):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if (data[j] < data[min_idx] and ascending) or (data[j] > data[min_idx] and not ascending):
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw(data, {i: "#4ECDC4", min_idx: "#FF6B6B"})
        yield True

def merge_sort(data, draw, ascending=True):
    def merge(arr, l, m, r):
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if (left[i] <= right[j] and ascending) or (left[i] >= right[j] and not ascending):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        draw(arr, {x: "#4ECDC4" for x in range(l, r + 1)})
        yield True

    def sort(arr, l, r):
        if l < r:
            m = (l + r) // 2
            yield from sort(arr, l, m)
            yield from sort(arr, m + 1, r)
            yield from merge(arr, l, m, r)

    yield from sort(data, 0, len(data) - 1)

def quick_sort(data, draw, ascending=True):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if (arr[j] <= pivot and ascending) or (arr[j] >= pivot and not ascending):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                draw(arr, {i: "#4ECDC4", j: "#FF6B6B"})
                yield True
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(arr, low, high):
        if low < high:
            pi = yield from partition(arr, low, high)
            yield from sort(arr, low, pi - 1)
            yield from sort(arr, pi + 1, high)

    yield from sort(data, 0, len(data) - 1)

def heap_sort(data, draw, ascending=True):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and ((arr[left] > arr[largest] and ascending) or (arr[left] < arr[largest] and not ascending)):
            largest = left
        if right < n and ((arr[right] > arr[largest] and ascending) or (arr[right] < arr[largest] and not ascending)):
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            draw(arr, {i: "#4ECDC4", largest: "#FF6B6B"})
            yield True
            yield from heapify(arr, n, largest)

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        yield from heapify(data, i, 0)

# Main Application
class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.configure(bg="#F5F5F5")
        self.data = []
        self.generate_data()
        self.setup_ui()
        self.draw_data()

    def generate_data(self):
        self.data = [random.randint(MIN_VAL, MAX_VAL) for _ in range(NUM_BARS)]

    def draw_data(self, color_positions={}):
        self.canvas.delete("all")
        bar_width = (WIDTH - 40) / len(self.data)
        for i, val in enumerate(self.data):
            x0 = 20 + i * bar_width
            y0 = HEIGHT - 80 - (val / MAX_VAL) * (HEIGHT - 120)
            x1 = 20 + (i + 1) * bar_width
            y1 = HEIGHT - 80
            color = GRADIENT[i % len(GRADIENT)]
            if i in color_positions:
                color = color_positions[i]
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)

    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Sorting Algorithm Visualizer", font=("Helvetica", 20, "bold"), bg="#F5F5F5", fg="#333333")
        title.pack(pady=10)

        # Canvas
        self.canvas = tk.Canvas(self.root, width=WIDTH - 40, height=HEIGHT - 160, bg="#FFFFFF", bd=0, highlightthickness=0)
        self.canvas.pack(pady=10)

        # Controls Frame
        controls = tk.Frame(self.root, bg="#F5F5F5")
        controls.pack(pady=10)

        # Algorithm Selection
        self.algo_var = tk.StringVar(value="Bubble Sort")
        algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort", "Heap Sort"]
        for algo in algorithms:
            tk.Radiobutton(controls, text=algo, variable=self.algo_var, value=algo, font=("Helvetica", 12), bg="#F5F5F5", fg="#333333").pack(side=tk.LEFT, padx=10)

        # Order Selection
        self.ascending_var = tk.BooleanVar(value=True)
        tk.Radiobutton(controls, text="Ascending", variable=self.ascending_var, value=True, font=("Helvetica", 12), bg="#F5F5F5", fg="#333333").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(controls, text="Descending", variable=self.ascending_var, value=False, font=("Helvetica", 12), bg="#F5F5F5", fg="#333333").pack(side=tk.LEFT, padx=10)

        # Buttons
        tk.Button(controls, text="Reset", command=self.reset, font=("Helvetica", 12), bg="#4ECDC4", fg="white", bd=0, padx=10, pady=5).pack(side=tk.LEFT, padx=10)
        tk.Button(controls, text="Start", command=self.start_sorting, font=("Helvetica", 12), bg="#FF6B6B", fg="white", bd=0, padx=10, pady=5).pack(side=tk.LEFT, padx=10)

        # Status Bar
        self.status = tk.Label(self.root, text="Ready", font=("Helvetica", 12), bg="#F5F5F5", fg="#333333")
        self.status.pack(pady=10)

    def reset(self):
        self.generate_data()
        self.draw_data()
        self.status.config(text="Ready")

    def start_sorting(self):
        self.status.config(text=f"Sorting - {self.algo_var.get()} ({'Ascending' if self.ascending_var.get() else 'Descending'})")
        algo = self.algo_var.get()
        ascending = self.ascending_var.get()
        if algo == "Bubble Sort":
            generator = bubble_sort(self.data, self.draw_data, ascending)
        elif algo == "Insertion Sort":
            generator = insertion_sort(self.data, self.draw_data, ascending)
        elif algo == "Selection Sort":
            generator = selection_sort(self.data, self.draw_data, ascending)
        elif algo == "Merge Sort":
            generator = merge_sort(self.data, self.draw_data, ascending)
        elif algo == "Quick Sort":
            generator = quick_sort(self.data, self.draw_data, ascending)
        elif algo == "Heap Sort":
            generator = heap_sort(self.data, self.draw_data, ascending)

        self.animate(generator)

    def animate(self, generator):
        try:
            next(generator)
            self.root.after(50, lambda: self.animate(generator))
        except StopIteration:
            self.status.config(text="Sorting Complete")

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
