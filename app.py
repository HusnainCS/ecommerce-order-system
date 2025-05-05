import streamlit as st

# Initialize session state
if 'stack_recent_order' not in st.session_state:
    st.session_state.stack_recent_order = []

if 'queue_pending_order' not in st.session_state:
    st.session_state.queue_pending_order = []

# Callback function to handle order placement and clear input
def place_order():
    product = st.session_state.product_input
    if product:
        st.session_state.stack_recent_order.append(product)
        st.session_state.queue_pending_order.append(product)
        st.success(f"Order placed for: {product}")
        st.session_state.product_input = ""  # Clear input here safely
    else:
        st.warning("Please enter a product name.")

st.title("🛒 E-Commerce Order Processing System")

# Input with key and on_change callback
st.text_input("Enter Product Name:", key="product_input", on_change=place_order)

# Display Buttons
if st.button("View Recent Orders"):
    if st.session_state.stack_recent_order:
        st.subheader("Recent Orders (Stack)")
        st.write("  \n".join(st.session_state.stack_recent_order))
    else:
        st.info("No recent orders found.")

if st.button("View Pending Orders"):
    if st.session_state.queue_pending_order:
        st.subheader("Pending Orders (Queue)")
        st.write("  \n".join(st.session_state.queue_pending_order))
    else:
        st.info("No pending orders found.")

if st.button("Process Next Order"):
    if st.session_state.queue_pending_order:
        processed = st.session_state.queue_pending_order.pop(0)
        st.success(f"Processed order: {processed}")
    else:
        st.warning("No pending orders to process.")
