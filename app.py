import streamlit as st

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


st.title("Binary Search vs Interpolation Search")

arr_input = st.text_input(
    "Enter sorted array elements separated by spaces"
)

target = st.number_input(
    "Enter target element",
    step=1
)

if st.button("Search"):
    try:
        arr = list(map(int, arr_input.split()))

        idx_is, comp_is = interpolation_search(arr, int(target))
        idx_bs, comp_bs = binary_search(arr, int(target))

        st.subheader("Results")

        st.write("Array:", arr)
        st.write("Target:", int(target))

        st.write("### Interpolation Search")
        st.write("Index:", idx_is)
        st.write("Comparisons:", comp_is)

        st.write("### Binary Search")
        st.write("Index:", idx_bs)
        st.write("Comparisons:", comp_bs)

    except:
        st.error("Please enter valid sorted integer values.")
