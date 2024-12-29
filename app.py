import streamlit as st
from fractions import Fraction

def main():
    st.title("✨ Fraction Calculator ✨")
    st.write("Perform operations on fractions \( P = \\frac{n}{d} \) and \( Q = \\frac{n}{d} \).")

    # Input for P = n/d and Q = n/d in one line
    st.write("### Enter Fractions:")
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([0.5, 1, 0.3, 1, 0.5, 0.5, 0.5, 0.3, 1])
    with col1:
        st.write("P = ")
    with col2:
        numerator1 = st.number_input("Numerator P", value=1, step=1, key="num1", label_visibility="collapsed")
    with col3:
        st.write("/")
    with col4:
        denominator1 = st.number_input("Denominator P", value=1, step=1, key="den1", label_visibility="collapsed")
    with col5:
        st.write("     Q = ")
    with col6:
        numerator2 = st.number_input("Numerator Q", value=1, step=1, key="num2", label_visibility="collapsed")
    with col7:
        st.write("/")
    with col8:
        denominator2 = st.number_input("Denominator Q", value=1, step=1, key="den2", label_visibility="collapsed")

    try:
        # Construct fractions
        fraction1 = Fraction(numerator1, denominator1)
        fraction2 = Fraction(numerator2, denominator2)

        st.write(f"**Fraction P = n/d**: {fraction1}")
        st.write(f"**Fraction Q = n/d**: {fraction2}")

        # Display operations and results
        st.write("### Choose Operation and View Result:")
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
