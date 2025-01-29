
import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# Function to draw the data on the canvas
def draw_data(data, color_array, description):
    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data, color=color_array)
    plt.title(description)
    st.pyplot(fig)
    plt.close(fig)

# Function to convert a comma-separated string to a list of integers
def convert_to_list(input_str):
    try:
        return [int(x) for x in input_str.split(',')]
    except ValueError:
        st.error("Please enter a valid comma-separated list of integers.")
        return []

# Sorting Algorithms
def bubble_sort(data, speed):
    st.text("Starting Bubble Sort...")
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))], f"Swapping elements at positions {j} and {j+1}")
                time.sleep(speed)
    draw_data(data, ['green' for x in range(len(data))], "Bubble Sort Completed!")

def selection_sort(data, speed):
    st.text("Starting Selection Sort...")
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, ['green' if x == i or x == min_idx else 'red' for x in range(len(data))], f"Swapping elements at positions {i} and {min_idx}")
        time.sleep(speed)
    draw_data(data, ['green' for x in range(len(data))], "Selection Sort Completed!")

def merge_sort(data, speed):
    st.text("Starting Merge Sort...")
    
    def merge_sort_helper(data, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(data, left, mid)
            merge_sort_helper(data, mid + 1, right)
            merge(data, left, mid, right)

    def merge(data, left, mid, right):
        left_part = data[left:mid + 1]
        right_part = data[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                data[k] = left_part[i]
                i += 1
            else:
                data[k] = right_part[j]
                j += 1
            k += 1
            draw_data(data, ['green' if x >= left and x <= right else 'red' for x in range(len(data))], "Merging parts")
            time.sleep(speed)

        while i < len(left_part):
            data[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            data[k] = right_part[j]
            j += 1
            k += 1

    merge_sort_helper(data, 0, len(data) - 1)
    draw_data(data, ['green' for x in range(len(data))], "Merge Sort Completed!")

def quick_sort(data, speed):
    st.text("Starting Quick Sort...")
    
    def quick_sort_helper(data, low, high):
        if low < high:
            pi = partition(data, low, high)
            quick_sort_helper(data, low, pi - 1)
            quick_sort_helper(data, pi + 1, high)

    def partition(data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                draw_data(data, ['yellow' if x == i or x == j else 'red' for x in range(len(data))], f"Swapping elements at positions {i} and {j} with pivot {high}")
                time.sleep(speed)
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    quick_sort_helper(data, 0, len(data) - 1)
    draw_data(data, ['green' for x in range(len(data))], "Quick Sort Completed!")

# Searching Algorithms
def linear_search(data, speed, search_value):
    st.text("Starting Linear Search...")
    for i in range(len(data)):
        draw_data(data, ['blue' if x == i else 'red' for x in range(len(data))], f"Checking element at position {i}")
        time.sleep(speed)
        if data[i] == search_value:
            draw_data(data, ['green' if x == i else 'red' for x in range(len(data))], f"Element found at position {i}")
            return True
    draw_data(data, ['red' for x in range(len(data))], "Element not found")
    return False

def binary_search(data, speed, search_value):
    st.text("Starting Binary Search...")
    left = 0
    right = len(data) - 1
    data.sort()  # Ensure the data is sorted before binary search
    while left <= right:
        mid = (left + right) // 2
        draw_data(data, ['yellow' if x == mid else 'blue' if left <= x <= right else 'red' for x in range(len(data))], f"Checking element at position {mid}")
        time.sleep(speed)
        if data[mid] == search_value:
            draw_data(data, ['green' if x == mid else 'red' for x in range(len(data))], f"Element found at position {mid}")
            return True
        elif data[mid] < search_value:
            left = mid + 1
        else:
            right = mid - 1
    draw_data(data, ['red' for x in range(len(data))], "Element not found")
    return False

# Streamlit interface
st.title("Algorithm Visualizer")

st.sidebar.title("Settings")
visualization_type = st.sidebar.radio("Choose Visualization", ["Sorting", "Searching"])

data_str = st.sidebar.text_area("Enter array elements (comma-separated)", "10, 20, 30, 40, 50")
data = convert_to_list(data_str)

speed = st.sidebar.slider("Speed", 0.2, 5.0, 1.0)

if visualization_type == "Sorting":
    selected_algorithm = st.sidebar.selectbox("Sorting Algorithm", ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort'])
    if st.button("Start"):
        if selected_algorithm == 'Bubble Sort':
            bubble_sort(data, speed)
        elif selected_algorithm == 'Selection Sort':
            selection_sort(data, speed)
        elif selected_algorithm == 'Merge Sort':
            merge_sort(data, speed)
        elif selected_algorithm == 'Quick Sort':
            quick_sort(data, speed)

elif visualization_type == "Searching":
    search_value = st.sidebar.number_input("Search Value", min_value=0)
    selected_algorithm = st.sidebar.selectbox("Searching Algorithm", ['Linear Search', 'Binary Search'])
    if st.button("Start"):
        if selected_algorithm == 'Linear Search':
            found = linear_search(data, speed, search_value)
            if not found:
                st.write(f"Value {search_value} not found in the array.")
        elif selected_algorithm == 'Binary Search':
            found = binary_search(data, speed, search_value)
            if not found:
                st.write(f"Value {search_value} not found in the array.")
