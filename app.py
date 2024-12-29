import streamlit as st
from fractions import Fraction

def main():
    st.title("✨ Fraction Calculator ✨")
    st.markdown("Perform operations on fractions like \( P = \\frac{n}{d} \) and \( Q = \\frac{n}{d} \).")

    # Input for Fraction 1
    st.write("### Enter Fraction 1 (P = n/d):")
    col1, col2 = st.columns(2)
    with col1:
        numerator1 = st.number_input("Numerator (n)", value=1, step=1, key="num1")
    with col2:
        denominator1 = st.number_input("Denominator (d)", value=1, step=1, key="den1")

    # Input for Fraction 2
    st.write("### Enter Fraction 2 (Q = n/d):")
    col3, col4 = st.columns(2)
    with col3:
        numerator2 = st.number_input("Numerator (n)", value=1, step=1, key="num2")
    with col4:
        denominator2 = st.number_input("Denominator (d)", value=1, step=1, key="den2")

    try:
        # Construct fractions
        fraction1 = Fraction(numerator1, denominator1)
        fraction2 = Fraction(numerator2, denominator2)

        st.write(f"**Fraction 1 (P = n/d)**: {fraction1}")
        st.write(f"**Fraction 2 (Q = n/d)**: {fraction2}")

        # Horizontal alignment for operations
        st.write("### Choose Operation:")
        col_op1, col_op2, col_op3, col_op4 = st.columns(4)

        with col_op1:
            if st.button("➕ Add"):
                result = fraction1 + fraction2
                st.success(f"Result: {result}")

        with col_op2:
            if st.button("➖ Subtract"):
                result = fraction1 - fraction2
                st.success(f"Result: {result}")

        with col_op3:
            if st.button("✖️ Multiply"):
                result = fraction1 * fraction2
                st.success(f"Result: {result}")

        with col_op4:
            if st.button("➗ Divide"):
                result = fraction1 / fraction2
                st.success(f"Result: {result}")

    except ZeroDivisionError:
        st.error("Denominator cannot be zero. Please enter a valid denominator.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
