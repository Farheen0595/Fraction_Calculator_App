import streamlit as st
from fractions import Fraction

def main():
    st.title("✨ Fraction Calculator ✨")
    st.markdown("Perform operations on fractions with separate numerator and denominator inputs!")

    # Sidebar inputs for fractions
    st.sidebar.header("Input Fractions")
    st.sidebar.subheader("Fraction 1")
    num1 = st.sidebar.number_input("Numerator 1", value=1, step=1)
    den1 = st.sidebar.number_input("Denominator 1", value=1, step=1)

    st.sidebar.subheader("Fraction 2")
    num2 = st.sidebar.number_input("Numerator 2", value=1, step=1)
    den2 = st.sidebar.number_input("Denominator 2", value=1, step=1)

    try:
        # Create fraction objects
        fraction1 = Fraction(num1, den1)
        fraction2 = Fraction(num2, den2)

        st.write(f"**Fraction 1**: {fraction1}")
        st.write(f"**Fraction 2**: {fraction2}")

        # Horizontal layout for operations
        st.write("### Choose Operation:")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("➕ Add"):
                result = fraction1 + fraction2
                st.success(f"Result: {result}")

        with col2:
            if st.button("➖ Subtract"):
                result = fraction1 - fraction2
                st.success(f"Result: {result}")

        with col3:
            if st.button("✖️ Multiply"):
                result = fraction1 * fraction2
                st.success(f"Result: {result}")

        with col4:
            if st.button("➗ Divide"):
                result = fraction1 / fraction2
                st.success(f"Result: {result}")

    except ZeroDivisionError:
        st.error("Denominator cannot be zero. Please enter a valid denominator.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
